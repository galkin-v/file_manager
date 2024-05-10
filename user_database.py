import os
import json

with open('/Users/vladimir/Documents/VS_Code/HW/Practucums/file_manager/root_dir', mode='r') as f:
        root_dir = f.read()
USER_DB_FILE = f"{root_dir}/user_database.json"

user_database = {}

def load_user_database():
    global user_database
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, 'r') as f:
            user_database = json.load(f)
            return user_database

def save_user_database():
    with open(USER_DB_FILE, 'w') as f:
        json.dump(user_database, f)

def register_user(username, dir):
    if username not in user_database:
        user_database[username] = username.lower()  # Personal directory name same as username
        os.mkdir(dir)  # Create personal directory for the user
        print(f"User '{username}' registered successfully.")
        save_user_database()
    else:
        print(f"User '{username}' already exists.")

def get_user_root(username):
    if username in user_database:
        return f'{root_dir}/{user_database[username]}'
    else:
        return None
