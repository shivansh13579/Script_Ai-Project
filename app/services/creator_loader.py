import json
from pathlib import Path

BASE_PATH = Path("app/datasets/creators")

def load_creator_style(creator_name: str):

    creator_path = BASE_PATH / creator_name

    print("creator_path",creator_path)

    data = {}

    for file in creator_path.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data[file.stem] = json.load(f)

    return data