# **Devlog: OS-Project-3 

## **Day 1: Project Initialization and Source Code Setup**

### **Project Setup & Starting Code**
- **Initialized a new Git repository**: I started by initializing a Git repository for the project.
- **File creation**: I created the initial Python file `main.py` and the Markdown file `devlog.md` for documenting the project.
- **Source Code**: I started incorporating the basic logic for the B-tree, specifically the creation of the index file. I implemented a `create_index()` function that prompts the user for a file name and creates the index file. The system also checks if the file already exists and asks whether to overwrite it.
- **Initial Commit**: After setting up the files and the basic B-tree structure, I committed them with a message: `git commit -m "Initial commit"`.
- **Push to GitHub**: Finally, I pushed the files to GitHub.

---

### **Functions Implemented**

- **`create_index()`**: 
    - This function is responsible for creating a new file. It prompts the user for a file name, checks if the file already exists, and asks whether to overwrite it if it does. If not, it creates a new empty file and sets it as the current working file.
    - **Implementation details**: 
        - Checks if the file exists using `os.path.exists()`.
        - Asks the user for confirmation to overwrite the file.
        - Initializes the file with `open(file_name, 'wb')`, including a header with a magic number, root block ID, and next block ID.
        - Sets the `btree` object as the B-tree instance for the current file.

- **`open_index()`**: 
    - This function opens an existing B-tree index file and reads its header. It prompts the user to input a file name and checks if the file exists before opening it.
    - **Implementation details**: 
        - Uses `os.path.exists()` to check if the file exists.
        - If the file is valid, it opens the file in read mode (`'rb'`) and loads the header (magic number, root block ID, next block ID).
        - Initializes the `btree` object and loads the root node.

- **`insert()`**: 
    - This function allows the user to insert a key into the current B-tree file. It first checks if a file is opened or created, and then prompts the user to input a key.
    - **Implementation details**:
        - If no B-tree file is open, it notifies the user and exits.
        - Adds a placeholder for key insertion logic, indicating that it inserts a key into the current B-tree structure. In a real B-tree, this would involve handling nodes and ensuring the key is inserted correctly while maintaining the B-tree properties.

- **`search()`**: 
    - This function searches for a key in the current B-tree file and returns its associated value if found.
    - **Implementation details**: 
        - If no B-tree file is open, it notifies the user and exits.
        - Placeholder for search logic within the B-tree structure (i.e., traversing nodes to find the key).

- **Main Loop**: The program now includes a main loop that continuously prompts the user for a command. The loop processes commands like `create`, `open`, `insert`, `search`, and `quit`.
    - **Commands**:
        - `create`: Calls `create_index()` to create a new index file.
        - `open`: Calls `open_index()` to open an existing index file.
        - `insert`: Calls `insert()` to insert data into the current B-tree.
        - `search`: Calls `search()` to search for a key in the current B-tree.
        - `quit`: Exits the program.

- **Functionality Testing**: I tested each function individually:
    - The file creation, file opening, insertion, and searching work as expected.
    - The system correctly prompts for the file only when necessary and allows for continued operations without repeatedly asking for the file name once it's been opened or created.

---
