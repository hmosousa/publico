import json

from src.constants import DATA_PATH

HF_PATH = DATA_PATH / "hf" / "Publico"
HF_PATH.mkdir(exist_ok=True)

train_ids, test_ids = None, None
for filepath in DATA_PATH.glob("*.json"):
    lang = filepath.stem
    content = json.load((DATA_PATH / f"{lang}.json").open())

    if train_ids is None:
        train_size = int(0.8 * len(content))
        train_ids = list(content.keys())[:train_size]
        test_ids = list(content.keys())[train_size:]

    train = [{"id": id_, "text": content[id_]} for id_ in train_ids]
    test = [{"id": id_, "text": content[id_]} for id_ in test_ids]

    lang_dir = HF_PATH / lang
    lang_dir.mkdir(exist_ok=True)
    json.dump(train, (lang_dir / "train.jsonl").open("w"))
    json.dump(test, (lang_dir / "test.jsonl").open("w"))
