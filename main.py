import os

BLOCK_SIZE = 512
MAGIC_NUMBER = b"4337PRJ9"
MIN_DEGREE = 10
MAX_KEYS = 2 * MIN_DEGREE - 1

current_file = None
btree = None

class BTreeNode:
    def __init__(self, block_id, is_leaf=True):
        self.block_id = block_id
        self.is_leaf = is_leaf
        self.keys = []
        self.values = []
        self.children = []

class BTree:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = None
        self.next_block_id = 1

    def create(self):
        with open(self.file_path, 'wb') as f:
            magic = MAGIC_NUMBER
            root_block_id = (0).to_bytes(8, 'big')
            next_block_id = (1).to_bytes(8, 'big')
            header = magic + root_block_id + next_block_id
            f.write(header.ljust(BLOCK_SIZE, b'\x00'))
        print("Index file created successfully.")

    def load_header(self):
        with open(self.file_path, 'rb') as f:
            header = f.read(BLOCK_SIZE)
            if header[:8] != MAGIC_NUMBER:
                raise ValueError("Invalid index file.")
            root_block_id = int.from_bytes(header[8:16], 'big')
            self.next_block_id = int.from_bytes(header[16:24], 'big')
            if root_block_id != 0:
                self.root = BTreeNode(root_block_id)

    def print_tree(self):
        if self.root is None:
            print("The B-tree is empty.")
            return
        print("B-Tree contents:")
        for key, value in zip(self.root.keys, self.root.values):
            print(f"Key = '{key}', Value = '{value}'")

    def search(self, key):
        if self.root is None:
            return None
        if key in self.root.keys:
            index = self.root.keys.index(key)
            return self.root.values[index]
        return None

    def extract(self, file_name):
        if not self.root:
            print("The B-tree is empty. Nothing to extract.")
            return

        if os.path.exists(file_name):
            overwrite = input(f"File {file_name} already exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite != 'yes':
                print("File not overwritten.")
                return

        with open(file_name, 'w') as f:
            for key, value in zip(self.root.keys, self.root.values):
                f.write(f"{key},{value}\n")
        print(f"Key-value pairs extracted to {file_name}.")

def create_index():
    global btree
    file_name = input("Enter file name to create: ").strip()

    if os.path.exists(file_name):
        overwrite = input("File already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != 'yes':
            print("File not created.")
            return

    btree = BTree(file_name)
    btree.create()

def open_index():
    global btree
    file_name = input("Enter file name to open: ").strip()

    if not os.path.exists(file_name):
        print(f"{file_name} does not exist.")
        return

    btree = BTree(file_name)
    btree.load_header()

    with open(file_name, 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            if line.strip():
                key, value = line.strip().split(',')
                if btree.root is None:
                    btree.root = BTreeNode(1)
                btree.root.keys.append(key)
                btree.root.values.append(value)

    print(f"Index file {file_name} opened and content loaded successfully.")

def load():
    global btree
    if btree is None:
        print("No B-tree file is open. Please create or open a file first.")
        return

    file_name = input("Enter the text file name to load from: ").strip()

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    key_value = line.split(',')
                    if len(key_value) == 2:
                        key, value = key_value[0].strip(), key_value[1].strip()
                        if btree.search(key):  # Check if key already exists
                            print(f"!! Key '{key}' already exists !!")
                        else:
                            btree.add(key, value)  # Use 'add' instead of 'insert' if required
            print(f"Data from '{file_name}' loaded into the B-tree successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")

def insert():
    global btree
    if btree is None:
        print("No B-tree file is open. Please create or open a file first.")
        return

    key = input("Enter key to insert: ").strip()
    value = input("Enter value to insert: ").strip()

    if btree.root is None:
        btree.root = BTreeNode(1)

    if key in btree.root.keys:
        print(f"!! Key '{key}' already exists !!")
        return

    btree.root.keys.append(key)
    btree.root.values.append(value)
    print(f"Inserted '{value}' at key '{key}'.")

    with open(btree.file_path, 'a') as f:
        f.write(f"{key},{value}\n")

def quit_program():
    print("Exiting the program.")
    exit(0)

# Main menu
def print_menu():
    print("\n==============================================")
    print("  B-Tree Management System")
    print("==============================================")
    print(" [1] Create a new index file")
    print(" [2] Open an existing index file")
    print(" [3] Insert a key-value pair")
    print(" [4] Load data from a text file into the B-tree")
    print(" [5] Search for a key in the B-tree")
    print(" [6] Extract all key-value pairs to a file")
    print(" [7] Print B-tree contents")
    print(" [8] Quit the program")
    print("==============================================")

while True:
    print_menu()
    user_input = input("\nEnter your choice (1-8): ").strip()

    if user_input == '1':
        create_index()
    elif user_input == '2':
        open_index()
    elif user_input == '3':
        insert()
    elif user_input == '4':
        load()
    elif user_input == '5':
        if btree is None:
            print("No B-tree file is open. Please create or open a file first.")
        else:
            key = input("Enter key to search for: ").strip()
            result = btree.search(key)
            if result:
                print(f"Found key '{key}' with value '{result}'.")
            else:
                print(f"Key '{key}' not found.")
    elif user_input == '6':
        if btree is None:
            print("No B-tree file is open. Please create or open a file first.")
        else:
            file_name = input("Enter the file name to extract to: ").strip()
            btree.extract(file_name)
    elif user_input == '7':
        if btree is None:
            print("No B-tree file is open. Please create or open a file first.")
        else:
            btree.print_tree()
    elif user_input == '8':
        quit_program()
    else:
        print("Invalid input. Please try again.")
