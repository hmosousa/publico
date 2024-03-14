from deep_translator import GoogleTranslator
from fire import Fire
from tqdm import tqdm

from src.data import Dataset


def main(lang="en"):
    translator = GoogleTranslator(source="pt", target=lang)

    source_ds = Dataset("pt")
    target_ds = Dataset(lang)
    for id_, text in tqdm(source_ds):
        if id_ not in target_ds:    
            try:
                
                if len(text) > 5000:
                    translate = []
                    for sentence in text.split("\n"):
                        translate.append(translator.translate(sentence))
                    translate = "\n".join(translate)
                
                else:
                    translate = translator.translate(text)
                
                target_ds.add(id_, translate)
            except Exception as e:
                print(f"Error translating {id_}: {e}")
            target_ds.save()


if __name__ == "__main__":
    Fire(main)
