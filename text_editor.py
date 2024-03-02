import os
import sys

def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            print("File created successfully!")
    else:
        print("File already exists!")

def edit_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r+') as file:
            content = file.read()
            print("Current content:\n", content)
            new_content = input("Enter new content:\n")
            file.seek(0)
            file.write(new_content)
            file.truncate()
            print("File edited successfully!")
    else:
        print("File does not exist!")

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print("File saved successfully!")

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
    elif option == 'save':
        if len(args) < 4:
            print("Usage: python text_editor.py save <filename> <content>")
            return
        content = args[3]
        save_file(filename, content)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main(sys.argv)