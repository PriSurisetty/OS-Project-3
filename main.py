import os


def create_index():
    # Ask user for file name
    file_name = input("Enter file name: ").strip()

    # If the file already exists, ask the user if they want to overwrite the file
    if os.path.exists(file_name):
        overwrite = input("File already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != 'yes':
            print("File not created.")
            return

    # Create the file
    try:
        with open(file_name, 'w') as file:
            file.write("") 
        print(f"{file_name} created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")


user_input = input("Which command? : ")
if user_input:
    create_index()

