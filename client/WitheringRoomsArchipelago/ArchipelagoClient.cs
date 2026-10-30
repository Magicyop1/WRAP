using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Models;
using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using System.Collections;
using System.Collections.Generic;
using APItemInfo = Archipelago.MultiClient.Net.Models.ItemInfo;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Packets;

namespace WitheringRoomsArchipelago
{
    public sealed class PendingArchipelagoItem
    {
        public int Index { get; }
        public APItemInfo Item { get; }

        public PendingArchipelagoItem(
            int index,
            APItemInfo item)
        {
            Index = index;
            Item = item;
        }
    }
    public static class ArchipelagoClient
    {
        private static ArchipelagoSession? session;

        

        private static readonly ConcurrentQueue<PendingArchipelagoItem> pendingItems = new();

        public static bool Connected { get; private set; }

        public static string LastConnectionError { get; private set; } = "";

        public static ArchipelagoSession? Session => session;

        public static bool ChallengeStart { get; private set; } = false;
        public static bool Loresanity { get; private set; } = true;
        public static bool Monstersanity { get; private set; } = true;

        private static DeathLinkService? deathLinkService;


        public static bool DeathLinkEnabled { get; private set; } = false;

        private static readonly HashSet<string>
    completionGoals =
        new(StringComparer.OrdinalIgnoreCase);

        public static IReadOnlyCollection<string>
            CompletionGoals => completionGoals;

        public static async Task<bool> Connect(
    string server,
    string slotName,
    string gameName,
    string? password = null)
        {
            try
            {
                Plugin.LogSource.LogInfo(
                    $"[AP] Creating session for {server}..."
                );

                session =
                    ArchipelagoSessionFactory.CreateSession(server);

                Plugin.LogSource.LogInfo(
                    "[AP] Session created."
                );

                session.Items.ItemReceived += OnItemReceived;
                session.Socket.SocketClosed += OnSocketClosed;

                Plugin.LogSource.LogInfo(
                    "[AP] Calling ConnectAsync..."
                );

                await session.ConnectAsync();

                Plugin.LogSource.LogInfo(
                    "[AP] Socket connected. Calling LoginAsync..."
                );

                LoginResult result =
                    await session.LoginAsync(
                        gameName,
                        slotName,
                        ItemsHandlingFlags.AllItems,
                        password: password
                    );

                Plugin.LogSource.LogInfo(
                    $"[AP] Login returned. Successful={result.Successful}"
                );

                if (!result.Successful)
                {
                    LoginFailure failure =
                        (LoginFailure)result;

                    foreach (string error in failure.Errors)
                    {
                        Plugin.LogSource.LogError(
                            $"[AP] Login error: {error}"
                        );
                    }

                    Connected = false;
                    return false;
                }

                Connected = true;

                Plugin.LogSource.LogInfo(
                    $"[AP] Connected successfully as {slotName}."
                );

                return true;
            }
            catch (Exception ex)
            {
                Connected = false;

                Plugin.LogSource.LogError(
                    $"[AP] Connection exception: {ex}"
                );

                return false;
            }
        }

        private static readonly object itemSyncLock = new();

        private static int receivedEventIndex = 0;

        /*
         * ItemReceived callbacks can begin during TryConnectAndLogin(),
         * before ArchipelagoState.Initialize() has loaded ProcessedItemCount.
         *
         * Until initialization is complete, buffer every received item instead
         * of deciding whether it is old or new.
         */
        private static bool receivedItemStateReady = false;

        private static readonly Queue<PendingArchipelagoItem>
            preStateReceivedItems = new();

        private static bool GetSlotDataBool(
            Dictionary<string, object> slotData,
            string key,
            bool defaultValue)
                {
                    if (!slotData.TryGetValue(key, out object? value))
                        return defaultValue;

                    try
                    {
                        return Convert.ToBoolean(value);
                    }
                    catch
                    {
                        return defaultValue;
                    }
                }

        public static bool SendRoomMessage(
    string text)
        {
            if (!Connected ||
                session == null ||
                string.IsNullOrWhiteSpace(text))
            {
                return false;
            }

            try
            {
                session.Socket.SendPacket(
                    new SayPacket
                    {
                        Text = text
                    }
                );

                Plugin.LogSource.LogInfo(
                    $"[AP CHAT] Sent room message: {text}"
                );

                return true;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP CHAT] Failed sending room message: {ex}"
                );

                return false;
            }
        }
        private static HashSet<string> GetSlotDataStringSet(
    Dictionary<string, object> slotData,
    string key,
    params string[] defaultValues)
        {
            HashSet<string> result =
                new(StringComparer.OrdinalIgnoreCase);

            if (!slotData.TryGetValue(
                    key,
                    out object? value) ||
                value == null)
            {
                result.UnionWith(defaultValues);
                return result;
            }

            if (value is IEnumerable enumerable &&
                value is not string)
            {
                foreach (object? entry in enumerable)
                {
                    if (entry == null)
                        continue;

                    string? text = entry.ToString();

                    if (!string.IsNullOrWhiteSpace(text))
                    {
                        result.Add(
                            text.Trim()
                        );
                    }
                }
            }

            if (result.Count == 0)
            {
                result.UnionWith(defaultValues);
            }

            return result;
        }

        private static void ResetReceivedItemStateForConnection()
        {
            lock (itemSyncLock)
            {
                receivedEventIndex = 0;
                receivedItemStateReady = false;

                preStateReceivedItems.Clear();

                /*
                 * Do not let queued items from an old connection/session leak
                 * into the new one.
                 */
                while (pendingItems.TryDequeue(out _))
                {
                }
            }
        }


        private static void ClassifyReceivedItem(
            int index,
            APItemInfo item)
        {
            if (index < ArchipelagoState.ProcessedItemCount)
            {
                Plugin.LogSource.LogInfo(
                    $"[AP] Restoring previously processed " +
                    $"item #{index}: {item.ItemName}"
                );

                RandomizedItemData? data =
                    ItemData.ByItemId(item.ItemId);

                if (data != null && data.CreatesLocation)
                {
                    ItemRandomizer.RestoreUnlockedItem(
                        data.Guid
                    );
                }

                return;
            }

            pendingItems.Enqueue(
                new PendingArchipelagoItem(
                    index,
                    item
                )
            );

            Plugin.LogSource.LogInfo(
                $"[AP] Queued new item #{index}: " +
                $"{item.ItemName} ({item.ItemId})"
            );
        }


        private static void FinishReceivedItemStateInitialization()
        {
            lock (itemSyncLock)
            {
                int bufferedCount =
                    preStateReceivedItems.Count;

                Plugin.LogSource.LogInfo(
                    $"[AP STATE] Classifying {bufferedCount} " +
                    $"item(s) received before AP state initialization. " +
                    $"ProcessedItemCount=" +
                    $"{ArchipelagoState.ProcessedItemCount}"
                );

                while (preStateReceivedItems.Count > 0)
                {
                    PendingArchipelagoItem pending =
                        preStateReceivedItems.Dequeue();

                    ClassifyReceivedItem(
                        pending.Index,
                        pending.Item
                    );
                }

                /*
                 * Set this while still holding itemSyncLock.
                 *
                 * Any ItemReceived callback waiting on the lock will therefore
                 * see the initialized ProcessedItemCount and classify normally.
                 */
                receivedItemStateReady = true;

                Plugin.LogSource.LogInfo(
                    "[AP STATE] Received-item history initialization complete."
                );
            }
        }

        private static void OnItemReceived(
    ReceivedItemsHelper helper)
        {
            try
            {
                lock (itemSyncLock)
                {
                    APItemInfo item =
                        helper.DequeueItem();

                    int index =
                        receivedEventIndex++;

                    /*
                     * TryConnectAndLogin can replay received-item history before
                     * ArchipelagoState.Initialize() has loaded ProcessedItemCount.
                     *
                     * Do not classify those callbacks yet.
                     */
                    if (!receivedItemStateReady)
                    {
                        preStateReceivedItems.Enqueue(
                            new PendingArchipelagoItem(
                                index,
                                item
                            )
                        );

                        Plugin.LogSource.LogInfo(
                            $"[AP] Buffered pre-state item #{index}: " +
                            $"{item.ItemName} ({item.ItemId})"
                        );

                        return;
                    }

                    ClassifyReceivedItem(
                        index,
                        item
                    );
                }
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP] Item receive error: {ex}"
                );
            }
        }



        private static void OnSocketClosed(string reason)
        {
            Connected = false;

            Plugin.LogSource.LogWarning(
                $"[AP] Disconnected: {reason}"
            );
        }

        public static bool TryDequeueItem(
            out PendingArchipelagoItem? item)
        {
            return pendingItems.TryDequeue(out item);
        }

        public static bool SendGoalCompletion()
        {
            if (session == null || !Connected)
            {
                Plugin.LogSource.LogWarning(
                    "[AP GOAL] Cannot send goal completion: " +
                    "not connected."
                );

                return false;
            }

            try
            {
                Plugin.LogSource.LogInfo(
                    "[AP GOAL] Sending goal completion."
                );

                session.SetGoalAchieved();

                return true;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP GOAL] Failed to send goal " +
                    $"completion: {ex}"
                );

                return false;
            }
        }



        public static bool SendLocationCheck(long locationId)
        {
            if (session == null || !Connected)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP] Cannot send location check " +
                    $"{locationId}: not connected."
                );

                return false;
            }

            try
            {
                Plugin.LogSource.LogInfo(
                    $"[AP] Sending location check: " +
                    $"{locationId}"
                );

                session.Locations.CompleteLocationChecks(
                    locationId
                );

                // Mark synchronously so local presentation and goal evaluation
                // immediately see the new checked state.
                checkedLocations[locationId] = 0;

                // A newly completed location may satisfy one of our configured
                // completion goals.
                GoalManager.EvaluateCompletion();

                return true;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP] Failed to send location check " +
                    $"{locationId}: {ex}"
                );

                return false;
            }
        }

        public static bool ConnectSync(
    string address,
    string slotName,
    string gameName,
    string password = "")
        {
            try
            {
                Connected = false;
                LastConnectionError = "";

                ResetReceivedItemStateForConnection();

                var jsonAssembly =
                    typeof(Newtonsoft.Json.JsonConvert).Assembly;

                Plugin.LogSource.LogInfo(
                    $"[JSON DEBUG] Assembly = {jsonAssembly.FullName}"
                );

                Plugin.LogSource.LogInfo(
                    $"[JSON DEBUG] Location = {jsonAssembly.Location}"
                );

                var serializeObjectMethod =
                    typeof(Newtonsoft.Json.JsonConvert).GetMethod(
                        "SerializeObject",
                        new[] { typeof(object) }
                    );

                Plugin.LogSource.LogInfo(
                    $"[JSON DEBUG] SerializeObject(object) exists = " +
                    $"{serializeObjectMethod != null}"
                );


                // Allow either:
                // localhost:38281
                // 127.0.0.1:38281
                // archipelago.gg:12345
                // ws://...
                // wss://...
                string uriString = address.Trim();

                if (!uriString.StartsWith(
                        "ws://",
                        StringComparison.OrdinalIgnoreCase) &&
                    !uriString.StartsWith(
                        "wss://",
                        StringComparison.OrdinalIgnoreCase))
                {
                    // The official Archipelago webhost uses secure WebSockets.
                    // Local/self-hosted test servers normally use ordinary WebSockets.
                    if (uriString.StartsWith(
                            "archipelago.gg:",
                            StringComparison.OrdinalIgnoreCase) ||
                        string.Equals(
                            uriString,
                            "archipelago.gg",
                            StringComparison.OrdinalIgnoreCase))
                    {
                        uriString = "wss://" + uriString;
                    }
                    else
                    {
                        uriString = "ws://" + uriString;
                    }
                }

                Plugin.LogSource.LogInfo(
                    $"[AP] Creating session for {uriString}..."
                );

                session = ArchipelagoSessionFactory.CreateSession(
                    new Uri(uriString)
                );

                session.Socket.SocketOpened += () =>
                {
                    Plugin.LogSource.LogInfo(
                        "[AP SOCKET] Opened."
                    );
                };

                session.Socket.SocketClosed += reason =>
                {
                    Connected = false;

                    Plugin.LogSource.LogWarning(
                        $"[AP SOCKET] Closed: {reason}"
                    );
                };

                session.Socket.ErrorReceived += (e, message) =>
                {
                    Plugin.LogSource.LogError(
                        $"[AP SOCKET] Error: {message}"
                    );

                    Plugin.LogSource.LogError(e);
                };

                session.Items.ItemReceived += OnItemReceived;

                Plugin.LogSource.LogInfo(
                    $"[AP] Session URI = {session.Socket.Uri}"
                );

                Plugin.LogSource.LogInfo(
                    "[AP] Calling TryConnectAndLogin..."
                );

                LoginResult result =
                    session.TryConnectAndLogin(
                        gameName,
                        slotName,
                        ItemsHandlingFlags.AllItems,
                        password: string.IsNullOrEmpty(password)
                            ? null
                            : password
                    );

                if (!result.Successful)
                {
                    Connected = false;

                    LoginFailure failure = (LoginFailure)result;

                    foreach (string error in failure.Errors)
                    {
                        Plugin.LogSource.LogWarning(
                            $"[AP] Login error: {error}"
                        );
                    }

                    string combinedErrors =
                        string.Join(" ", failure.Errors);

                    if (combinedErrors.IndexOf(
                            "password",
                            StringComparison.OrdinalIgnoreCase) >= 0)
                    {
                        LastConnectionError = "Invalid password";
                    }
                    else if (
                        combinedErrors.IndexOf(
                            "slot",
                            StringComparison.OrdinalIgnoreCase) >= 0 ||
                        combinedErrors.IndexOf(
                            "name",
                            StringComparison.OrdinalIgnoreCase) >= 0)
                    {
                        LastConnectionError = "Invalid slot name";
                    }
                    else
                    {
                        LastConnectionError = "Login failed";
                    }

                    Plugin.LogSource.LogWarning(
                        $"[AP] LOGIN FAILED. " +
                        $"Slot={slotName}, Game={gameName}"
                    );

                    try
                    {
                        if (session.Socket.Connected)
                        {
                            session.Socket
                                .DisconnectAsync()
                                .GetAwaiter()
                                .GetResult();
                        }
                    }
                    catch (Exception ex)
                    {
                        Plugin.LogSource.LogWarning(
                            $"[AP] Error cleaning up failed connection: {ex}"
                        );
                    }

                    session = null;
                    return false;
                }

                LoginSuccessful login = (LoginSuccessful)result;

                string seed = session.RoomState.Seed;

                Plugin.LogSource.LogInfo(
                    $"[AP] Connected seed: {seed}"
                );

                ChallengeStart = GetSlotDataBool(
                    login.SlotData,
                    "challenge_start",
                    false
                );

                                Loresanity = GetSlotDataBool(
                                    login.SlotData,
                                    "loresanity",
                                    true
                                );

                                Monstersanity = GetSlotDataBool(
                                    login.SlotData,
                                    "monstersanity",
                                    true
                                );


                DeathLinkEnabled = GetSlotDataBool(
                    login.SlotData,
                    "death_link",
                    false
                );

                //DeathLinkManager.Enabled = DeathLinkEnabled;

                completionGoals.Clear();

                completionGoals.UnionWith(
                    GetSlotDataStringSet(
                        login.SlotData,
                        "completion_goals",
                        "Priscilla Mostyn"
                    )
                );


                Plugin.LogSource.LogInfo(
                    $"[AP] Slot options: " +
                    $"ChallengeStart={ChallengeStart}, " +
                    $"Loresanity={Loresanity}, " +
                    $"Monstersanity={Monstersanity}, " +
                    $"DeathLink={DeathLinkEnabled}, " +
                    $"CompletionGoals=[" +
                    $"{string.Join(", ", completionGoals)}]"
                );

                ArchipelagoState.Initialize(
    seed,
    slotName
);

                Connected = true;

                /*
                 * RestoreCheckedLocations currently clears both CheckedItems and
                 * UnlockedItems before reconstructing checked-location state.
                 *
                 * Therefore this MUST happen before we classify the buffered AP item
                 * history. Otherwise it would erase the UnlockedItems we just restored.
                 */
                RestoreCheckedLocations();

                /*
                 * We now know:
                 *
                 *   1. ProcessedItemCount has been loaded for this seed/slot.
                 *   2. CheckedItems has been rebuilt from the AP server.
                 *   3. UnlockedItems has been cleared and is ready to be rebuilt.
                 *
                 * It is now safe to classify every ItemReceived callback that arrived
                 * during TryConnectAndLogin.
                 */
                FinishReceivedItemStateInitialization();

                InitializeDeathLink();

                Plugin.LogSource.LogInfo(
                    $"[AP] LOGIN SUCCESS. " +
                    $"Slot={slotName}, Game={gameName}"
                );

                // Cache information about what each location contains.
                ScoutWitheringRoomsLocations();

                /*
                 * If the player completed all required goals while
                 * disconnected, or the previous victory packet was lost,
                 * re-evaluate persisted goal state now that the AP
                 * connection is available again.
                 */
                GoalManager.EvaluateCompletion();

                return true;
            }
            catch (Exception ex)
            {
                Connected = false;
                LastConnectionError = "Invalid host";

                Plugin.LogSource.LogError(
                    $"[AP] Connection exception: {ex}"
                );

                session = null;
                return false;
            }
        }

        private static readonly ConcurrentDictionary<long, ScoutedItemInfo>
            scoutedLocations = new();

        private static readonly ConcurrentDictionary<long, byte>
            checkedLocations = new();


        public static bool IsLocationChecked(long locationId)
        {
            return checkedLocations.ContainsKey(locationId);
        }

        private static void InitializeDeathLink()
        {
            if (session == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot initialize: session is null."
                );
                return;
            }

            try
            {
                // Clean up any service left over from a previous connection.
                if (deathLinkService != null)
                {
                    try
                    {
                        deathLinkService.OnDeathLinkReceived -=
                            OnDeathLinkReceived;

                        deathLinkService.DisableDeathLink();
                    }
                    catch (Exception ex)
                    {
                        Plugin.LogSource.LogDebug(
                            "[AP DEATHLINK] Exception while cleaning up old service: " +
                            ex.Message
                        );
                    }

                    deathLinkService = null;
                }

                if (!DeathLinkEnabled)
                {
                    Plugin.LogSource.LogInfo(
                        "[AP DEATHLINK] Disabled for this slot."
                    );

                    return;
                }

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Creating MultiClient DeathLink service..."
                );

                deathLinkService =
                    session.CreateDeathLinkService();

                deathLinkService.OnDeathLinkReceived +=
                    OnDeathLinkReceived;

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Calling EnableDeathLink()..."
                );

                deathLinkService.EnableDeathLink();

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] MultiClient DeathLink service enabled."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP DEATHLINK] Failed to initialize: {ex}"
                );

                deathLinkService = null;
            }
        }

        private static void OnDeathLinkReceived(DeathLink deathLink)
        {
            if (!DeathLinkEnabled)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Received DeathLink while feature disabled; ignoring."
                );
                return;
            }

            Plugin.LogSource.LogWarning(
                $"[AP DEATHLINK] RECEIVED DeathLink. " +
                $"Source={deathLink.Source}, " +
                $"Cause={deathLink.Cause}"
            );

            DeathLinkManager.QueueRemoteDeath(
                deathLink.Source,
                deathLink.Cause ?? ""
            );
        }

        public static bool SendDeathLink(string cause)
        {
            if (!Connected)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot send: Archipelago is not connected."
                );
                return false;
            }

            if (!DeathLinkEnabled)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot send: DeathLink slot option is disabled."
                );
                return false;
            }

            if (session == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot send: session is null."
                );
                return false;
            }

            if (deathLinkService == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot send: DeathLink service is null."
                );
                return false;
            }

            try
            {
                string source =
                    session.Players.ActivePlayer.Alias;

                Plugin.LogSource.LogInfo(
                    $"[AP DEATHLINK] Preparing outgoing DeathLink. " +
                    $"Source={source}, Cause={cause}"
                );

                DeathLink deathLink =
                    new DeathLink(
                        source,
                        cause
                    );

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Calling MultiClient SendDeathLink()..."
                );

                deathLinkService.SendDeathLink(
                    deathLink
                );

                Plugin.LogSource.LogWarning(
                    $"[AP DEATHLINK] MultiClient SendDeathLink() returned normally. " +
                    $"Cause={cause}"
                );

                /*
 * DeathLink itself is a Bounce feature and does not necessarily
 * generate a visible chat line in AP Text Clients.
 *
 * Send a normal Say packet as a human-readable companion message.
 * Failure to send this cosmetic chat line does NOT mean the
 * DeathLink itself failed.
 */
                SendRoomMessage(
                    $"[DeathLink] {source} died in the dream. Sending DeathLink..."
                );

                return true;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP DEATHLINK] Failed to send: {ex}"
                );

                return false;
            }
        }

        public static void MarkLocationChecked(long locationId)
        {
            checkedLocations[locationId] = 0;
        }

        public static bool TryGetScoutedLocation(
            long locationId,
            out ScoutedItemInfo? info)
        {
            if (scoutedLocations.TryGetValue(
                    locationId,
                    out ScoutedItemInfo? found))
            {
                info = found;
                return true;
            }

            info = null;
            return false;
        }


        public static async System.Threading.Tasks.Task DisconnectAsync()
        {
            try
            {
                if (session != null)
                {
                    Plugin.LogSource.LogInfo(
                        "[AP] Disconnecting existing session..."
                    );

                    await session.Socket.DisconnectAsync();

                                        Plugin.LogSource.LogInfo(
                        "[AP] Session disconnected."
                    );
                }
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP] Exception while disconnecting: {ex}"
                );
            }
            finally
            {

                if (deathLinkService != null)
                {
                    try
                    {
                        deathLinkService.OnDeathLinkReceived -=
                            OnDeathLinkReceived;

                        deathLinkService.DisableDeathLink();
                    }
                    catch (Exception ex)
                    {
                        Plugin.LogSource.LogDebug(
                            "[AP DEATHLINK] Exception while shutting down service: " +
                            ex.Message
                        );
                    }

                    deathLinkService = null;
                }

                DeathLinkManager.Reset();

                Connected = false;
                session = null;
            }
        }



        public static void RestoreCheckedLocations()
        {
            if (session == null || !Connected)
            {
                Plugin.LogSource.LogWarning(
                    "[AP STATE] Cannot restore checked locations: not connected."
                );

                return;
            }

            ItemRandomizer.ClearCheckedItems();
            ItemRandomizer.ClearUnlockedItems();


            try
            {

                int restored = 0;
                checkedLocations.Clear();

                foreach (long locationId in session.Locations.AllLocationsChecked)
                {
                    checkedLocations[locationId] = 0;

                    RandomizedItemData? data =
                        ItemData.ByLocationId(locationId);

                    if (data != null)
                    {
                        if (!ItemData.IsMultiDiscoveryItem(data))
                        {
                            ItemRandomizer.RestoreCheckedItem(
                                data.Guid
                            );
                        }

                        Plugin.LogSource.LogInfo(
                            $"[AP STATE] Restored checked item location: " +
                            $"{data.LocationName} ({locationId})"
                        );

                        restored++;
                    }
                }

                Plugin.LogSource.LogInfo(
                    $"[AP STATE] Restored {restored} checked location(s) " +
                    $"from the Archipelago server."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP STATE] Failed to restore checked locations: {ex}"
                );
            }
        }


        public static void ScoutWitheringRoomsLocations()
        {
            if (session == null || !Connected)
            {
                Plugin.LogSource.LogWarning(
                    "[AP SCOUT] Cannot scout locations: not connected."
                );

                return;
            }

            try
            {
                var locationData = ItemData.RandomizedItems();

                var ids = new System.Collections.Generic.List<long>();

                // ---------------------------------------------------------
                // Normal randomized-item discovery locations
                // ---------------------------------------------------------
                foreach (RandomizedItemData data in locationData)
                {
                    if (data.CreatesLocation &&
                        data.LocationId.HasValue)
                    {
                        ids.Add(data.LocationId.Value);
                    }
                }

                // ---------------------------------------------------------
                // Additional multi-discovery item locations
                // ---------------------------------------------------------
                //
                // The ordinary first location is already included above
                // through data.LocationId.
                //
                // Only add ordinal locations 2+ here.
                //
                foreach (RandomizedItemData data in ItemData.All())
                {
                    if (!ItemData.IsMultiDiscoveryItem(data))
                        continue;

                    var multiLocations =
                        ItemData.GetMultiDiscoveryLocations(data);

                    foreach (MultiDiscoveryLocationData location
                             in multiLocations)
                    {
                        // Ordinal 1 is the item's ordinary LocationId and
                        // was already added by the normal loop above.
                        if (location.Ordinal <= 1)
                            continue;

                        ids.Add(location.LocationId);

                        Plugin.LogSource.LogInfo(
                            $"[AP SCOUT] Added multi-discovery location: " +
                            $"{location.LocationName} " +
                            $"({location.LocationId})"
                        );
                    }
                }

                // ---------------------------------------------------------
                // Remembrance Shrine locations
                // ---------------------------------------------------------

                foreach (
                    RemembranceShrineLocationData shrine
                    in RemembranceShrineData.All())
                {
                    ids.Add(shrine.LocationId);
                }

                // ---------------------------------------------------------
                // Loresanity locations
                // ---------------------------------------------------------

                if (Loresanity)
                {
                    foreach (LoreLocationData lore in LoreData.All())
                    {
                        ids.Add(lore.LocationId);
                    }
                }
                if (Monstersanity)
                {
                    foreach (MonsterLocationData monster in MonsterData.All())
                    {
                        ids.Add(monster.LocationId);
                    }
                }

                if (ids.Count == 0)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP SCOUT] No Withering Rooms locations found."
                    );

                    return;
                }

                Plugin.LogSource.LogInfo(
                    $"[AP SCOUT] Scouting {ids.Count} locations..."
                );

                var results =
                    session.Locations
                        .ScoutLocationsAsync(ids.ToArray())
                        .GetAwaiter()
                        .GetResult();

                scoutedLocations.Clear();

                foreach (var pair in results)
                {
                    scoutedLocations[pair.Key] = pair.Value;

                    Plugin.LogSource.LogInfo(
                        $"[AP SCOUT] {pair.Value.LocationName} -> " +
                        $"{pair.Value.ItemName} / " +
                        $"Player={pair.Value.Player}"
                    );
                }

                Plugin.LogSource.LogInfo(
                    $"[AP SCOUT] Cached {scoutedLocations.Count} locations."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP SCOUT] Failed scouting locations: {ex}"
                );
            }
        }


        public static bool TryGetCheckInfo(
    long locationId,
    out long itemId,
    out string itemName,
    out string playerName)
        {
            itemId = 0;
            itemName = "";
            playerName = "";

            if (!TryGetScoutedLocation(
                    locationId,
                    out ScoutedItemInfo? info) ||
                info == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP SCOUT] No cached scout data for {locationId}."
                );

                return false;
            }

            itemId = info.ItemId;
            itemName = info.ItemName;
            playerName = info.Player.ToString();

            return true;
        }

    }
    
}