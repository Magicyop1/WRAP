using System;
using System.Collections.Generic;
using UnityEngine;

namespace WitheringRoomsArchipelago
{
    public sealed class MerchantAPDisplay
    {
        public Item VanillaItem = null!;

        public long LocationId;
        public long APItemId;

        public string APItemName = "";
        public string PlayerName = "";
        public string LocationName = "";

        // Non-null when the scouted AP item is itself a
        // Withering Rooms item that we can resolve locally.
        public Item? LocalDisplayItem = null;

        public bool UsesAPLogo =>
            LocalDisplayItem == null;
    }


    public static class MerchantPresentation
    {
        // We only enable ItemBox presentation substitution while
        // CraftingUIController is actively building/displaying a store.
        //
        // This prevents ordinary inventory ItemBoxUIControllers from
        // being affected.
        private static bool merchantUIActive = false;



        public static bool MerchantUIActive =>
            merchantUIActive;


        public static bool IsMerchantItemInfo(
    ItemInfo? itemInfo)
        {
            if (!MerchantUIActive ||
                itemInfo == null)
            {
                return false;
            }

            return itemInfo
                is CraftingUIController.CraftingItemInfo;
        }


        // Cache native Withering Rooms icon textures by GUID.
        private static readonly Dictionary<string, Texture2D>
            localIconCache = new();


        private static readonly HashSet<string> activeMerchantItemGuids =
    new HashSet<string>();

        public static void ClearActiveMerchantItems()
        {
            activeMerchantItemGuids.Clear();
        }

        public static void RegisterActiveMerchantItem(Item? item)
        {
            if (item == null)
                return;

            string guid = item.GetGUID();

            if (!string.IsNullOrEmpty(guid))
                activeMerchantItemGuids.Add(guid);
        }

        public static void RegisterActiveMerchantItemGuid(string? guid)
        {
            if (!string.IsNullOrEmpty(guid))
                activeMerchantItemGuids.Add(guid);
        }

        public static bool IsActiveMerchantItem(Item? item)
        {
            if (!MerchantUIActive || item == null)
                return false;

            string guid = item.GetGUID();

            return !string.IsNullOrEmpty(guid) &&
                   activeMerchantItemGuids.Contains(guid);
        }


        public static bool IsActiveMerchantItem(ItemInfo? itemInfo)
        {
            if (itemInfo == null ||
                itemInfo.item == null)
            {
                return false;
            }

            return IsActiveMerchantItem(itemInfo.item);
        }


        public static void BeginMerchantUI()
        {
            activeMerchantItemGuids.Clear();

            selectedMerchantResult = null;
            selectedMerchantDisplay = null;
            waitingForResultIngredient = false;
            MerchantSelectedItemPresentation.Pending = null;

            merchantUIActive = true;

            Plugin.LogSource.LogInfo(
                "[AP SHOP UI] Merchant presentation enabled."
            );
        }

        public static void EndMerchantPresentation()
        {
            Plugin.LogSource.LogWarning(
                $"[AP SHOP UI] EndMerchantPresentation ENTER: " +
                $"active={merchantUIActive}, " +
                $"merchantGuids={activeMerchantItemGuids.Count}, " +
                $"selectedResult={(selectedMerchantResult != null)}, " +
                $"selectedDisplay={(selectedMerchantDisplay != null)}, " +
                $"waiting={waitingForResultIngredient}, " +
                $"pending={(MerchantSelectedItemPresentation.Pending != null)}"
            );

            merchantUIActive = false;

            activeMerchantItemGuids.Clear();

            selectedMerchantResult = null;
            selectedMerchantDisplay = null;
            waitingForResultIngredient = false;

            MerchantSelectedItemPresentation.Pending = null;

            Plugin.LogSource.LogWarning(
                $"[AP SHOP UI] EndMerchantPresentation EXIT: " +
                $"active={merchantUIActive}, " +
                $"merchantGuids={activeMerchantItemGuids.Count}"
            );
        }


        public static void EndMerchantUI()
        {
            merchantUIActive = false;
            activeMerchantItemGuids.Clear();

            Plugin.LogSource.LogInfo(
                "[AP SHOP UI] Merchant presentation disabled."
            );
        }


        // -------------------------------------------------------------
        // CORE LOOKUP
        // -------------------------------------------------------------

        public static bool TryGetDisplay(
            Item? vanillaItem,
            out MerchantAPDisplay? display)
        {
            display = null;

            if (!merchantUIActive)
                return false;

            if (!ArchipelagoClient.Connected)
                return false;

            if (vanillaItem == null)
                return false;

            string guid = vanillaItem.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return false;

            RandomizedItemData? locationData =
                ItemData.ByGuid(guid);

            if (locationData == null ||
                !locationData.CreatesLocation ||
                !locationData.LocationId.HasValue)
            {
                return false;
            }

            long locationId =
                locationData.LocationId.Value;

            if (!ArchipelagoClient.TryGetCheckInfo(
                    locationId,
                    out long apItemId,
                    out string apItemName,
                    out string playerName))
            {
                return false;
            }

            Item? localDisplayItem = null;

            // If the AP item ID belongs to our own game's ItemData,
            // resolve the actual Withering Rooms Item so that we can
            // use its native icon and native detail presentation.
            RandomizedItemData? replacementData =
                ItemData.ByItemId(apItemId);

            if (replacementData != null)
            {
                localDisplayItem =
                    GameItems.FindItemByGuid(
                        replacementData.Guid
                    );
            }

            display = new MerchantAPDisplay
            {
                VanillaItem = vanillaItem,

                LocationId = locationId,
                APItemId = apItemId,

                APItemName =
                    string.IsNullOrWhiteSpace(apItemName)
                        ? "Archipelago Item"
                        : apItemName,

                PlayerName =
                    playerName ?? "",

                LocationName =
                    locationData.LocationName
                    ?? locationData.Name,

                LocalDisplayItem =
                    localDisplayItem
            };

            return true;
        }


        public static bool TryGetDisplay(
            ItemInfo? itemInfo,
            out MerchantAPDisplay? display)
        {
            display = null;

            if (itemInfo == null ||
                itemInfo.item == null)
            {
                return false;
            }

            return TryGetDisplay(
                itemInfo.item,
                out display
            );
        }


        // -------------------------------------------------------------
        // TEXT
        // -------------------------------------------------------------

        public static string GetDisplayName(
            MerchantAPDisplay display)
        {
            return display.APItemName;
        }


        public static string GetRecipientText(
            MerchantAPDisplay display)
        {
            if (string.IsNullOrWhiteSpace(
                    display.PlayerName))
            {
                return "Archipelago Item";
            }

            return
                $"For {display.PlayerName}";
        }


        // -------------------------------------------------------------
        // ICON
        // -------------------------------------------------------------

        public static Texture2D? GetDisplayTexture(
            MerchantAPDisplay display)
        {
            // Foreign / unresolved AP item:
            // use the Archipelago logo.
            if (display.LocalDisplayItem == null)
            {
                return
                    ArchipelagoNotifications
                        .GetLogoTexture();
            }

            Item localItem =
                display.LocalDisplayItem;

            string guid =
                localItem.GetGUID();

            if (!string.IsNullOrEmpty(guid) &&
                localIconCache.TryGetValue(
                    guid,
                    out Texture2D cached) &&
                cached != null)
            {
                return cached;
            }

            try
            {
                var iconRef =
                    localItem.icon;

                if (!iconRef.Valid())
                {
                    Plugin.LogSource.LogWarning(
                        $"[AP SHOP UI] Native icon reference " +
                        $"was invalid for " +
                        $"{display.APItemName}."
                    );

                    return
                        ArchipelagoNotifications
                            .GetLogoTexture();
                }

                Texture2D? texture =
                    iconRef.LoadSync<Texture2D>(true);

                if (texture == null)
                {
                    Plugin.LogSource.LogWarning(
                        $"[AP SHOP UI] Could not load native " +
                        $"icon for {display.APItemName}."
                    );

                    return
                        ArchipelagoNotifications
                            .GetLogoTexture();
                }

                if (!string.IsNullOrEmpty(guid))
                {
                    localIconCache[guid] =
                        texture;
                }

                return texture;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP SHOP UI] Error loading icon for " +
                    $"{display.APItemName}: {ex}"
                );

                return
                    ArchipelagoNotifications
                        .GetLogoTexture();
            }
        }


        // -------------------------------------------------------------
        // LOGGING
        // -------------------------------------------------------------

        public static void LogDisplay(
    MerchantAPDisplay display,
    string context)
        {
            string iconType =
                display.LocalDisplayItem != null
                    ? "native"
                    : "AP";

            Plugin.LogSource.LogInfo(
                $"[AP SHOP UI] {context}: " +
                $"{display.VanillaItem.GetTitle()} -> " +
                $"{display.APItemName} / " +
                $"{display.PlayerName} / " +
                $"location={display.LocationName} / " +
                $"icon={iconType}"
            );
        }

        private static Item? selectedMerchantResult = null;
        private static MerchantAPDisplay? selectedMerchantDisplay = null;
        private static bool waitingForResultIngredient = false;

        public static void BeginSelectedMerchantPresentation(
            Item item,
            MerchantAPDisplay display)
        {
            selectedMerchantResult = item;
            selectedMerchantDisplay = display;
            waitingForResultIngredient = true;
        }

        public static bool TryConsumeResultIngredient(
            Item item,
            out MerchantAPDisplay? display)
        {
            display = null;

            if (!MerchantUIActive ||
                !waitingForResultIngredient ||
                selectedMerchantResult == null ||
                selectedMerchantDisplay == null ||
                item == null)
            {
                return false;
            }

            // This identity check is important: it prevents us from
            // touching the Strange Coin / other cost rows.
            if (item.GetGUID() != selectedMerchantResult.GetGUID())
                return false;

            waitingForResultIngredient = false;
            display = selectedMerchantDisplay;
            return true;
        }
    }
}