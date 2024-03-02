import os
import sys

def create_file(filename):
    try:
        # Function for creating a new file. Eg: `>create {fileName}`.
        with open(filename, 'w') as file:
            print("File created successfully")
    except FileNotFoundError:
        print("File already exists")
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print(f"An error occured: {e}")

def edit_file(filename):
    try:
        # Function for editing the file. Eg: `>edit {fileName}`.
        with open(filename, 'r+') as file:
            content = file.read()
            print("Current content:\n", content)
            new_content = input("Enter new content:\n")
            file.seek(0)
            file.write(new_content)
            file.truncate()
            print()
            print("File edited successfully!")
    except FileNotFoundError:
        print("File does not exist!")
    except Exception as e:
        print(f"An error occured: {e}")

def main(args):
    if len(args) < 2:
        print("Usage: python text_editor.py <option> <filename> [content]")
        return

    option = args[1]
    filename = args[2]

    if option == 'create':
        create_file(filename)
    elif option == 'edit':
        edit_file(filename)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main(sys.argv)