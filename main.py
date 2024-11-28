import os

# Variable to store the current file name
current_file = None


def create_index():
    global current_file
    # Ask user for file name
    file_name = input("Enter file name: ").strip()

    # If the file already exists, ask the user if they want to overwrite the file
    if os.path.exists(file_name):
        overwrite = input("File already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != 'yes':
            print("File not created.")
            return
    try:
        with open(file_name, 'w') as file:
            file.write("")  # Initialize an empty file
        current_file = file_name  # Set the current file
        print(f"{file_name} created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")


# Open an existing file and print its contents
def open_index():
    global current_file
    # Ask user for file name to open
    file_name = input("Enter file name to open: ").strip()

    # If the file exists, open and read the file
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as file:
                print(f"Index {file_name} opened.")
            current_file = file_name  # Set the current file
        except Exception as e:
            print(f"Error opening file: {e}")
    else:
        print(f"{file_name} does not exist.")

# Insert key-value pair into the file


def insert():
    global current_file

    # If no file has been opened or created, ask for a file name
    if current_file is None:
        print("No file has been selected. Please use the 'open' or 'create' command first.")
        return

    key = input("Enter key: ").strip()
    value = input("Enter value: ").strip()

    try:
        # Append the key-value pair to the current file
        with open(current_file, 'a') as file:
            file.write(f"{key}: {value}\n")
        print(f"Inserted '{key}' at key '{value}' into {current_file}")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Search for a key in the file


def search():
    global current_file

    # If no file has been opened or created, ask for a file name
    if current_file is None:
        print("No file has been selected. Please use the 'open' or 'create' command first.")
        return

    key = input("Enter key: ").strip()

    try:
        # Open the current file and search for the key
        with open(current_file, 'r') as file:
            lines = file.readlines()
            found = False
            for line in lines:
                # Check if the key is in the current line
                if line.startswith(f"{key}:"):
                    print(f"Key {key} found with value: {line.strip().split(': ')[1]}")
                    found = True
                    break
            if not found:
                print(f"Key {key} not found in {current_file}.")
    except Exception as e:
        print(f"Error reading file: {e}")


# Main loop to process user commands
while True:
    user_input = input("Which command? (create/open/insert/search/quit): ").strip().lower()

    if user_input == 'create':
        create_index()
    elif user_input == 'open':
        open_index()
    elif user_input == 'insert':
        insert()
    elif user_input == 'search':
        search()
    elif user_input == 'quit':
        print("Exiting the program.")
        break
    else:
        print("Invalid command. Please type 'create', 'open', 'insert', 'search', or 'quit'.")
