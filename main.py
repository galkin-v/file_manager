# main_file_manager.py

import os
import shutil
from functions import *
from user_database import load_user_database, save_user_database, register_user, get_user_root

def main():
    clear()
    current_output = ''

    user_database = load_user_database()  # Load user database
    with open('/Users/vladimir/Documents/VS_Code/HW/Practucums/file_manager/root_dir', mode='r') as f:
        root_dir = f.read()
    
    # Prompt user for username or registration
    while True:
        print("Welcome to the File Manager!")
        print("Enter your username or type 'reg' to register a new username:")
        username = input()
        if username == 'reg':
            new_username = input("Enter a new username: ")
            root_dir += f'/{new_username}'
            register_user(new_username, root_dir)
        elif username in user_database:
            print(f"Welcome back, {username}!")
            root_dir = get_user_root(username)
            os.chdir(root_dir)  # Set current working directory to user's personal directory
            break
        else:
            print("Invalid username. Please try again or register a new username.")
    
    # Main file manager loop
    while True:
        print(f'{esc(33)}Current directory: {os.getcwd()}{esc(0)}')
        list_files()
        print_menu()
        print(current_output)

        command = input()
        if command == 'q':
            break
        elif command == '.':
            if navigate_down() is not None:
                current_output = navigate_down()
            else:
                current_output = ''
        elif command == 'md':
            create_directory()
        elif command == 'rm':
            delete_directory()
        elif command == 'rf':
            read_file()
        elif command == 'wf':
            write_to_file()
        elif command == 'op':
            open_file()
        elif command == 'mv':
            move_file()
        elif command == 'df':
            delete_file()
        elif command == 'cp':
            copy_file()
        elif command == 'pt':
            paste_file()
        elif command == 'rn':
            rename_file()
        elif command == 'cd':
            navigate_directory()
        elif command == 'arc':
            archive_files()
        elif command == 'uar':
            unarchive_files()
        elif command == 'du':
            current_output = f'{get_disk_usage()}'
        else:
            if navigate_to_folder(command) is not None:
                current_output = navigate_to_folder(command)
            else:
                current_output = ''
        clear()

    save_user_database()  # Save user database before exiting

if __name__ == "__main__":
    main()
