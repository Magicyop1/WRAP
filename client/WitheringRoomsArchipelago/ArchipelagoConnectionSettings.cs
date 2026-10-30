using System;
using System.IO;

namespace WitheringRoomsArchipelago
{
    public static class ArchipelagoConnectionSettings
    {
        private static string SettingsDirectory =>
            Path.Combine(
                BepInEx.Paths.ConfigPath,
                "WitheringRoomsArchipelago"
            );

        private static string SettingsFile =>
            Path.Combine(
                SettingsDirectory,
                "connection.txt"
            );

        public static bool TryLoad(
    out string address,
    out string slotName,
    out string password)
        {
            address = "";
            slotName = "";
            password = "";

            Plugin.LogSource.LogInfo(
                $"[AP SETTINGS] TryLoad called."
            );

            Plugin.LogSource.LogInfo(
                $"[AP SETTINGS] Settings path: {SettingsFile}"
            );

            try
            {
                bool exists = File.Exists(SettingsFile);

                Plugin.LogSource.LogInfo(
                    $"[AP SETTINGS] File exists={exists}"
                );

                if (!exists)
                    return false;

                string[] lines =
                    File.ReadAllLines(SettingsFile);

                Plugin.LogSource.LogInfo(
                    $"[AP SETTINGS] Read {lines.Length} line(s)."
                );

                if (lines.Length < 2)
                    return false;

                address = lines[0].Trim();
                slotName = lines[1].Trim();

                if (lines.Length >= 3)
                    password = lines[2];

                Plugin.LogSource.LogInfo(
                    $"[AP SETTINGS] Parsed address=\"{address}\", " +
                    $"slot=\"{slotName}\""
                );

                if (string.IsNullOrWhiteSpace(address) ||
                    string.IsNullOrWhiteSpace(slotName))
                {
                    Plugin.LogSource.LogWarning(
                        "[AP SETTINGS] Saved connection is incomplete."
                    );

                    return false;
                }

                Plugin.LogSource.LogInfo(
                    $"[AP SETTINGS] Loaded previous connection: " +
                    $"{address}, slot={slotName}"
                );

                return true;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP SETTINGS] Failed loading connection: {ex}"
                );

                return false;
            }
        }

        public static void Save(
            string address,
            string slotName,
            string password)
        {
            try
            {
                Directory.CreateDirectory(
                    SettingsDirectory
                );

                File.WriteAllLines(
                    SettingsFile,
                    new[]
                    {
                        address,
                        slotName,
                        password ?? ""
                    }
                );

                Plugin.LogSource.LogInfo(
                    $"[AP SETTINGS] Saved connection: " +
                    $"{address}, slot={slotName}"
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP SETTINGS] Failed saving connection: {ex}"
                );
            }
        }
    }
}