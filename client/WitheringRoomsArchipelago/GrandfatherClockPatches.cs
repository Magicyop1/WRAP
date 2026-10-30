using System;
using HarmonyLib;

namespace WitheringRoomsArchipelago
{
    [HarmonyPatch(
        typeof(StandardInteractableComponent),
        nameof(StandardInteractableComponent.Interact)
    )]
    internal static class GrandfatherClockInteractPatch
    {
        [HarmonyPrefix]
        private static bool Prefix(
    StandardInteractableComponent __instance)
        {
            try
            {
                /*
                 * This deliberately remains true after the menu closes
                 * if chapter travel is underway.  In particular, it
                 * consumes the E press which confirmed travel.
                 */
                if (ChapterTravelUI.ShouldBlockWorldInteraction)
                {
                    Plugin.LogSource.LogInfo(
                        "[AP CLOCK DEBUG] Suppressed standard interaction " +
                        "while AP chapter UI/travel owns input."
                    );

                    return false;
                }

                if (!ArchipelagoClient.Connected)
                    return true;

                if (!IsGrandfatherClock(__instance))
                    return true;

                Plugin.LogSource.LogInfo(
                    "[AP CLOCK] Intercepted Grandfather Clock interaction."
                );

                ChapterTravelUI.Open(__instance);

                return false;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    "[AP CLOCK] Failed to intercept Grandfather Clock: " +
                    ex
                );

                return true;
            }
        }


        private static bool IsGrandfatherClock(
            StandardInteractableComponent interactable)
        {
            if (interactable == null)
                return false;

            try
            {
                if (interactable.gameObject == null)
                    return false;

                string name =
                    interactable.gameObject.name;

                if (string.IsNullOrEmpty(name))
                    return false;

                /*
                 * This is the instantiated authored prefab name observed
                 * directly in-game:
                 *
                 *     GrandfatherClock(Clone)
                 *
                 * Normalize Unity's normal clone suffix so this also works
                 * if we ever encounter the prefab without the suffix.
                 */
                const string cloneSuffix = "(Clone)";

                if (name.EndsWith(
                    cloneSuffix,
                    StringComparison.Ordinal))
                {
                    name = name.Substring(
                        0,
                        name.Length - cloneSuffix.Length
                    );
                }

                return string.Equals(
                    name,
                    "GrandfatherClock",
                    StringComparison.Ordinal
                );
            }
            catch
            {
                return false;
            }
        }
    }
}