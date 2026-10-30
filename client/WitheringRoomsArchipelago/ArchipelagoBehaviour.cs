using BepInEx.Logging;
using Il2CppInterop.Runtime.Attributes;
using Il2CppSystem;
using System;
using UnityEngine;
using static ArchipelagoNotifications;
using APItemInfo = Archipelago.MultiClient.Net.Models.ItemInfo;

namespace WitheringRoomsArchipelago
{
    public class ArchipelagoBehaviour : MonoBehaviour
    {
        private bool inventoryReady = false;
        private float inventoryReadyTime = -1f;

        private const float APItemStartupDelay = 3.0f;

        private ArchipelagoUI? archipelagoUI;
        private PendingArchipelagoItem? deferredArchipelagoItem = null;

        private float deferredRetryTimer = 0f;

        private const float DeferredRetryInterval = 2.0f;

public ArchipelagoBehaviour(System.IntPtr ptr) : base(ptr)
        {
        }

        public void Start()
        {
            Plugin.LogSource.LogInfo(
                "ArchipelagoBehaviour started."
            );

            ArchipelagoNotifications.LoadLogo();

            archipelagoUI =
                new ArchipelagoUI();

            archipelagoUI.Start();

        }

        [HideFromIl2Cpp]
        private bool HandleArchipelagoItem(APItemInfo apItem)
        {
            Plugin.LogSource.LogInfo(
                $"[AP MAIN THREAD] Processing " +
                $"{apItem.ItemName} ({apItem.ItemId})"
            );

            RandomizedItemData? data =
                ItemData.ByItemId(apItem.ItemId);

            if (data == null)
            {
                Plugin.LogSource.LogError(
                    $"[AP] Unknown Withering Rooms item ID " +
                    $"{apItem.ItemId} ({apItem.ItemName})"
                );

                return false;
            }

            Plugin.LogSource.LogInfo(
                $"[AP RECEIVE] {apItem.ItemName} -> " +
                $"{data.Name} ({data.Guid})"
            );

            return ItemRandomizer.HandleReceivedArchipelagoItem(
                data,
                1
            );
        }

        public void Update()
        {
            if (!inventoryReady &&
    Inventory.instance != null &&
    Inventory.instance.Ready())
            {
                inventoryReady = true;
                inventoryReadyTime = Time.unscaledTime;

                Plugin.LogSource.LogInfo(
                    "Inventory is fully ready! " +
                    "Starting AP item-delivery grace period."
                );

                OnInventoryReady();
            }

            bool vanillaLoadSafe =
                inventoryReady &&
                VanillaLoadSafetyGate.CanMutateGameplayState();

            bool safeForAPGameplay =
                inventoryReady &&
                vanillaLoadSafe;

            bool safeForAPItemDelivery =
                safeForAPGameplay &&
                inventoryReadyTime >= 0f &&
                Time.unscaledTime - inventoryReadyTime >= APItemStartupDelay;

            archipelagoUI?.Update();
            ArchipelagoNotifications.Update();
            QuestAutoCompleteCompatibility.Update();

            if (safeForAPGameplay &&
                ArchipelagoClient.DeathLinkEnabled)
            {
                DeathLinkManager.Update();
            }



            if (inventoryReady &&
    ArchipelagoNotifications.QueuedCheck != null)
            {
                QueuedCheckNotification notification =
                    ArchipelagoNotifications.QueuedCheck;

                ArchipelagoNotifications.QueuedCheck = null;

                Plugin.LogSource.LogInfo(
                    $"[AP NOTIFY] Processing queued check from Update(): " +
                    $"{notification.ItemName} " +
                    $"({notification.PlayerName}) / " +
                    $"{notification.LocationName}"
                );

                Plugin.LogSource.LogInfo(
                    $"[AP NOTIFY] Update calling queued ShowCheckSent on frame " +
                    $"{Time.frameCount}"
                );

                ArchipelagoNotifications.ShowCheckSent(
                    notification.OriginalItem,
                    notification.DisplayItem,
                    notification.ItemName,
                    notification.PlayerName,
                    notification.LocationName
                );
            }

            if (safeForAPGameplay &&
                ArchipelagoClient.Connected)
            {
                TutorialBypass.TrySkipPreMargaretTutorial();
            }


            if (safeForAPItemDelivery &&
    ArchipelagoClient.Connected)
            {
                //TutorialBypass.TrySkipPreMargaretTutorial();
                // If a previous AP item could not be delivered because
                // its Withering Rooms Item object was unavailable,
                // periodically retry it.
                if (deferredArchipelagoItem != null)
                {
                    deferredRetryTimer += Time.deltaTime;

                    if (deferredRetryTimer >= DeferredRetryInterval)
                    {
                        deferredRetryTimer = 0f;

                        PendingArchipelagoItem pending =
                            deferredArchipelagoItem;

                        Plugin.LogSource.LogInfo(
                            $"[AP RETRY] Retrying item #{pending.Index}: " +
                            $"{pending.Item.ItemName}"
                        );

                        bool success =
                            HandleArchipelagoItem(
                                pending.Item
                            );

                        if (success)
                        {
                            ArchipelagoState.SetProcessedItemCount(
                                pending.Index + 1
                            );

                            Plugin.LogSource.LogInfo(
                                $"[AP STATE] Processed through item " +
                                $"#{pending.Index}"
                            );

                            deferredArchipelagoItem = null;
                        }
                    }
                }
                else
                {
                    // No unresolved item exists, so take the next AP item.
                    if (ArchipelagoClient.TryDequeueItem(
                        out PendingArchipelagoItem? pending))
                    {
                        if (pending != null)
                        {
                            // Archipelago sends us the complete received-item
                            // history when connecting. If this item was already
                            // processed in a previous session, restore its unlock
                            // state without physically granting it again.
                            if (pending.Index <
                                ArchipelagoState.ProcessedItemCount)
                            {
                                RandomizedItemData? data =
                                    ItemData.ByItemId(
                                        pending.Item.ItemId
                                    );

                                if (data != null)
                                {
                                    Plugin.LogSource.LogInfo(
                                        $"[AP STATE] Restoring previously processed " +
                                        $"item #{pending.Index}: {data.Name}"
                                    );

                                    if (data.CreatesLocation)
                                    {
                                        ItemRandomizer.RestoreUnlockedItem(
                                            data.Guid
                                        );
                                    }
                                }
                                else
                                {
                                    Plugin.LogSource.LogWarning(
                                        $"[AP STATE] Could not restore unknown " +
                                        $"AP item {pending.Item.ItemId} at " +
                                        $"index #{pending.Index}"
                                    );
                                }

                                // IMPORTANT:
                                // Do not call HandleArchipelagoItem().
                                // Do not advance ProcessedItemCount.
                                // This item was already processed previously.
                            }
                            else
                            {
                                // This is a genuinely new AP delivery.
                                bool success =
                                    HandleArchipelagoItem(
                                        pending.Item
                                    );

                                if (success)
                                {
                                    ArchipelagoState.SetProcessedItemCount(
                                        pending.Index + 1
                                    );

                                    Plugin.LogSource.LogInfo(
                                        $"[AP STATE] Processed through item " +
                                        $"#{pending.Index}"
                                    );
                                }
                                else
                                {
                                    // Do NOT advance ProcessedItemCount.
                                    // Hold this item and try it again later.
                                    deferredArchipelagoItem = pending;
                                    deferredRetryTimer = 0f;

                                    Plugin.LogSource.LogWarning(
                                        $"[AP DEFER] Could not deliver item " +
                                        $"#{pending.Index}: " +
                                        $"{pending.Item.ItemName}. " +
                                        $"Will retry when its game Item " +
                                        $"becomes available."
                                    );
                                }
                            }
                        }
                    }
                }
            }

            // An already-open local UI must remain responsive even if
            // Archipelago connection state changes.
            ChapterTravelUI.Update();

            if (ArchipelagoClient.Connected)
            {
                ChapterTravelManager.UpdateUnlockedChapters();
                ChapterTravelManager.UpdateTravelState();
            }

        }



        private void OnInventoryReady()
        {
            Plugin.LogSource.LogInfo(
                "Inventory reports ready. AP gameplay mutation remains " +
                "gated until vanilla inventory/mansion/player loading is stable."
            );

            //GameItems.LogLoadedItems();
        }

        public void OnGUI()
        {
            if (archipelagoUI != null)
            {
                archipelagoUI.OnGUI();
            }

            ChapterTravelUI.Draw();

            DeathLinkNoticeUI.OnGUI();
        }

    }

    public static class TutorialBypass
    {
        private const string CompletedPreMargaretGuid =
            "5e8790be1f4ec8645b086908672fd63b";

        private static bool attempted = false;

        public static void TrySkipPreMargaretTutorial()
        {
            if (attempted)
                return;

            if (!ArchipelagoClient.Connected)
                return;

            if (Inventory.instance == null ||
                !Inventory.instance.Ready())
            {
                return;
            }

            Item? token =
                GameItems.FindItemByGuid(
                    CompletedPreMargaretGuid
                );

            if (token == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP TUTORIAL] Could not resolve " +
                    "Tutorial_CompletedPreMargaret."
                );
                return;
            }

            // Do not add another copy if this save already has the token.
            ItemInfo? existing =
                Inventory.instance.GetInfo(token);

            if (existing != null && existing.quantity >= 1)
            {
                attempted = true;

                Plugin.LogSource.LogInfo(
                    "[AP TUTORIAL] Tutorial_CompletedPreMargaret " +
                    "is already present; no bypass token needed."
                );

                return;
            }

            attempted = true;

            Plugin.LogSource.LogInfo(
                "[AP TUTORIAL] Granting Tutorial_CompletedPreMargaret " +
                "to bypass the Chapter 1 combat tutorial."
            );

            ItemRandomizer.GiveInternalNewItem(token, 1);
        }
    }
}
