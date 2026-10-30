using System;
using System.Reflection;
using HarmonyLib;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// Handles canonical AP item rewards authored through
    /// AddRemoveItemAction(Add).
    ///
    /// AddRemoveItemAction.Act returns IEnumerator, so patching Act itself
    /// only tells us when the coroutine was CREATED, not when it FINISHED.
    ///
    /// We therefore patch the generated Act coroutine's MoveNext().
    /// When MoveNext returns false, the authored action has completed.
    /// </summary>
    [HarmonyPatch(
        typeof(AddRemoveItemAction._Act_d__6),
        nameof(AddRemoveItemAction._Act_d__6.MoveNext)
    )]
        internal static class AddRemoveItemAction_ActCoroutine_APDiscovery_Patch
    {
        


        [HarmonyPostfix]
        private static void Postfix(
            object __instance,
            bool __result)
        {
            // IEnumerator.MoveNext():
            //
            // true  = coroutine is still running
            // false = coroutine has finished
            //
            // Do absolutely nothing until it has finished.
            if (__result)
                return;

            try
            {
                AddRemoveItemAction? action =
                    FindOwningAction(__instance);

                if (action == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP DIALOG REWARD] Completed Act coroutine, but " +
                        "could not recover its AddRemoveItemAction."
                    );

                    return;
                }

                if (action.behavior !=
                    AddRemoveItemAction.AddRemoveBehavior.Add)
                {
                    return;
                }

                Item item = action.item;

                if (item == null)
                    return;

                RandomizedItemData? data =
                    ItemData.ByGuid(item.GetGUID());

                // Hidden quest tokens and internal state items do not
                // participate. Only actual AP discovery locations do.
                if (data == null ||
                    !data.CreatesLocation ||
                    !data.LocationId.HasValue)
                {
                    return;
                }

                Plugin.LogSource.LogInfo(
                    $"[AP DIALOG REWARD] Authored Add completed: " +
                    $"item='{data.Name}', guid={data.Guid}, " +
                    $"checkedAfterVanilla=" +
                    $"{ItemRandomizer.IsLocationChecked(data.Guid)}"
                );

                /*
                 * If normal Inventory.NewItem/AddItem interception handled
                 * the reward, CheckedItems is already true and this becomes
                 * a no-op.
                 *
                 * If vanilla skipped the physical acquisition because the
                 * player already owns the item, the location is still
                 * unchecked and this sends the missing AP check.
                 */
                ItemRandomizer.ProcessAuthoredRewardAction(
                    item,
                    "AddRemoveItemAction.Act coroutine completion"
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP DIALOG REWARD] Completed-action hook failed: {ex}"
                );
            }
        }


        /// <summary>
        /// The compiler-generated iterator stores a reference back to the
        /// original AddRemoveItemAction ("this").
        ///
        /// Rather than relying on the compiler-generated field name
        /// (usually something resembling <>4__this), find it by type.
        /// </summary>
        private static AddRemoveItemAction? FindOwningAction(
            object stateMachine)
        {
            if (stateMachine == null)
                return null;

            Type stateType = stateMachine.GetType();

            foreach (FieldInfo field in
                     stateType.GetFields(
                         BindingFlags.Instance |
                         BindingFlags.Public |
                         BindingFlags.NonPublic))
            {
                if (!typeof(AddRemoveItemAction)
                        .IsAssignableFrom(field.FieldType))
                {
                    continue;
                }

                try
                {
                    return field.GetValue(stateMachine)
                        as AddRemoveItemAction;
                }
                catch
                {
                }
            }

            // Some IL2CPP interop-generated wrappers expose native fields
            // as properties rather than ordinary managed fields.
            foreach (PropertyInfo property in
                     stateType.GetProperties(
                         BindingFlags.Instance |
                         BindingFlags.Public |
                         BindingFlags.NonPublic))
            {
                if (!typeof(AddRemoveItemAction)
                        .IsAssignableFrom(property.PropertyType))
                {
                    continue;
                }

                if (property.GetIndexParameters().Length != 0)
                    continue;

                try
                {
                    return property.GetValue(stateMachine)
                        as AddRemoveItemAction;
                }
                catch
                {
                }
            }

            return null;
        }
    }
}