using System;
using UnityEngine;

namespace WitheringRoomsArchipelago
{
    internal static class DeathLinkManager
    {
        private static SimulationDamageableComponent attachedDamageable;

        // Keep the managed delegates alive for as long as they are registered
        // with the IL2CPP object.
        private static Action<SimulationDamageableComponent.LivingStatus> diedHandler;
        private static Action resurrectedHandler;

        // A DeathLink we have received but have not yet been able to apply.
        private static bool remoteDeathPending;


        private static string remoteDeathSource = "";
        private static string remoteDeathCause = "";


        private static string pendingRemoteSource = "";
        private static string pendingRemoteCause = "";

        // True from the moment we deliberately cause a received DeathLink
        // until the player resurrects / a new player object is created.
        //
        // While this is true, any death callback belongs to the remote-caused
        // death and must not be echoed back to the Archipelago server.
        private static bool suppressNextLocalDeath;

        // Prevent duplicate sends if, for some reason, the game's death
        // callback fires more than once before resurrection.
        private static bool deathAlreadyReported;


        public static void Update()
        {
            if (!ArchipelagoClient.DeathLinkEnabled)
                return;

            TryAttachToPlayer();

            if (remoteDeathPending && attachedDamageable != null)
            {
                ApplyRemoteDeath();
            }
        }

        public static void QueueRemoteDeath(
    string source,
    string cause)
        {
            if (!ArchipelagoClient.DeathLinkEnabled)
                return;

            pendingRemoteSource =
                string.IsNullOrWhiteSpace(source) ? "another player" : source;

            pendingRemoteCause =
                cause ?? "";

            Plugin.LogSource.LogWarning(
                $"[AP DEATHLINK] Remote DeathLink queued. " +
                $"Source={pendingRemoteSource}, Cause={pendingRemoteCause}"
            );

            remoteDeathPending = true;
        }

        private static void TryAttachToPlayer()
        {
            try
            {
                var player = PlayerController.instance;

                if (player == null || player.simulationObject == null)
                {
                    // If our old player object disappeared, forget it.
                    if (attachedDamageable != null)
                        Detach();

                    return;
                }

                var damageable =
                    player.simulationObject
                        .GetComponent<SimulationDamageableComponent>();

                if (damageable == null)
                {
                    if (attachedDamageable != null)
                        Detach();

                    return;
                }

                // Still attached to the same component.
                if (attachedDamageable == damageable)
                    return;

                // Player object/component changed, e.g. because of a reload.
                Detach();

                attachedDamageable = damageable;

                diedHandler =
                    new Action<SimulationDamageableComponent.LivingStatus>(
                        OnPlayerDied
                    );

                resurrectedHandler =
                    new Action(
                        OnPlayerResurrected
                    );

                attachedDamageable.diedDelegate += diedHandler;
                attachedDamageable.resurrectedDelegate += resurrectedHandler;

                // We have attached to a live/new player instance.
                deathAlreadyReported = false;
                suppressNextLocalDeath = false;

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Attached to player damageable component " +
                    "(death + resurrection delegates)."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Failed to attach to player: " + ex
                );
            }
        }

        private static void Detach()
        {
            if (attachedDamageable != null)
            {
                try
                {
                    if (diedHandler != null)
                        attachedDamageable.diedDelegate -= diedHandler;

                    if (resurrectedHandler != null)
                        attachedDamageable.resurrectedDelegate -= resurrectedHandler;
                }
                catch (Exception ex)
                {
                    // Object destruction/reload can make the old IL2CPP object
                    // invalid. Losing the old attachment is still what we want.
                    Plugin.LogSource.LogDebug(
                        "[AP DEATHLINK] Exception while detaching old player: " +
                        ex.Message
                    );
                }
            }

            attachedDamageable = null;
            diedHandler = null;
            resurrectedHandler = null;
            deathAlreadyReported = false;
            suppressNextLocalDeath = false;
        }

        private static void OnPlayerDied(
            SimulationDamageableComponent.LivingStatus livingStatus)
        {
            try
            {
                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Player death delegate fired. " +
                    "LivingStatus=" + livingStatus
                );

                // This death was deliberately caused by an incoming DeathLink.
                // Do not echo it back to the AP server.
                if (suppressNextLocalDeath)
                {
                    /*
                     * Do NOT clear suppressNextLocalDeath here.
                     *
                     * A received DeathLink owns the entire death sequence.
                     * It is cleared by OnPlayerResurrected(), or when the old
                     * player object is detached during a reload/respawn.
                     */
                    deathAlreadyReported = true;

                    Plugin.LogSource.LogInfo(
                        "[AP DEATHLINK] Suppressed outgoing DeathLink " +
                        "for remote-caused death."
                    );

                    return;
                }

                // Defensive duplicate protection.
                if (deathAlreadyReported)
                {
                    Plugin.LogSource.LogDebug(
                        "[AP DEATHLINK] Ignoring duplicate death callback."
                    );

                    return;
                }

                deathAlreadyReported = true;

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Natural player death detected; " +
                    "sending DeathLink."
                );

                DeathLinkNoticeUI.Show("Sending DeathLink...", 2.0f);

                bool sent =
    ArchipelagoClient.SendDeathLink(
        "died in the dream."
    );

                Plugin.LogSource.LogInfo(
                                $"[AP DEATHLINK] SendDeathLink result = {sent}"
                            );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    "[AP DEATHLINK] Error handling player death: " + ex
                );
            }
        }

        private static void OnPlayerResurrected()
        {
            try
            {
                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Player resurrection detected; " +
                    "DeathLink re-armed."
                );

                // The same player can now legitimately die again.
                deathAlreadyReported = false;

                // Any remote-death suppression should have been consumed by
                // the death callback. Clear it defensively here as well.
                suppressNextLocalDeath = false;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    "[AP DEATHLINK] Error handling player resurrection: " + ex
                );
            }
        }
        private static bool TryApplyInstantRemoteDeath()
        {
            /*
             * Shared by:
             *
             *   1. real received DeathLinks
             *   2. Ctrl+Shift+K local testing
             *
             * The goal is to reproduce a real Withering Rooms death,
             * including the visible death reaction, rather than merely
             * jumping directly to the scenario's PlayerDead state.
             */

            TryAttachToPlayer();

            if (attachedDamageable == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot apply remote death: " +
                    "player damageable component is unavailable."
                );

                return false;
            }

            PlayerController player =
                PlayerController.instance;

            if (player == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot apply remote death: " +
                    "PlayerController is unavailable."
                );

                return false;
            }

            DamageableComponent liveDamageable =
                player.GetComponent<DamageableComponent>();

            if (liveDamageable == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot apply remote death: " +
                    "live DamageableComponent is unavailable."
                );

                return false;
            }

            GlobalGameSettings settings =
                GlobalGameSettings.instance;

            if (settings == null ||
                settings.healthStat == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Cannot apply remote death: " +
                    "health StatType is unavailable."
                );

                return false;
            }

            try
            {
                /*
                 * From this point until resurrection/reload, any death callback
                 * belongs to the received DeathLink and must not be echoed.
                 */
                suppressNextLocalDeath = true;

                Plugin.LogSource.LogWarning(
                    "[AP DEATHLINK] Applying instant remote death."
                );

                /*
                 * ForceDie() by itself brings the WR player to zero health,
                 * which normally activates the Danger grace state.
                 */
                attachedDamageable.ForceDie();

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] ForceDie applied. " +
                    "LivingStatus=" +
                    attachedDamageable.GetLivingStatus()
                );

                /*
                 * The vanilla rule is that taking damage AGAIN while at
                 * zero health / in Danger causes the real death.
                 *
                 * Therefore give the player one point of genuine health
                 * damage through the normal DamageableComponent pipeline.
                 */
                Damage finishingDamage =
                    new Damage();

                DamageValue healthDamage =
                    new DamageValue();

                healthDamage.damageType =
                    DamageType.CreateDynamic(
                        settings.healthStat,
                        false
                    );

                healthDamage.value = 1;

                finishingDamage.v =
                    new Il2CppSystem.Collections.Generic.List<
                        DamageValue>();

                finishingDamage.v.Add(
                    healthDamage
                );

                finishingDamage.sourceType =
                    DamageSourceType.Unknown;

                finishingDamage.blockability =
                    DamageBlockability.NotBlockable;

                finishingDamage.shouldHitStop = false;
                finishingDamage.telemetry = false;

                /*
                 * Use the LIVE damageable component here rather than directly
                 * manipulating the simulation state. That gives vanilla its
                 * normal opportunity to start its death reaction/animation.
                 */
                /*
 * Do NOT use the ordinary DoDamage path here.
 *
 * DangerEquippableItem modifies incoming applied damage during
 * the Danger grace state.  That is exactly what prevented our
 * previous finishing hit from killing the player.
 *
 * InnerApplyDamage is the simulation's lower-level application
 * stage, underneath that outer damage-modification pipeline.
 * We still use real health damage, so the SimulationDamageableComponent
 * gets to perform its normal actual-death handling.
 */
                attachedDamageable.InnerApplyDamage(
                    finishingDamage,
                    null
                );

                SimulationDamageableComponent.LivingStatus finalStatus =
                    attachedDamageable.GetLivingStatus();

                Plugin.LogSource.LogInfo(
                    "[AP DEATHLINK] Inner finishing damage applied. " +
                    "LivingStatus=" + finalStatus +
                    ", LiveStartedDead=" + liveDamageable.StartedDead()
                );

                /*
                 * If this did NOT actually produce DeadHealth, do not leave the
                 * DeathLink suppression armed forever.  The previous failed test
                 * could otherwise cause the player's next genuine death to be
                 * mistaken for the remote-caused death.
                 */
                if (finalStatus !=
                    SimulationDamageableComponent.LivingStatus.DeadHealth)
                {
                    suppressNextLocalDeath = false;

                    Plugin.LogSource.LogWarning(
                        "[AP DEATHLINK] Inner finishing damage did not produce " +
                        "DeadHealth; remote death attempt failed."
                    );

                    return false;
                }

                return true;
                /*
                 * IMPORTANT:
                 *
                 * Do NOT call:
                 *
                 *     GameScenarioManager.instance.EnterState(
                 *         GameScenarioState.PlayerDead);
                 *
                 * If the finishing damage produced a genuine death, vanilla
                 * will enter PlayerDead itself after the normal death reaction.
                 */
                return true;
            }
            catch (Exception ex)
            {
                suppressNextLocalDeath = false;

                Plugin.LogSource.LogError(
                    "[AP DEATHLINK] Failed to apply instant remote death: " +
                    ex
                );

                return false;
            }
        }


        private static void ApplyRemoteDeath()
        {
            string source =
                pendingRemoteSource;

            string cause =
                pendingRemoteCause;

            /*
             * Use the exact proven instant-death path:
             *
             * ForceDie()
             *     -> Danger
             * InnerApplyDamage()
             *     -> true DeadHealth
             *     -> normal vanilla death sequence
             */
            if (!TryApplyInstantRemoteDeath())
            {
                return;
            }

            string who =
                string.IsNullOrWhiteSpace(source)
                    ? "another player"
                    : source;

            string uiMessage =
                $"DeathLink triggered by {who}";

            if (!string.IsNullOrWhiteSpace(cause))
            {
                uiMessage +=
                    $"\n{cause}";
            }

            DeathLinkNoticeUI.Show(
                uiMessage,
                3.5f
            );

            remoteDeathPending = false;
            pendingRemoteSource = "";
            pendingRemoteCause = "";
        }



        public static void Reset()
        {
            Detach();

            remoteDeathPending = false;
            suppressNextLocalDeath = false;
            deathAlreadyReported = false;
            remoteDeathSource = "";
            remoteDeathCause = "";

            DeathLinkOverlay.Clear();

            Plugin.LogSource.LogInfo(
                "[AP DEATHLINK] Manager reset."
            );
        }
    }
}