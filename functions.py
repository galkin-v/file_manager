import os
import shutil
import subprocess
import zipfile

with open('/Users/vladimir/Documents/VS_Code/HW/Practucums/file_manager/root_dir', mode='r') as f:
    root_dir = f.read()

def esc(code):
    return f'\033[{code}m'

def list_files():
    files = os.listdir()
    max_length = max(len(file) for file in files) if files else 0
    if max_length > 40:
        max_length = 40  # Limit max length for better formatting
    line = '-' * (max_length + 2)  # Length of the line separator
    print(f'╔{line}╗')
    for file in files:
        print(f'║ {file.ljust(max_length)} ║')
    print(f'╚{line}╝')

def create_directory():
    dir_name = input('Enter directory name: ')
    os.mkdir(dir_name)
    print(f'Directory "{dir_name}" created successfully.')

def delete_directory():
    dir_name = input('Enter directory name to delete: ')
    try:
        os.rmdir(dir_name)
        print(f'Directory "{dir_name}" deleted successfully.')
    except OSError as e:
        print(f'Error: {e}')

def navigate_directory():
    target_dir = input('Enter directory name to navigate: ')
    new_dir = os.path.abspath(os.path.join(os.getcwd(), target_dir))
    if new_dir.startswith(root_dir):
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            print(f'Navigated to directory "{new_dir}".')
        else:
            print(f'Directory "{target_dir}" does not exist.')
    else:
        print(f'Cannot navigate outside the root directory.')

def navigate_down():
    current_dir = os.getcwd()
    if current_dir == root_dir:
        return "You are already at the root directory."
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir)
    print(f'Navigated down to directory "{parent_dir}".')

def create_file():
    file_name = input('Enter file name to create: ')
    with open(file_name, 'w') as file:
        pass
    print(f'File "{file_name}" created successfully.')

def read_file():
    file_name = input('Enter file name to read: ')
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'Error: File "{file_name}" not found.')

def write_to_file():
    file_name = input('Enter file name to write to: ')
    content = input('Enter content: ')
    with open(file_name, 'w') as file:
        file.write(content)
    print(f'Content written to file "{file_name}" successfully.')

def delete_file():
    file_name = input('Enter file name to delete: ')
    try:
        os.remove(file_name)
        print(f'File "{file_name}" deleted successfully.')
    except FileNotFoundError:
        print(f'Error: File "{file_name}" not found.')

copied_file = {}  # Dictionary to store copied file temporarily

def copy_file():
    global copied_file
    src_file = input('Enter source file name: ')
    try:
        with open(src_file, 'rb') as file:
            copied_file = {
                'name': src_file,
                'content': file.read()
            }
        print(f'File "{src_file}" copied successfully.')
    except FileNotFoundError:
        print(f'Error: File "{src_file}" not found.')

def paste_file():
    global copied_file
    if copied_file:
        try:
            with open(copied_file['name'], 'wb') as file:
                file.write(copied_file['content'])
            print(f'File "{copied_file["name"]}" pasted to current directory successfully.')
        except FileNotFoundError:
            print(f'Error: Failed to paste file "{copied_file["name"]}".')
    else:
        print('Error: No file has been copied.')

def move_file():
    src_file = input('Enter source file name: ')
    dest_dir = input('Enter destination directory name: ')
    try:
        shutil.move(src_file, dest_dir)
        print(f'File "{src_file}" moved to directory "{dest_dir}" successfully.')
    except FileNotFoundError:
        print(f'Error: File "{src_file}" not found.')

def rename_file():
    old_name = input('Enter current file name: ')
    new_name = input('Enter new file name: ')
    try:
        os.rename(old_name, new_name)
        print(f'File "{old_name}" renamed to "{new_name}" successfully.')
    except FileNotFoundError:
        print(f'Error: File "{old_name}" not found.')

def navigate_to_folder(folder_name):
    if os.path.isdir(folder_name):
        os.chdir(folder_name)
    else:
        return f'{esc(31)}There is no such command or folder.{esc(0)}'

def open_file():
    file_name = input('Enter file name to open: ')
    try:
        subprocess.run(['open', file_name], check=True)
    except subprocess.CalledProcessError:
        print(f'Error: Failed to open file "{file_name}".')

def archive_files():
    files = input("Enter files or directories to archive (separated by comma): ").split(',')
    archive_name = input("Enter the name of the archive file: ")
    with zipfile.ZipFile(archive_name, 'w') as zipf:
        for f in files:
            zipf.write(f)
    print(f'Files archived successfully into {archive_name}')

def unarchive_files():
    archive_name = input("Enter the name of the archive file: ")
    extract_to = input("Enter the directory to extract to: ")
    with zipfile.ZipFile(archive_name, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f'Files extracted successfully from {archive_name} to {extract_to}')

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return total, used, free

def print_disk_usage():
    total, used, free = get_disk_usage()
    print(f"Total disk space: {total} bytes")
    print(f"Used disk space: {used} bytes")
    print(f"Free disk space: {free} bytes")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print('')
    print('')
    print('[q] Quit     [.] Navigate Down     [md] Create Directory     [rm] Delete Directory')
    print('[rf] Read File     [wf] Write to File     [op] Open File     [mv] Move File     [df] Delete File')
    print('[cp] Copy File     [pt] Paste File     [rn] Rename File     [cd] Navigate Directory')
    print('[arc] Archive Files     [uar] Unarchive Files     [du] Disk Usage')