using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace WitheringRoomsArchipelago
{
    public static class ArchipelagoState
    {
        private static string? currentSeed;
        private static string? currentSlot;

        private static readonly HashSet<string>
    completedGoals =
        new(StringComparer.OrdinalIgnoreCase);

        public static IReadOnlyCollection<string>
            CompletedGoals => completedGoals;

        private static string StateDirectory =>
            Path.Combine(
                BepInEx.Paths.ConfigPath,
                "WitheringRoomsArchipelago"
            );

        private static string StateFile
        {
            get
            {
                if (string.IsNullOrEmpty(currentSeed) ||
                    string.IsNullOrEmpty(currentSlot))
                {
                    throw new InvalidOperationException(
                        "ArchipelagoState has not been initialized."
                    );
                }

                string safeSeed =
                    MakeSafeFileName(currentSeed);

                string safeSlot =
                    MakeSafeFileName(currentSlot);

                /*
                 * Keep the existing filename so current users
                 * automatically migrate from the old one-value format.
                 */
                return Path.Combine(
                    StateDirectory,
                    $"{safeSeed}_{safeSlot}_received_item_index.txt"
                );
            }
        }


        public static int ProcessedItemCount
        {
            get;
            private set;
        }


        public static int HighestUnlockedChapter
        {
            get;
            private set;
        }


        public static bool Initialized =>
            !string.IsNullOrEmpty(currentSeed) &&
            !string.IsNullOrEmpty(currentSlot);


        public static void Initialize(
            string seed,
            string slot)
        {
            currentSeed = seed;
            currentSlot = slot;

            Plugin.LogSource.LogInfo(
                $"[AP STATE] Initializing state for " +
                $"seed=\"{seed}\", slot=\"{slot}\""
            );

            Load();
        }


        private static void Load()
        {
            ProcessedItemCount = 0;
            HighestUnlockedChapter = 0;
            completedGoals.Clear();

            try
            {
                Directory.CreateDirectory(
                    StateDirectory
                );

                if (!File.Exists(StateFile))
                {
                    Plugin.LogSource.LogInfo(
                        "[AP STATE] No previous state file " +
                        "for this seed/slot. Starting fresh."
                    );

                    return;
                }

                string[] lines =
                    File.ReadAllLines(StateFile);

                /*
                 * Backward compatibility:
                 *
                 * The old format was simply:
                 *
                 *     4
                 *
                 * meaning ProcessedItemCount == 4.
                 */
                if (lines.Length == 1 &&
                    !lines[0].Contains("="))
                {
                    if (int.TryParse(
                        lines[0].Trim(),
                        out int legacyCount))
                    {
                        ProcessedItemCount =
                            Math.Max(0, legacyCount);
                    }

                    Plugin.LogSource.LogInfo(
                        $"[AP STATE] Loaded legacy state. " +
                        $"ProcessedItemCount={ProcessedItemCount}, " +
                        $"HighestUnlockedChapter=0"
                    );

                    /*
                     * Immediately migrate it to the new format.
                     */
                    Save();

                    return;
                }


                foreach (string rawLine in lines)
                {
                    string line = rawLine.Trim();

                    if (string.IsNullOrEmpty(line))
                        continue;

                    int separator =
                        line.IndexOf('=');

                    if (separator <= 0)
                        continue;

                    string key =
                        line.Substring(
                            0,
                            separator
                        ).Trim();

                    string value =
                        line.Substring(
                            separator + 1
                        ).Trim();


                    if (key.Equals(
                        "processedItemCount",
                        StringComparison.OrdinalIgnoreCase))
                    {
                        if (int.TryParse(
                            value,
                            out int count))
                        {
                            ProcessedItemCount =
                                Math.Max(0, count);
                        }
                    }
                    else if (key.Equals(
                        "highestUnlockedChapter",
                        StringComparison.OrdinalIgnoreCase))
                    {
                        if (int.TryParse(
                            value,
                            out int chapter))
                        {
                            HighestUnlockedChapter =
                                Math.Max(0, chapter);
                        }
                    }
                    else if (key.Equals(
    "completedGoal",
    StringComparison.OrdinalIgnoreCase))
                    {
                        if (!string.IsNullOrWhiteSpace(value))
                        {
                            completedGoals.Add(
                                value
                            );
                        }
                    }
                }


                Plugin.LogSource.LogInfo(
                    $"[AP STATE] Loaded state: " +
                    $"ProcessedItemCount={ProcessedItemCount}, " +
                    $"HighestUnlockedChapter=" +
                    $"{HighestUnlockedChapter}, " +
                    $"CompletedGoals=[" +
                    $"{string.Join(", ", completedGoals)}]"
                );
            }
            catch (Exception ex)
            {
                ProcessedItemCount = 0;
                HighestUnlockedChapter = 0;
                completedGoals.Clear();

                Plugin.LogSource.LogError(
                    $"[AP STATE] Failed loading state: {ex}"
                );
            }
        }


        public static void SetProcessedItemCount(
            int count)
        {
            if (!Initialized)
            {
                Plugin.LogSource.LogWarning(
                    "[AP STATE] Tried to save processed item " +
                    "count before ArchipelagoState was initialized."
                );

                return;
            }

            ProcessedItemCount =
                Math.Max(0, count);

            Save();
        }


        /// <summary>
        /// Records the furthest chapter ever reached for this
        /// Archipelago seed/slot.
        ///
        /// This value is monotonic: travelling backwards can never
        /// remove access to a previously reached chapter.
        /// </summary>
        public static void UnlockChapter(
            int chapter)
        {
            if (!Initialized)
                return;

            chapter =
                Math.Max(0, chapter);

            if (chapter <= HighestUnlockedChapter)
                return;

            HighestUnlockedChapter = chapter;

            Plugin.LogSource.LogInfo(
                $"[AP STATE] Highest unlocked chapter is now " +
                $"{HighestUnlockedChapter}."
            );

            Save();
        }


        public static bool IsGoalCompleted(
    string goal)
        {
            return completedGoals.Contains(
                goal
            );
        }


        public static bool CompleteGoal(
    string goal)
        {
            if (!Initialized)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP STATE] Tried to record goal " +
                    $"\"{goal}\" before state initialization."
                );

                return false;
            }

            if (!completedGoals.Add(goal))
            {
                return false;
            }

            Plugin.LogSource.LogInfo(
                $"[AP STATE] Goal completed: {goal}"
            );

            Save();

            return true;
        }


        private static void Save()
        {
            if (!Initialized)
                return;

            try
            {
                Directory.CreateDirectory(
                    StateDirectory
                );

                List<string> lines = new()
        {
            $"processedItemCount={ProcessedItemCount}",
            $"highestUnlockedChapter={HighestUnlockedChapter}"
        };

                foreach (string goal in
                    completedGoals.OrderBy(
                        goal => goal,
                        StringComparer.OrdinalIgnoreCase))
                {
                    lines.Add(
                        $"completedGoal={goal}"
                    );
                }

                File.WriteAllLines(
                    StateFile,
                    lines
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP STATE] Failed saving state: {ex}"
                );
            }
        }


        public static void Reset()
        {
            if (!Initialized)
            {
                ProcessedItemCount = 0;
                HighestUnlockedChapter = 0;
                completedGoals.Clear();
                return;
            }

            ProcessedItemCount = 0;
            HighestUnlockedChapter = 0;
            completedGoals.Clear();

            Save();
        }


        private static string MakeSafeFileName(
            string value)
        {
            char[] invalidChars =
                Path.GetInvalidFileNameChars();

            return new string(
                value.Select(
                    c => invalidChars.Contains(c)
                        ? '_'
                        : c
                ).ToArray()
            );
        }
    }
}