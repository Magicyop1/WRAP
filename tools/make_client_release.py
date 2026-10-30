"""Prepare a player-only distribution from a freshly compiled RELEASE build.
Deliberately does NOT embed BepInEx, game assemblies, or debug builds.
"""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parents[1]
build = root / 'client' / 'WitheringRoomsArchipelago' / 'bin' / 'Release' / 'net6.0'
dlls = ['WitheringRoomsArchipelago.dll',
        'Archipelago.MultiClient.Net.dll', 'Newtonsoft.Json.dll']
for file in dlls:
    if not (build/file).is_file():
        raise SystemExit(f'Missing {file}. First run dotnet build -c Release.')
destination = root / 'dist' / 'WitheringRoomsArchipelago-Client.zip'
destination.parent.mkdir(exist_ok=True)
with ZipFile(destination, 'w', compression=ZIP_DEFLATED) as z:
    for file in dlls:
        z.write(build/file, f'BepInEx/plugins/WitheringRoomsArchipelago/{file}')
print(f'Player package built: {destination}')
