from app.data.db import connect_database


# getting a ticket from the csv file and inserting into the database
def migrate_tickets_from_file(path="DATA/it_tickets.csv"):
    """
    Reads the CSV file for IT tickets and inserts entries into
    the it_tickets table if they are not already present.
    """
    db = connect_database()
    cur = db.cursor()

    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                parts = line.strip().split(",")
                if len(parts) < 8:
                    continue  # ignore broken lines

                (
                    t_id,
                    pri,
                    stat,
                    cat,
                    subj,
                    desc,
                    created_on,
                    assigned,
                ) = parts

                cur.execute(
                    """
                    INSERT OR IGNORE INTO it_tickets
                    (ticket_id, priority, status, category, subject, description, created_date, assigned_to)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (t_id, pri, stat, cat, subj, desc, created_on, assigned)
                )

    except FileNotFoundError:
        print(f"[tickets] Could not find file: {path}")

    db.commit()
    db.close()


# adding a new ticket into the database
def insert_ticket(ticket_id, priority, status, category, subject, description, created_date, assigned_to=None):
    db = connect_database()
    cur = db.cursor()

    cur.execute(
        """
        INSERT INTO it_tickets
        (ticket_id, priority, status, category, subject, description, created_date, assigned_to)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (ticket_id, priority, status, category, subject, description, created_date, assigned_to)
    )

    db.commit()
    new_id = cur.lastrowid
    db.close()
    return new_id


# getting all tickets
def get_all_tickets():
    db = connect_database()
    cur = db.cursor()

    cur.execute("SELECT * FROM it_tickets ORDER BY id DESC")
    data = cur.fetchall()

    db.close()
    return data


# updating the status of a ticket
def update_ticket_status(ticket_id, new_status):
    db = connect_database()
    cur = db.cursor()

    cur.execute(
        "UPDATE it_tickets SET status = ? WHERE ticket_id = ?",
        (new_status, ticket_id)
    )

    db.commit()
    updated = cur.rowcount
    db.close()
    return updated
