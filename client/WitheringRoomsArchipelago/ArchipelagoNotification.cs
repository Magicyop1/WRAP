using System;
using System.IO;
using UnityEngine;
using WitheringRoomsArchipelago;



public class ArchipelagoNotification
{
    public string ItemName = "";
    public string PlayerName = "";
    public string LocationName = "";
}

public static class ArchipelagoNotifications
{
    public static ArchipelagoNotification? Pending = null;

    public static Texture2D? LogoTexture = null;


    public static UnityEngine.UI.RawImage? WatchedIcon = null;
    public static int WatchIconFrames = 0;

    public static int PendingIconDelayFrames = 0;

    private static bool _reportedMissingLogo = false;

    private static Item? _pendingAPIconItem = null;

    public static bool ShouldReplaceIcon(Item? item)
    {
        if (item == null || _pendingAPIconItem == null)
            return false;

        return item.Pointer == _pendingAPIconItem.Pointer;
    }

    public static void Update()
    {

        if (LogoTexture == null)
        {
            if (!_reportedMissingLogo)
            {
                _reportedMissingLogo = true;

                Plugin.LogSource.LogWarning(
                    "[AP NOTIFY] LogoTexture has become NULL."
                );
            }
        }
        else
        {
            _reportedMissingLogo = false;
        }
        /*
        if (_queuedCheck != null)
        {
            if (_queuedCheckDelayFrames > 0)
            {
                _queuedCheckDelayFrames--;
            }
            else
            {
                QueuedCheckNotification request = _queuedCheck;
                _queuedCheck = null;

                Plugin.LogSource.LogInfo(
                    $"[AP NOTIFY] Displaying deferred notification: " +
                    $"{request.ItemName} ({request.PlayerName}) / " +
                    $"{request.LocationName}"
                );

                ShowCheckSent(
                    request.OriginalItem,
                    request.ItemName,
                    request.PlayerName,
                    request.LocationName
                );
            }
        }
        */

        

        Texture2D? logo = GetLogoTexture();
    }

    public static bool TryConsumeAPIcon(Item? item)
    {
        if (item == null || _pendingAPIconItem == null)
            return false;

        if (item.Pointer != _pendingAPIconItem.Pointer)
            return false;

        _pendingAPIconItem = null;
        return true;
    }

    public static void LoadLogo()
    {
        if (LogoTexture != null)
            return;

        try
        {
            string logoPath = Path.Combine(
                BepInEx.Paths.PluginPath,
                "WitheringRoomsArchipelago",
                "archipelago.png"
            );

            Plugin.LogSource.LogInfo(
                $"[AP NOTIFY] Loading Archipelago logo from {logoPath}"
            );

            if (!File.Exists(logoPath))
            {
                Plugin.LogSource.LogWarning(
                    $"[AP NOTIFY] Archipelago logo not found: {logoPath}"
                );

                return;
            }

            byte[] imageData = File.ReadAllBytes(logoPath);

            Texture2D texture =
                new Texture2D(2, 2, TextureFormat.RGBA32, false);

            bool success =
                ImageConversion.LoadImage(
                    texture,
                    imageData
                );

            if (!success)
            {
                Plugin.LogSource.LogWarning(
                    "[AP NOTIFY] Failed to decode Archipelago logo PNG."
                );

                UnityEngine.Object.Destroy(texture);
                return;
            }

            texture.name = "ArchipelagoLogo";

            UnityEngine.Object.DontDestroyOnLoad(texture);

            LogoTexture = texture;

            Plugin.LogSource.LogInfo(
                $"[AP NOTIFY] Archipelago logo loaded successfully: " +
                $"{texture.width}x{texture.height}"
            );
        }
        catch (Exception ex)
        {
            Plugin.LogSource.LogError(
                $"[AP NOTIFY] Failed loading Archipelago logo: {ex}"
            );
        }
    }

    public class QueuedCheckNotification
    {
        public Item OriginalItem = null!;
        public Item? DisplayItem = null;
        public string ItemName = "";
        public string PlayerName = "";
        public string LocationName = "";
    }

    public static QueuedCheckNotification? QueuedCheck = null;

    public static void QueueCheckSent(
        Item originalItem,
        Item? displayItem,
        string apItemName,
        string receivingPlayer,
        string locationName)
    {

        QueuedCheck = new QueuedCheckNotification
        {
            OriginalItem = originalItem,
            DisplayItem = displayItem,
            ItemName = apItemName,
            PlayerName = receivingPlayer,
            LocationName = locationName
        };

        Plugin.LogSource.LogInfo(
            $"[AP NOTIFY] Queued check notification: " +
            $"{apItemName} ({receivingPlayer}) / {locationName}"
        );
    }

    public static void ShowCheckSent(
        Item originalItem,
        Item? displayItem,
        string apItemName,
        string receivingPlayer,
        string locationName)
    {
        Pending = new ArchipelagoNotification
        {
            ItemName = apItemName,
            PlayerName = receivingPlayer,
            LocationName = locationName
        };

        // Remember exactly which native Item is being used to construct
        // this AP notification.
        Item? itemForDisplay = displayItem;

        if (itemForDisplay != null)
        {
            // Native Withering Rooms AP reward:
            // show its real icon.
            _pendingAPIconItem = null;
        }
        else
        {
            // Foreign-game AP reward:
            // QuickItemUIDisplay needs a normal native Item to construct
            // the popup. Its icon will then be replaced with the AP logo.
            itemForDisplay = GetNotificationFallbackItem();

            _pendingAPIconItem = itemForDisplay;
        }

        if (itemForDisplay == null)
        {
            Plugin.LogSource.LogWarning(
                "[AP NOTIFY] Could not resolve notification display item."
            );

            Pending = null;
            _pendingAPIconItem = null;
            return;
        }

        QuickItemUIDisplay[] displays =
            UnityEngine.Object.FindObjectsOfType<QuickItemUIDisplay>(true);

        if (displays.Length == 0)
        {
            Plugin.LogSource.LogWarning(
                "[AP NOTIFY] No QuickItemUIDisplay found."
            );

            Pending = null;
            _pendingAPIconItem = null;
            return;
        }

        Plugin.LogSource.LogInfo(
            $"[AP NOTIFY] {apItemName} ({receivingPlayer}) / " +
            $"{locationName}"
        );

        displays[0].ShowItem(itemForDisplay, 1);
        displays[0].PlaySound();
    }

    public static Texture2D? GetLogoTexture()
    {
        if (LogoTexture != null)
            return LogoTexture;

        Plugin.LogSource.LogWarning(
            "[AP NOTIFY] LogoTexture was null; reloading Archipelago logo."
        );

        LoadLogo();

        return LogoTexture;
    }

    private static void DumpUIHierarchy(
    UnityEngine.Transform root,
    string indent = "")
    {
        if (root == null)
            return;

        GameObject go = root.gameObject;

        Plugin.LogSource.LogInfo(
            $"[AP UI TREE] {indent}{go.name} " +
            $"active={go.activeInHierarchy}"
        );

        // RawImage
        UnityEngine.UI.RawImage rawImage =
            go.GetComponent<UnityEngine.UI.RawImage>();

        if (rawImage != null)
        {
            Plugin.LogSource.LogInfo(
                $"[AP UI TREE] {indent}  RawImage: " +
                $"enabled={rawImage.enabled}, " +
                $"texture={rawImage.texture?.name ?? "NULL"}"
            );
        }

        // Standard Unity Image
        UnityEngine.UI.Image image =
            go.GetComponent<UnityEngine.UI.Image>();

        if (image != null)
        {
            Plugin.LogSource.LogInfo(
                $"[AP UI TREE] {indent}  Image: " +
                $"enabled={image.enabled}, " +
                $"sprite={image.sprite?.name ?? "NULL"}, " +
                $"texture={image.sprite?.texture?.name ?? "NULL"}"
            );
        }

        // TextMeshPro
        TMPro.TextMeshProUGUI tmp =
            go.GetComponent<TMPro.TextMeshProUGUI>();

        if (tmp != null)
        {
            Plugin.LogSource.LogInfo(
                $"[AP UI TREE] {indent}  TMP: \"{tmp.text}\""
            );
        }

        for (int i = 0; i < root.childCount; i++)
        {
            DumpUIHierarchy(
                root.GetChild(i),
                indent + "  "
            );
        }
    }

    private static Item? GetNotificationFallbackItem()
    {
        // Any ordinary native item with a known working UI icon is fine.
        // Knife is a convenient choice.

        return GameItems.FindItemByGuid("1d472eb78b3f71645b05f7f337331955");
    }
}