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
        
        if child.suffix not in ignored_sufficies:
            print(prefix + branch + child.name)

