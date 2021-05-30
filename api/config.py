import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_FILE = BASE_DIR / 'hospital.db'
SERVICES_FILE = BASE_DIR / 'researches.txt'
