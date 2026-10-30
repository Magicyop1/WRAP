using BepInEx.Unity.IL2CPP.Utils;
using System;
using System.Collections;
using UnityEngine;
using static GameScenarioManager;

namespace WitheringRoomsArchipelago
{
    public static class ChapterTravelManager
    {
        // Highest chapter/scenario observed during this game.
        //
        // First implementation only: this is runtime state.
        // Once the transition itself is proven, we can persist it.

        private static bool travelInProgress = false;
        private static float travelStartedAt = 0f;
        private static int lastTravelDiagnosticSecond = -1;

        private const float TravelCooldownSeconds = 3.0f;

        public static int HighestUnlockedChapter =>
            ArchipelagoState.Initialized
                ? ArchipelagoState.HighestUnlockedChapter
                : 0;

        public static bool TravelInProgress =>
            travelInProgress;

        /// <summary>
        /// Call periodically while a game is active.
        /// Observing a later vanilla chapter permanently unlocks
        /// all earlier chapters for this session.
        /// </summary>
        public static void UpdateUnlockedChapters()
        {
            GameScenarioManager manager =
                GameScenarioManager.instance;

            if (manager == null)
                return;

            if (!ArchipelagoState.Initialized)
                return;

            int currentChapter =
                manager.chapterIndex;

            int previousHighest =
                ArchipelagoState.HighestUnlockedChapter;

            if (currentChapter <= previousHighest)
                return;

            ArchipelagoState.UnlockChapter(
                currentChapter
            );

            Plugin.LogSource.LogInfo(
                $"[AP TIME TRAVEL] Unlocked chapter " +
                $"{currentChapter}. Highest unlocked chapter is now " +
                $"{ArchipelagoState.HighestUnlockedChapter}."
            );
        }

        public static bool IsChapterUnlocked(
            int chapter)
                {
                    return chapter >= 0 &&
                           chapter <= HighestUnlockedChapter;
                }

        /// <summary>
        /// Experimental first-pass scenario travel.
        ///
        /// This intentionally does NOT use EndChapter().
        /// EndChapter has chapter-completion semantics which we
        /// do not want for backwards travel.
        /// </summary>
        public static bool TravelToChapter(int destinationChapter)
        {
            if (travelInProgress)
            {
                Plugin.LogSource.LogWarning(
                    "[AP TIME TRAVEL] Travel already in progress."
                );

                return false;
            }

            GameScenarioManager manager =
                GameScenarioManager.instance;

            if (manager == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP TIME TRAVEL] GameScenarioManager is unavailable."
                );

                return false;
            }

            if (!IsChapterUnlocked(destinationChapter))
            {
                Plugin.LogSource.LogWarning(
                    $"[AP TIME TRAVEL] Chapter {destinationChapter} " +
                    "has not been unlocked."
                );

                return false;
            }

            if (manager.scenarioCards == null ||
                destinationChapter >= manager.scenarioCards.Count)
            {
                Plugin.LogSource.LogError(
                    $"[AP TIME TRAVEL] Chapter {destinationChapter} " +
                    "does not have a corresponding scenario card."
                );

                return false;
            }

            if (manager.chapterIndex == destinationChapter)
            {
                ChapterTravelUI.Close();
                ChapterTravelUI.ReleaseWorldInteraction();

                Plugin.LogSource.LogInfo(
                    $"[AP TIME TRAVEL] Already in chapter " +
                    $"{destinationChapter}."
                );

                return false;
            }

            int oldChapter = manager.chapterIndex;

            try
            {
                travelInProgress = true;
                travelStartedAt = Time.realtimeSinceStartup;



                Plugin.LogSource.LogInfo(
                    $"[AP TIME TRAVEL] Requesting travel: " +
                    $"{oldChapter} -> {destinationChapter}."
                );

                bool hasClockKey = HasClockKey();

                Plugin.LogSource.LogInfo(
                    $"[AP TIME TRAVEL] Grandfather Clock Key: " +
                    $"{(hasClockKey ? "OWNED" : "not owned")}."
                );

                manager.chapterIndex = destinationChapter;

                manager.SetPostLoadBehavior(
                    hasClockKey
                        ? PostLoadBehavior.ForceCoffin
                        : PostLoadBehavior.Normal
                );

                Plugin.LogSource.LogInfo(
                    $"[AP TIME TRAVEL] Entering Rebooting with " +
                    $"PostLoadBehavior=" +
                    $"{(hasClockKey ? "ForceCoffin" : "Normal")}."
                );

                manager.EnterState(
                    GameScenarioState.Rebooting
                );

                Plugin.LogSource.LogInfo(
                    $"[AP TIME TRAVEL] Entered Rebooting for " +
                    $"chapter {destinationChapter}."
                );

                return true;
            }
            catch (Exception ex)
            {
                manager.chapterIndex = oldChapter;

                travelInProgress = false;

                Plugin.LogSource.LogError(
                    $"[AP TIME TRAVEL] Travel failed: {ex}"
                );

                return false;
            }
        }

        /// <summary>
        /// Call after the game has returned to its normal playable state.
        /// </summary>
        /// <summary>
        /// Clears the travel guard after the reboot has had enough time to
        /// complete.  This guard only prevents repeated travel requests while
        /// the game is rebuilding the scenario; it does not control the actual
        /// scenario transition.
        /// </summary>
        public static void UpdateTravelState()
        {
            if (!travelInProgress)
                return;

            GameScenarioManager manager =
                GameScenarioManager.instance;

            if (manager == null)
                return;

            float elapsed =
                Time.realtimeSinceStartup - travelStartedAt;

            int diagnosticSecond = (int)elapsed;

            if (diagnosticSecond != lastTravelDiagnosticSecond)
            {
                lastTravelDiagnosticSecond = diagnosticSecond;

                bool inventoryExists =
                    Inventory.instance != null;

                bool inventoryReady =
                    inventoryExists &&
                    Inventory.instance.Ready();

                Plugin.LogSource.LogInfo(
                    $"[AP TIME TRAVEL DEBUG] " +
                    $"elapsed={elapsed:F1}, " +
                    $"chapter={manager.chapterIndex}, " +
                    $"inventoryExists={inventoryExists}, " +
                    $"inventoryReady={inventoryReady}"
                );
            }

            if (elapsed < TravelCooldownSeconds)
                return;

            if (Inventory.instance == null ||
                !Inventory.instance.Ready())
                return;

            travelInProgress = false;

            Plugin.LogSource.LogInfo(
                $"[AP TIME TRAVEL] Travel guard released after " +
                $"{elapsed:F1}s. Current chapter: " +
                $"{manager.chapterIndex}."
            );
            ChapterTravelUI.ReleaseWorldInteraction();
        }

        private const string ClockKeyGuid =
    "aad7d8862b70d974e9244f356b02723a";

        private static bool HasClockKey()
        {
            try
            {
                if (Inventory.instance == null ||
                    !Inventory.instance.Ready())
                    return false;

                Item key =
                    GameItems.FindItemByGuid(
                        ClockKeyGuid
                    );

                if (key == null)
                    return false;

                ItemInfo info =
                    Inventory.instance.GetInfo(key);

                return info != null &&
                       info.quantity >= 1;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    "[AP TIME TRAVEL] Failed to check Grandfather " +
                    "Clock Key: " + ex
                );

                return false;
            }
        }


    }

    public static class ChapterTravelUI
    {
        private static bool open = false;
        private static int selection = 0;

        // Prevent the E press which opened the clock menu
        // from immediately selecting an entry.
        private static float openedAt = 0f;

        private const float InputDelaySeconds = 0.20f;

        public static bool IsOpen => open;

        private static Vector3 lockedPlayerPosition;
        private static bool hasLockedPlayerPosition = false;

        private static bool blockWorldInteraction = false;

        public static bool ShouldBlockWorldInteraction =>
            open || blockWorldInteraction;

        private static StandardInteractableComponent currentClock = null;
        public static void Open(
            StandardInteractableComponent clock)
        {
            if (open)
                return;

            currentClock = clock;


            open = true;
            blockWorldInteraction = true;

            CapturePlayerPosition();

            ChapterTravelManager.UpdateUnlockedChapters();

            int highest =
                ChapterTravelManager.HighestUnlockedChapter;

            int current =
                GameScenarioManager.instance != null
                    ? GameScenarioManager.instance.chapterIndex
                    : 0;

            selection =
                Mathf.Clamp(
                    current,
                    0,
                    highest
                );

            openedAt = Time.realtimeSinceStartup;

            Plugin.LogSource.LogInfo(
                $"[AP TIME TRAVEL] Chapter selection opened. " +
                $"Current={current}, HighestUnlocked={highest}."
            );
        }

        private static void PlayClockChime(
    StandardInteractableComponent clock)
        {
            try
            {
                if (clock == null)
                    return;

                SimulationStandardInteractableComponent interaction =
                    clock.GetSimulation();

                if (interaction == null)
                    return;

                MansionSimulationObject simulationObject =
                    interaction.GetParent();

                if (simulationObject == null)
                    return;

                SimulationTimerComponent timer =
                    simulationObject
                        .GetComponent<SimulationTimerComponent>();

                if (timer == null || timer.sound == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP TIME TRAVEL] Grandfather Clock has no " +
                        "available timer sound."
                    );
                    return;
                }

                timer.sound.Play(
                    new Rand(),
                    new ProceduralDropTable(),
                    new FXImpactRequest(),
                    clock.transform
                );

                Plugin.LogSource.LogInfo(
                    "[AP TIME TRAVEL] Played Grandfather Clock chime."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    "[AP TIME TRAVEL] Could not play clock chime: " +
                    ex
                );
            }
        }


        public static void Close()
        {
            if (!open)
                return;

            open = false;
            currentClock = null;
            hasLockedPlayerPosition = false;

            Plugin.LogSource.LogInfo(
                "[AP TIME TRAVEL] Chapter selection closed."
            );
        }

        public static void ReleaseWorldInteraction()
        {
            blockWorldInteraction = false;

            Plugin.LogSource.LogInfo(
                "[AP TIME TRAVEL] World interaction guard released."
            );
        }


        public static void Update()
        {
            if (!open)
                return;

            HoldPlayerPosition();
        }


        public static void Draw()
        {
            if (!open)
                return;

            Event evt = Event.current;

            if (evt != null &&
                evt.type == EventType.KeyDown &&
                Time.realtimeSinceStartup - openedAt >= InputDelaySeconds)
            {
                int highest_2 =
                    ChapterTravelManager.HighestUnlockedChapter;

                if (evt.keyCode == KeyCode.W ||
                    evt.keyCode == KeyCode.UpArrow)
                {
                    selection--;

                    if (selection < 0)
                        selection = highest_2;

                    evt.Use();
                }
                else if (evt.keyCode == KeyCode.S ||
                         evt.keyCode == KeyCode.DownArrow)
                {
                    selection++;

                    if (selection > highest_2)
                        selection = 0;

                    evt.Use();
                }
                else if (evt.keyCode == KeyCode.C ||
                         evt.keyCode == KeyCode.Escape)
                {
                    Close();
                    ReleaseWorldInteraction();
                    evt.Use();
                    return;
                }
                else if (evt.keyCode == KeyCode.E ||
                         evt.keyCode == KeyCode.Return)
                {
                    int destination = selection;

                    if (!ChapterTravelManager.IsChapterUnlocked(destination))
                    {
                        evt.Use();
                        return;
                    }

                    if (GameScenarioManager.instance == null)
                    {
                        evt.Use();
                        return;
                    }

                    if (GameScenarioManager.instance.scenarioCards == null ||
                        destination >=
                            GameScenarioManager.instance.scenarioCards.Count)
                    {
                        evt.Use();
                        return;
                    }

                    // Selecting the current chapter does nothing.
                    if (GameScenarioManager.instance.chapterIndex == destination)
                    {
                        evt.Use();
                        return;
                    }

                    StandardInteractableComponent clock =
                        currentClock;

                    Close();

                    PlayClockChime(clock);

                    ChapterTravelManager.TravelToChapter(
                        destination
                    );

                    evt.Use();
                    return;
                }
            }

            int highest =
                ChapterTravelManager.HighestUnlockedChapter;

            int current =
                GameScenarioManager.instance != null
                    ? GameScenarioManager.instance.chapterIndex
                    : -1;

            const float width = 420f;

            float height =
                150f +
                ((highest + 1) * 36f);

            Rect boxRect =
                new Rect(
                    (Screen.width - width) / 2f,
                    (Screen.height - height) / 2f,
                    width,
                    height
                );

            GUI.Box(
                boxRect,
                ""
            );

            GUIStyle titleStyle =
                new GUIStyle(GUI.skin.label);

            titleStyle.alignment =
                TextAnchor.MiddleCenter;

            titleStyle.fontSize = 24;
            titleStyle.fontStyle = FontStyle.Bold;

            GUI.Label(
                new Rect(
                    boxRect.x + 20f,
                    boxRect.y + 15f,
                    boxRect.width - 40f,
                    40f
                ),
                "GRANDFATHER CLOCK",
                titleStyle
            );


            GUIStyle chapterStyle =
                new GUIStyle(GUI.skin.label);

            chapterStyle.fontSize = 20;
            chapterStyle.alignment =
                TextAnchor.MiddleLeft;


            float y =
                boxRect.y + 65f;

            for (int chapter = 0;
                 chapter <= highest;
                 chapter++)
            {
                string cursor =
                    chapter == selection
                        ? "> "
                        : "  ";

                string currentMarker =
                    chapter == current
                        ? "  (Current)"
                        : "";

                GUI.Label(
                    new Rect(
                        boxRect.x + 50f,
                        y,
                        boxRect.width - 100f,
                        32f
                    ),
                    $"{cursor}Chapter {chapter}" +
                    $"{currentMarker}",
                    chapterStyle
                );

                y += 36f;
            }


            GUIStyle helpStyle =
                new GUIStyle(GUI.skin.label);

            helpStyle.alignment =
                TextAnchor.MiddleCenter;

            helpStyle.fontSize = 15;

            GUI.Label(
                new Rect(
                    boxRect.x + 20f,
                    boxRect.yMax - 55f,
                    boxRect.width - 40f,
                    30f
                ),
                "W/S: Select     E: Travel     C: Close",
                helpStyle
            );
        }

        private static void CapturePlayerPosition()
        {
            hasLockedPlayerPosition = false;

            try
            {
                PlayerController player =
                    PlayerController.instance;

                if (player == null)
                    return;

                lockedPlayerPosition =
                    player.transform.position;

                hasLockedPlayerPosition = true;

                Plugin.LogSource.LogInfo(
                    "[AP TIME TRAVEL] Player position locked while " +
                    "chapter menu is open."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    "[AP TIME TRAVEL] Could not capture player " +
                    $"position: {ex}"
                );
            }
        }


        private static void HoldPlayerPosition()
        {
            if (!hasLockedPlayerPosition)
                return;

            try
            {
                PlayerController player =
                    PlayerController.instance;

                if (player == null)
                    return;

                player.transform.position =
                    lockedPlayerPosition;
            }
            catch
            {
                // Don't spam the log every frame.
            }
        }

    
    }
}