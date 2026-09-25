def find_file(node, name):
    for child in node.children:
        if child.name == name:
            return child
        
        elif child.is_directory:
            result = find_file(child, name)
            if result != None: return result
            
    return None


def count_total_files(node):
    file_counter = 0
    
    for child in node.children:
        file_counter = file_counter + 1
        
        if child.is_directory:
            file_counter += count_total_files(child)
            
    return file_counter

def count_total_file_ignored(node, ignored_names, ignored_sufficies):
    file_counter = 0
        
    for child in node.children:
        if child.suffix not in ignored_sufficies:
            file_counter = file_counter + 1
            
        if child.is_directory and child.name not in ignored_names:
            file_counter += count_total_files(child)
                
    return file_counter

def count_total_directories(node):
    dir_counter = 0
    
    for child in node.children:
        if child.is_directory:
            dir_counter = dir_counter + 1
            dir_counter += count_total_directories(child)
            
    return dir_counter

def count_total_directories_ignored(node, ignored_names):
    dir_counter = 0
    
    for child in node.children:
        if child.name not in ignored_names and child.is_directory:
            dir_counter = dir_counter + 1
            dir_counter += count_total_directories_ignored(child, ignored_names)
            
    return dir_counter
