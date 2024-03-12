from deep_translator import GoogleTranslator
from fire import Fire

from src.data import Dataset


def main(lang="en"):
    translator = GoogleTranslator(source="pt", target=lang)

    source_ds = Dataset("pt")
    target_ds = Dataset(lang)

    ids = source_ds.ids
    texts = source_ds.texts

    translated = translator.translate_batch(texts)
    for id, translation in zip(ids, translated):
        target_ds.add(id, translation)
    target_ds.save()


if __name__ == "__main__":
    Fire(main)
