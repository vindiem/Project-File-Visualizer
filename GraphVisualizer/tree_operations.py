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
            
def render_tree_ignored(node, ignored_names, ignored_sufficies, prefix=""):
    for index, child in enumerate(node.children):
        is_last = index == len(node.children) - 1
        branch = "└── " if is_last else "├── "
        
        if child.is_directory and child.name not in ignored_names:
            print(prefix + branch + child.name + "/")
            new_prefix = prefix + ("    " if is_last else "│   ")
            render_tree_ignored(child, ignored_names, ignored_sufficies, new_prefix)
        
        elif child.name not in ignored_names and child.suffix not in ignored_sufficies:
            print(prefix + branch + child.name)

def find_file(node, name):
    for child in node.children:
        if child.name == name:
            return child.name
        
        elif child.is_directory:
            result = find_file(child, name)
            
            if result != None: return result
            
    return None

def find_strpath_to_file(node, file_name, prefix=""):
    for child in node.children:
        if child.name == file_name:
            return prefix + file_name
        
        elif child.is_directory:
            result = find_strpath_to_file(child, file_name, (prefix + child.name + "/"))
            
            if result != None: return result
            
    return None
        

