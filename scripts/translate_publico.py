from deep_translator import GoogleTranslator
from tqdm import tqdm


from src.contants import PARSED_PATH, TRANSLATED_PATH


def main(lang="en"):
    translator = GoogleTranslator(source="pt", target=lang)

    filepaths = list(PARSED_PATH.glob("*.txt"))
    for input_fp in tqdm(filepaths):
        output_fp = TRANSLATED_PATH / f"{input_fp.stem}.txt"
        if not output_fp.exists():
            content = input_fp.read_text()

            if len(content) <= 5000:
                try:
                    translated = translator.translate(content)
                    output_fp.write_text(translated)
                except Exception as e:
                    print(input_fp)
                    print(e)


if __name__ == "__main__":
    main()
