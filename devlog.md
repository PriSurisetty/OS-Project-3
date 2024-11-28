# **Devlog: OS-Project-3 - Initial Setup and Source Code Development**

## **Day 1: Project Initialization and Source Code Setup**

### **Project Setup & Starting Code**
- **Initialized a new Git repository**: I started by initializing a Git repository for the project.
- **File creation**: I created the initial Python file `main.py` and the Markdown file `devlog.md` for documenting the project.
- **Source Code**: I got started on the source code, making a `create()` function to trigger when the user types in a command; my approach is to go one at a time. I forgot to include information in my devlog file for the first commit.
- **Initial Commit**: After setting up the files, I committed them with a message: `git commit -m "Initial commit"`.
- **Push to GitHub**: Finally, I pushed the files to GitHub.

---

### **Functions Implemented**
- **`create_index()`**: 
    - This function is responsible for creating a new file. It prompts the user for a file name, checks if the file already exists, and asks whether to overwrite it if it does. If not, it creates a new empty file and sets it as the current working file.
    - **Implementation details**: 
        - Checks if the file exists using `os.path.exists()`.
        - Asks the user for confirmation to overwrite the file.
        - Initializes the file with `open(file_name, 'w')`.
        - Sets the `current_file` global variable to the newly created file.

- **`open_index()`**: 
    - This function opens an existing file and reads its contents. It prompts the user to input a file name and checks if the file exists before opening it.
    - **Implementation details**: 
        - Uses `os.path.exists()` to check if the file exists.
        - If the file is valid, it opens the file in read mode (`'r'`) and sets the `current_file` variable.
  
- **`insert()`**: 
    - This function allows the user to insert a key-value pair into the current file. It first checks if a file is opened or created, and then prompts the user to input a key and a value.
    - **Implementation details**:
        - If no file is open, it notifies the user and exits.
        - Appends the key-value pair to the current file using `open(current_file, 'a')`.
  
- **`search()`**: 
    - This function searches for a key in the current file and returns its associated value if found.
    - **Implementation details**: 
        - If no file is open, it notifies the user and exits.
        - Reads the file and checks if any line starts with the given key, then prints the corresponding value.

---

- **Main Loop**: The program now includes a main loop that continuously prompts the user for a command. The loop processes commands like `create`, `open`, `insert`, `search`, and `quit`.
    - Commands:
        - `create`: Calls `create_index()` to create a new file.
        - `open`: Calls `open_index()` to open an existing file.
        - `insert`: Calls `insert()` to insert data into the current file.
        - `search`: Calls `search()` to search for a key in the current file.
        - `quit`: Exits the program.

- **Functionality Testing**: I tested each function individually:
    - The file creation, file opening, insertion, and searching work as expected.
    - The system correctly prompts for the file only when necessary and allows for continued operations without repeatedly asking for the file name once it's been opened or created.

---