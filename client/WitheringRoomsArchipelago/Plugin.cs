using BepInEx;
using BepInEx.Logging;
using BepInEx.Unity.IL2CPP;
using Il2CppInterop.Runtime.Injection;
using UnityEngine;
using Archipelago.MultiClient.Net;
using HarmonyLib;



namespace WitheringRoomsArchipelago
{
    [BepInPlugin(
        "davidruth.witheringrooms.archipelago",
        "Withering Rooms Archipelago",
        "0.0.1")]
    public class Plugin : BasePlugin
    {
        internal static ManualLogSource LogSource = null!;

        private ArchipelagoSession? session;
        private Harmony? harmony;

        public override void Load()
        {
            LogSource = Log;

            Log.LogInfo("Withering Rooms Archipelago loaded!");

            ItemCatalog.Initialize();

            session = ArchipelagoSessionFactory.CreateSession(
                "localhost",
                38281
            );

            Log.LogInfo("Archipelago session object created.");

            AddComponent<ArchipelagoBehaviour>();

            Log.LogInfo("ArchipelagoBehaviour component added.");

            harmony = new Harmony(
                "davidruth.witheringrooms.archipelago"
            );

            harmony.PatchAll();

            Log.LogInfo("Harmony patches applied.");

            //ArchipelagoState.Load();

        }
    }
}