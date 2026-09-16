class Node:
    def __init__(self, name, is_directory, parent=None):
        self.name = name
        self.is_directory = is_directory
        self.parent = parent
        self.children = []