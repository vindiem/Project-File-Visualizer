from pathlib import Path

class Node:
    def __init__(self, 
                 name, 
                 is_directory, 
                 parent=None, 
                 suffix=""):
        self.name = name
        self.is_directory = is_directory
        self.suffix = Path(name).suffix.lower()
        self.parent = parent
        self.children = []
        
    