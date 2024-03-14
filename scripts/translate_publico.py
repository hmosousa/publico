from fire import Fire
from tqdm import tqdm

from src.data import Dataset
from src.translator import Translator


def main(lang="es"):
    translator = Translator(source="pt", target=lang)

    source_ds = Dataset("pt")
    target_ds = Dataset(lang)
    for id_, text in tqdm(source_ds):
        if id_ not in target_ds:
            try:
                translate = translator.translate(text)
                target_ds.add(id_, translate)
            except Exception as e:
                print(f"Error translating {id_}: {e}")
            target_ds.save()


if __name__ == "__main__":
    Fire(main)
