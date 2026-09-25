from pathlib import Path

class Node:
    def __init__(self, 
                 name, 
                 is_directory, 
                 path,
                 parent=None):
        self.name = name
        self.is_directory = is_directory
        self.path = Path(path)
        self.parent = parent
        
        self.children = []
        self.suffix = Path(name).suffix.lower()
    