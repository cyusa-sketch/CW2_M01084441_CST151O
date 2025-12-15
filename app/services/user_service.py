import bcrypt
from pathlib import Path

# users.txt location
DATA_DIR = Path(__file__).resolve().parents[2] / "DATA"
USERS_FILE = DATA_DIR / "users.txt"

DATA_DIR.mkdir(exist_ok=True)
USERS_FILE.touch(exist_ok=True)



# register a new user

def register_user(username: str, password: str):
    username = username.strip()

    if not username or not password:
        return False, "Username and password are required."

    # check if user already exists
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 1 and parts[0] == username:
                return False, "Username already exists."

    # hash password with bcrypt
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # save user (username, hashed_password, role)
    with open(USERS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed_pw},user\n")

    return True, "Account created successfully."



# loggin existing user

def login_user(username: str, password: str):
    username = username.strip()

    if not username or not password:
        return False, "Username and password are required."

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")

            # must be exactly: username, hash, role
            if len(parts) != 3:
                continue

            stored_user, stored_hash, role = parts

            if stored_user == username:
                if bcrypt.checkpw(password.encode(), stored_hash.encode()):
                    return True, "Login successful"
                else:
                    return False, "Invalid username or password"

    return False, "User not found"
