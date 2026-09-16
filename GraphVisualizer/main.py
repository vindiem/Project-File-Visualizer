from pathlib import Path
import tree_operations as TreeOp

path = Path("/Users/alohadance/General/ConsoleApplications/Funki")
root = []

if __name__ == "__main__":
    # draw_architecture(path)
    root = TreeOp.build_tree(path)
    TreeOp.render_tree(root)
