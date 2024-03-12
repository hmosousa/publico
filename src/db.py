from pymongo import MongoClient

from src.constants import MONGO_ENDPOINT


class Database:
    def __init__(self, language: str = "en"):
        self._client = MongoClient(MONGO_ENDPOINT)
        self._db = self._client["publico"]
        self._collection = self._db[language]
        self._lang = language
    
    def insert(self, data: dict):
        self._collection.insert_one(data)

    def insert_many(self, data: list):
        self._collection.insert_many(data)

    def get(self, id: int):
        answer = self._collection.find_one({"_id": id})
        return answer

    def delete(self, id: int):
        self._collection.delete_one({"_id": id})

    def __iter__(self):
        return self._collection.find()
    
    def __len__(self):
        return self._collection.count_documents({})
    
    def __del__(self):
        self._db.drop_collection(self._lang)

    def __contains__(self, id: int):
        return bool(self.get(id))
