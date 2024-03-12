from deep_translator import GoogleTranslator
from tqdm import tqdm

from fire import Fire
from src.data import Dataset


def main(lang="en"):
    translator = GoogleTranslator(source="pt", target=lang)

    source_ds = Dataset("pt")
    target_ds = Dataset(lang)
    for id, text in source_ds:
        if id not in target_ds:
            if len(text) <= 5000:
                try:
                    translated = translator.translate(text)
                    target_ds.add(id, translated)
                except Exception as e:
                    target_ds.save()
                    print(f"Error translating text og id {id}.")
                    print(e)


if __name__ == "__main__":
    main()
