from src.db import Database

class TestDatabase:

    def test_init(self):
        db = Database("test")
        assert db._lang == "test"
    
    def test_insert_get(self):
        db = Database("test")
        db.insert({"id": 1, "text": "test"})
        assert db.get(1)["text"] == "test"
        del db

    def test_iter(self):
        db = Database("test")
        db.insert({"id": 1, "text": "test"})
        db.insert({"id": 2, "text": "test2"})
        assert len(list(db)) == 2
        del db