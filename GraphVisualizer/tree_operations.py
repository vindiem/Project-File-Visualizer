import node as Node

# every suffix and directory name are being included so far
def build_tree(path):
    node = Node.Node(path.name, path.is_dir())

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

