import json

from src.constants import DATA_PATH


class Dataset:
    def __init__(self, name: str) -> None:
        self._name = name
        self._path = DATA_PATH / f"{name}.json"

        if self._path.exists():
            self._data = json.load(self._path.open())
        else:
            self._data = {}

    @property
    def ids(self):
        return list(self._data.keys())
    
    @property
    def texts(self):
        return list(self._data.values())
    
    def add(self, id: int, data: dict) -> None:
        self._data[id] = data
    
    def save(self) -> None:
        json.dump(self._data, self._path.open("w"), ensure_ascii=False, indent=4)

    def __len__(self) -> int:
        return len(self._data)
    
    def __iter__(self):
        return iter(self._data.items())

    def __contains__(self, id) -> bool:
        return id in self._data
