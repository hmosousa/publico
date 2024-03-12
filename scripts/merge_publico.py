import json

from src.constants import DATA_PATH


def main():
    parsed_path = DATA_PATH / "parsed"
    transl_path = DATA_PATH / "translated"

    data = []
    for ps_fp in parsed_path.glob("*.txt"):
        filename = ps_fp.stem
        original = json.load(ps_fp.open())
        translated = json.load((transl_path / f"{filename}.txt").open())



        out_fp = parsed_path / f"{in_fp.stem}.txt"
        out_fp.write_text(content["texto"])


if __name__ == "__main__":
    main()
