import sqlite3
import pandas as pd

DB_PATH = "DATA/intelligence_platform.db"


def get_all_incidents():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        """
        SELECT
            id,
            date,
            incident_type,
            severity,
            status,
            description,
            reported_by
        FROM cyber_incidents
        ORDER BY id DESC
        """,
        conn
    )
    conn.close()
    return df


def create_incident(
    incident_type,
    severity,
    status,
    description,
    date,
    reported_by="system"
):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO cyber_incidents
        (date, incident_type, severity, status, description, reported_by)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (date, incident_type, severity, status, description, reported_by)
    )

    conn.commit()
    conn.close()
