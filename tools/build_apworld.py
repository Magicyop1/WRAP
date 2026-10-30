"""Package an APWorld from repository source. No Archipelago runtime required."""
from pathlib import Path
import zipfile
import ast
import json
root = Path(__file__).resolve().parents[1]
src = root / "apworld" / "withering_rooms"
target = root / "dist" / "withering_rooms.apworld"
target.parent.mkdir(exist_ok=True)
for py in src.glob("*.py"):
    ast.parse(py.read_text(encoding="utf-8"), filename=str(py))
json.loads((src / "archipelago.json").read_text(encoding="utf-8"))
with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(src.iterdir()):
        if p.suffix == ".py" or p.name == "archipelago.json":
            z.write(p, "withering_rooms/" + p.name)
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    assert "withering_rooms/__init__.py" in z.namelist()
print(f"APWorld built: {target}")
