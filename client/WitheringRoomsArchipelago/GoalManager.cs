using System;
using System.Collections.Generic;

namespace WitheringRoomsArchipelago
{
    public static class GoalManager
    {
        /*
         * Maps the canonical Withering Rooms bestiary GUID
         * to the user-facing Archipelago completion-goal name.
         *
         * These strings must match the valid keys in the
         * APWorld CompletionGoals OptionSet.
         */
        private static readonly Dictionary<string, string>
            MonsterGuidToGoal =
                new(StringComparer.OrdinalIgnoreCase)
                {
                    {
                        "01ddaaf8d4565dc4cb95742a922c1dae",
                        "Priscilla Mostyn"
                    },
                    {
                        "9b58dc0db02dbf24fbb430eba593df8e",
                        "God Millie"
                    },
                };


        public static void ProcessDefeatedMonster(
            string guid)
        {
            if (string.IsNullOrWhiteSpace(guid))
                return;

            if (!MonsterGuidToGoal.TryGetValue(
                    guid,
                    out string? goal))
            {
                return;
            }

            bool newlyCompleted =
                ArchipelagoState.CompleteGoal(
                    goal
                );

            if (newlyCompleted)
            {
                Plugin.LogSource.LogInfo(
                    $"[AP GOAL] Objective completed: " +
                    $"{goal}"
                );
            }
            else
            {
                Plugin.LogSource.LogInfo(
                    $"[AP GOAL] Objective already completed: " +
                    $"{goal}"
                );
            }

            EvaluateCompletion();
        }




        public static void EvaluateCompletion()
        {
            if (!ArchipelagoState.Initialized)
                return;

            IReadOnlyCollection<string>
                requiredGoals =
                    ArchipelagoClient.CompletionGoals;

            if (requiredGoals.Count == 0)
            {
                Plugin.LogSource.LogWarning(
                    "[AP GOAL] No completion goals are " +
                    "configured; refusing to send victory."
                );

                return;
            }

            foreach (string requiredGoal in requiredGoals)
            {
                if (!ArchipelagoState.IsGoalCompleted(
                        requiredGoal))
                {
                    Plugin.LogSource.LogInfo(
                        $"[AP GOAL] Still required: " +
                        $"{requiredGoal}"
                    );

                    return;
                }
            }

            Plugin.LogSource.LogInfo(
                "[AP GOAL] All configured completion " +
                "goals have been completed."
            );

            ArchipelagoClient.SendGoalCompletion();
        }
    }
}