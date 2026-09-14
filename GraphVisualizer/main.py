from pathlib import Path
import color

path = Path("/Users/alohadance/General/ConsoleApplications/Funki")
root = []

class Node:
    def __init__(self, name, is_directory, parent=None):
        self.name = name
        self.is_directory = is_directory
        self.parent = parent
        self.children = []

# every suffix and directory name are being included so far
def build_tree(path):
    node = Node(path.name, path.is_dir())

    if path.is_dir():
        for item in path.iterdir():
            child = build_tree(item)
            node.children.append(child)
            child.parent = node

    return node

def render_tree(node, prefix=""):
    for index, child in enumerate(node.children):
        is_last = index == len(node.children) - 1
        branch = "└── " if is_last else "├── "

        if child.is_directory:
            print(prefix + branch + child.name + "/")
            new_prefix = prefix + ("    " if is_last else "│   ")
            render_tree(child, new_prefix)

        else:
            print(prefix + branch + child.name)

if __name__ == "__main__":
    # draw_architecture(path)
    root = build_tree(path)
    render_tree(root)
