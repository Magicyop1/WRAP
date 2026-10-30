# Withering Rooms — Archipelago (community alpha)

Unofficial [Archipelago](https://archipelago.gg/) multiworld integration for *Withering Rooms*.
This project is community-made, not affiliated with the game's developer or the Archipelago core maintainers. All credit for Withering Rooms and its assets goes to Moonless Formless.

The current build is an alpha, and while it works reasonably well, bugs or logic errors are still likely. Currently the only 



## Features

* Basic randomization and generation logic for all equipment and non-repeatable items
* Grandfather Clocks can be used to travel to previous chapters to obtain missed checks. If you do not have the Grandfather Clock key, this will kill you and reset your inventory accordingly. Holding the Grandfather Clock Key will enable free travel between chapters you have already accessed.
* MonsterSanity can be enabled in the config, providing locations for all unique monster and boss kills.
* LoreSanity can be enabled in the config, providing locations for each unique lore page read.
* Without these on there will be very few filler locations available, so it is recommended to play with one or both of these.
* Add extra coin purses, remembrance tears, or stats to the pool in the config.
* DeathLink can be enabled in the config
* Currently the only goal that has been tested is completion of the game's main boss.





## Planned Features

* Traps
* Locations and infrastructure for postgame content including Blighted Bestiary Pages and Starry Flesh
* Additional goals including Ending D and Blighted Bestiary full completion
* Possible monster and/or door randomization
* Resolve all items with unrecorded regions



## Repository structure

* `apworld/withering\_rooms/` — Python world logic and generated item/location definitions.
* `client/WitheringRoomsArchipelago/` — BepInEx 6 IL2CPP C# plugin source.
* `example/Withering Rooms.yaml` — starting YAML, edit your player name and options.
* `tools/build\_apworld.py` — builds `dist/withering\_rooms.apworld`.
* `tools/make\_client\_release.py` — builds a client ZIP from the fresh *Release* DLLs.



# Player setup (Windows)

1. Own and install **Withering Rooms**; use the game version listed in the matching GitHub Release.
2. Install the **BepInEx 6 Unity IL2CPP Windows x64** loader in the folder containing the game executable.
Match the version tested in the Release notes; do **not** use the ordinary BepInEx 5 Mono pack.
3. Run the game once and quit, so BepInEx creates `BepInEx/` and its IL2CPP interop assemblies.
4. Extract the release client ZIP into the **game root**. It installs:
`BepInEx/plugins/WitheringRoomsArchipelago/WitheringRoomsArchipelago.dll`,
`Archipelago.MultiClient.Net.dll`, and `Newtonsoft.Json.dll`.
Do not install the source ZIP or an old debug DLL.
5. Join a new Archipelago room. Start a **new Withering Rooms game** for that generated seed.
6. Press **F7** for the AP connection window; enter server address, player/slot name, and password if used.
Confirm connection in game and/or `BepInEx/LogOutput.log`.

