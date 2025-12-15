from app.data.db import connect_database


# getting a user according to their username
def get_user_by_username(name: str):
    """
    Returns a full user row from the 'users' table,
    or None if no matching username is found.
    """
    db = connect_database()
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username = ?",
        (name,)
    )

    record = cur.fetchone()
    db.close()
    return record


# adding a new user to the database
def insert_user(name: str, hashed_pass: str, role: str = "user"):
    """
    Creates a new user entry.
    Returns the auto-generated id of the inserted row.
    """
    db = connect_database()
    cur = db.cursor()

    cur.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (name, hashed_pass, role)
    )

    db.commit()
    user_id = cur.lastrowid
    db.close()
    return user_id


# getting the list of all users with their details
def list_users():
    """
    Returns a list of user rows for display purposes.
    """
    db = connect_database()
    cur = db.cursor()

    cur.execute(
        "SELECT id, username, role, created_at FROM users ORDER BY id"
    )

    info = cur.fetchall()
    db.close()
    return info
