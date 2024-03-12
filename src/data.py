from pathlib import Path
from typing import Optional

from torch.utils.data import Dataset

from src.contants import PARSED_PATH, TRANSLATED_PATH, TRANSLATE_TOKEN


class TranslationDataset(Dataset):
    def __init__(
            self, 
            data_path: Path = PARSED_PATH, 
            translated_path: Path = TRANSLATED_PATH, 
            split: Optional[str] = None,
        ):
        self.data_path = data_path
        self.translated_path = translated_path

        self.pt = []
        self.en = []

        self._load_data()

        if split == "train":
            self.pt = self.pt[:int(len(self.pt) * 0.9)]
            self.en = self.en[:int(len(self.en) * 0.9)]
        elif split == "test":
            self.pt = self.pt[int(len(self.pt) * 0.9):]
            self.en = self.en[int(len(self.en) * 0.9):]

    def _load_data(self) -> None:
        for fp in self.translated_path.glob("*.txt"):
            self.en.append(fp.read_text())
            self.pt.append((self.data_path / fp.name).read_text())

    def __len__(self):
        return len(self.pt)

    def __getitem__(self, idx: int):
        text = f"{self.en[idx]}{TRANSLATE_TOKEN}{self.pt[idx]}"
        return text
