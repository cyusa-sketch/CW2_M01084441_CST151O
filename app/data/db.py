import sqlite3
from pathlib import Path

# the base folder for the database file
BASE_FOLDER = Path(__file__).resolve().parents[2] / "DATA"
BASE_FOLDER.mkdir(parents=True, exist_ok=True)

DB_FILE = BASE_FOLDER / "intelligence_platform.db"


# opening the database connection
def connect_database(path: Path = DB_FILE):
    """
    Opens (or creates) the SQLite database file.
    Returns a ready-to-use sqlite3 connection.
    """
    db = sqlite3.connect(str(path))

    # Allow column access by name
    db.row_factory = sqlite3.Row

    # Important: turn on foreign key constraints
    db.execute("PRAGMA foreign_keys = ON;")

    return db
