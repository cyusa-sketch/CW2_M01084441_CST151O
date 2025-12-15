import sqlite3

# the table for user accounts
def build_users_table(db):
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            username     TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role         TEXT DEFAULT 'user',
            created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.commit()


# the table for cyber incidents
def build_incidents_table(db):
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            date          TEXT,
            incident_type TEXT,
            severity      TEXT,
            status        TEXT,
            description   TEXT,
            reported_by   TEXT,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            FOREIGN KEY (reported_by)
              REFERENCES users(username)
              ON DELETE SET NULL
        )
    """)
    db.commit()


# a code block for creating the datasets metadata table
def build_metadata_table(db):
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_name   TEXT NOT NULL,
            category       TEXT,
            source         TEXT,
            last_updated   TEXT,
            record_count   INTEGER,
            file_size_mb   REAL,
            created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.commit()



#  the it tickets table

def build_tickets_table(db):
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id     TEXT UNIQUE NOT NULL,
            priority      TEXT,
            status        TEXT,
            category      TEXT,
            subject       TEXT NOT NULL,
            description   TEXT,
            created_date  TEXT,
            resolved_date TEXT,
            assigned_to   TEXT,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.commit()


# creating all tables with a single function
def create_all_tables(db):
    """
    Runs all table creation functions in a single call.
    """
    build_users_table(db)
    build_incidents_table(db)
    build_metadata_table(db)
    build_tickets_table(db)
