"""Drop metadata and save text from publico json files."""

import json

from src.constants import DATA_PATH
from src.data import Dataset


def main():
    publico_path = DATA_PATH / "publico"

    texts = set()
    dataset = Dataset("pt")
    for in_fp in publico_path.glob("*.json"):
        content = json.load(in_fp.open())
        text = content["texto"].strip()
        if text and text.lower() not in texts:
            dataset.add(content["id"], text)
            texts.add(text.lower())
    dataset.save()


if __name__ == "__main__":
    main()
