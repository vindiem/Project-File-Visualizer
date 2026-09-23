from pathlib import Path
import tree_operations as TreeOp

path = Path("/Users/alohadance/General/ConsoleApplications/Funki")
root = []

ignored_names = ["objects", ".git"]
ignored_sufficies = [".sample"]

if __name__ == "__main__":
    root = TreeOp.build_tree(path)
    TreeOp.render_tree_ignored(root, ignored_names, ignored_sufficies)
    
    print(TreeOp.find_file(root, "app.json"))
    print(TreeOp.find_strpath_to_file(root, "Launcher.java"))
