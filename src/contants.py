import os
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).parent.parent

DATA_PATH = ROOT / "data"

load_dotenv(ROOT / ".env")

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_URL = os.getenv("MONGO_URL")
MONGO_ENDPOINT = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_URL}"
