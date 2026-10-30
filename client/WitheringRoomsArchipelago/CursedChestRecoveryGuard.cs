using System;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// Identifies acquisitions that are restoring an item from a previous
    /// night through an Otherworld / cursed recovery chest.
    ///
    /// These are not legitimate vanilla source discoveries for Archipelago:
    /// the item should simply be restored to physical inventory.
    /// </summary>
    internal static class CursedChestRecoveryGuard
    {
        public static bool IsRecoveryAcquisition(
            bool ressurected,
            MansionSimulationObject sourceObject,
            out bool hasResurrectableTreasureComponent)
        {
            hasResurrectableTreasureComponent = false;

            if (sourceObject != null)
            {
                try
                {
                    SimulationRessurectableTreasureComponent component =
                        sourceObject.GetComponent<SimulationRessurectableTreasureComponent>();

                    hasResurrectableTreasureComponent =
                        component != null;
                }
                catch (Exception ex)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP RECOVERY CHEST] Could not inspect source for " +
                        "SimulationRessurectableTreasureComponent: " +
                        ex.Message
                    );
                }
            }

            return ressurected || hasResurrectableTreasureComponent;
        }
    }
}
