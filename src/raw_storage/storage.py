from pathlib import Path
import json

def write_raw(data: list[dict], path: Path) -> Path:
    with open(path, "w") as f:
        json.dump(data, f)
    return path