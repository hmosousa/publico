"""Drop metadata and save text from publico json files."""

import json

from src.contants import DATA_PATH


def main():
    
    publico_path = DATA_PATH / "publico"

    texts = set()
    parsed = []
    for in_fp in publico_path.glob("*.json"):
        content = json.load(in_fp.open())
        text = content["texto"].strip()
        if text and text.lower() not in texts:
            parsed.append({
                "id": content["id"],
                "text": text
            })

            texts.add(text.lower())
    
    parsed_path = DATA_PATH / "pt.jsonl"        
    json.dump(parsed, parsed_path.open("w"), ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
