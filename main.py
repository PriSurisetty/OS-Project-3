import os

BLOCK_SIZE = 512
MAGIC_NUMBER = b"4337PRJ9"
MIN_DEGREE = 10
MAX_KEYS = 2 * MIN_DEGREE - 1

# Initialize current file
current_file = None
btree = None  # Hold the B-tree instance once it's created


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
        self.next_block_id = 1  # Start from block 1 after header

    def create(self):
        """Create the B-tree header and file"""
        with open(self.file_path, 'wb') as f:
            # Write magic number, root block id (0 initially), and next block id
            magic = MAGIC_NUMBER
            root_block_id = (0).to_bytes(8, 'big')
            next_block_id = (1).to_bytes(8, 'big')  # Next block id after header
            header = magic + root_block_id + next_block_id
            f.write(header.ljust(BLOCK_SIZE, b'\x00'))
        print("Index file created successfully.")

    def load_header(self):
        """Load the header from the index file"""
        with open(self.file_path, 'rb') as f:
            header = f.read(BLOCK_SIZE)
            if header[:8] != MAGIC_NUMBER:
                raise ValueError("Invalid index file.")
            root_block_id = int.from_bytes(header[8:16], 'big')
            self.next_block_id = int.from_bytes(header[16:24], 'big')
            if root_block_id != 0:
                self.root = self.load_node(root_block_id)

    def load_node(self, block_id):
        """Load a node (dummy implementation for now)"""
        # In reality, we'd read node data from file using block_id
        return BTreeNode(block_id)


def create_index():
    """Function to create a new B-tree index file"""
    global btree
    # Ask user for file name
    file_name = input("Enter file name to create: ").strip()

    # If the file already exists, ask if they want to overwrite
    if os.path.exists(file_name):
        overwrite = input("File already exists. Overwrite? (yes/no): ").strip().lower()
        if overwrite != 'yes':
            print("File not created.")
            return

    # Create B-tree and index file
    btree = BTree(file_name)
    btree.create()


def open_index():
    """Function to open an existing B-tree index file"""
    global btree
    file_name = input("Enter file name to open: ").strip()

    if not os.path.exists(file_name):
        print(f"{file_name} does not exist.")
        return

    # Open and load B-tree from file
    btree = BTree(file_name)
    btree.load_header()
    print(f"Index file {file_name} opened successfully.")


def insert():
    """Insert a key into the current B-tree file"""
    global btree

    # If no B-tree file is open, prompt to open or create one
    if btree is None:
        print("No B-tree file is open. Please create or open a file first.")
        return

    # Ask for key + value to insert
    key = input("Enter key to insert: ").strip()
    value = input("Enter value to insert: ").strip()
    # Placeholder for insertion logic (usually depends on B-tree structure)
    print(f"Inserted '{value}' at key '{key}'.")


def quit_program():
    """Quit the program"""
    print("Exiting the program.")
    exit(0)


# User commands
while True:
    user_input = input("Which command? (create/open/insert/quit): ").strip().lower()

    if user_input == 'create':
        create_index()
    elif user_input == 'open':
        open_index()
    elif user_input == 'insert':
        insert()
    elif user_input == 'quit':
        quit_program()
    else:
        print("Invalid command. Please type 'create', 'open', 'insert', or 'quit'.")
