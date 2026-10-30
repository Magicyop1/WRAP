using System;
using System.Collections.Generic;
using System.IO;

namespace WitheringRoomsArchipelago
{
    public static class ItemCatalog
    {
        private static readonly HashSet<string> KnownGuids = new();

        private static readonly string CatalogPath =
            Path.Combine(
                BepInEx.Paths.PluginPath,
                "WitheringRoomsArchipelago",
                "item_catalog.csv"
            );

        public static void Initialize()
        {
            try
            {
                string? directory = Path.GetDirectoryName(CatalogPath);

                if (!string.IsNullOrEmpty(directory))
                    Directory.CreateDirectory(directory);

                if (!File.Exists(CatalogPath))
                {
                    File.WriteAllText(
                        CatalogPath,
                        "GUID,ShortGUID,Title,DebugName,Type,Dynamic\n"
                    );

                    Plugin.LogSource.LogInfo(
                        $"Created item catalog at: {CatalogPath}"
                    );

                    return;
                }

                foreach (string line in File.ReadLines(CatalogPath))
                {
                    if (line.StartsWith("GUID,"))
                        continue;

                    string[] columns = line.Split(',');

                    if (columns.Length > 0 &&
                        !string.IsNullOrWhiteSpace(columns[0]))
                    {
                        KnownGuids.Add(columns[0].Trim('"'));
                    }
                }

                Plugin.LogSource.LogInfo(
                    $"Loaded {KnownGuids.Count} previously catalogued items."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"Failed to initialize item catalog: {ex}"
                );
            }
        }

        public static void RecordItem(Item item)
        {
            try
            {
                if (item == null)
                    return;

                string guid = item.GetGUID();

                if (string.IsNullOrWhiteSpace(guid))
                    return;

                // Already encountered during this or an earlier run.
                if (!KnownGuids.Add(guid))
                    return;

                string shortGuid = item.GetShortGUID() ?? "";
                string title = item.GetTitle() ?? "";
                string debugName = item.DebugName() ?? "";
                string type = item.GetType().Name ?? "";
                bool dynamicItem = item.IsDynamic();

                string line =
                    $"{Csv(guid)}," +
                    $"{Csv(shortGuid)}," +
                    $"{Csv(title)}," +
                    $"{Csv(debugName)}," +
                    $"{Csv(type)}," +
                    $"{dynamicItem}";

                File.AppendAllText(
                    CatalogPath,
                    line + Environment.NewLine
                );

                Plugin.LogSource.LogInfo(
                    $"[CATALOG] New item: {title} / {debugName} / {guid}"
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"Failed to record item in catalog: {ex}"
                );
            }
        }

        private static string Csv(string value)
        {
            if (value == null)
                return "\"\"";

            return "\"" + value.Replace("\"", "\"\"") + "\"";
        }
    }
}