# Tree Structure - TreeNode in Decision Tree
class TreeNode:

    def __init__(self, node_label, leaf=False):
        self.op = node_label
        self.kids = [None] * 2
        self.leaf = leaf

    def __str__(self):
        return str(self.op)

    def preorder_traversal(self):
        if self.op == None:
            return "null"
        else:
            left = ""

            if self.kids[0] == None:
                left = "null"
            else:
                left = self.kids[0].preorder_traversal()

            if self.kids[1] == None:
                right = "null"
            else:
                right = self.kids[1].preorder_traversal()
            return str(self.op) + ", " + left + ", " + right

    def set_leaf(self):
        self.leaf = True

    def set_child(self, index, child):
        self.kids[index] = child

    def get_child(self, index):
        return self.kids[index]

    @staticmethod
    def traverse(root):
        current_level = [root]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:

                if n.op == "A":
                    continue;

                if n.kids[0]:
                    next_level.append(n.kids[0])
                else:
                    next_level.append(TreeNode("A"))
                if n.kids[1]:
                    next_level.append(n.kids[1])
                else:
                    next_level.append(TreeNode("A"))
            current_level = next_level

    # TREE STRUCTURE - Utility functions
    def flatten_tree(self, root):
        print(str(root.op), end='')
        if root.kids:
            for kid in root.kids:
                if kid:
                    print('[', end='')
                    self.flatten_tree(kid)
                    print(']', end='')

    def print_tree(self, root):
        self.flatten_tree(root)
        print()
