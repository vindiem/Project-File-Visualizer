from pathlib import Path
import tree_operations as TreeOp
import tree_builder as TreeBuilder
import tree_renderer as TreeRenderer

path = Path("/Users/alohadance/General/ConsoleApplications")
root = []

ignored_names = ["objects", "Python"]
ignored_sufficies = [".sample", ".pyc", ".git"]

if __name__ == "__main__":
    root = TreeBuilder.build_tree(path)
    TreeRenderer.render_tree_ignored(root, ignored_names, ignored_sufficies)
    
    print("Found file name: ", (TreeOp.find_file(root, "refs").name) 
          if TreeOp.find_file(root, "refs") != None 
          else "None")
    print("Total files: ", TreeOp.count_total_files(root))
    print("Visible files: ", TreeOp.count_total_file_ignored(root, ignored_names, ignored_sufficies))
    
    print("Total folders: ", TreeOp.count_total_directories(root))
    print("Visible folders: ", TreeOp.count_total_directories_ignored(root, ignored_names))



