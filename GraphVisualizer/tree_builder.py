import node as Node

def build_tree(path):
    node = Node.Node(path.name, path.is_dir(), path)

    if path.is_dir():
        for item in path.iterdir():
            child = build_tree(item)
            node.children.append(child)
            child.parent = node

    return node