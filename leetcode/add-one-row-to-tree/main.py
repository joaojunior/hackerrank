class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def add_one_row(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            root = new_root
        else:
            level = 1
            parents = [root]
            while level + 1 != d:
                level += 1
                childrens = []
                for node in parents:
                    if node.left is not None:
                        childrens.append(node.left)
                    if node.right is not None:
                        childrens.append(node.right)
                parents = childrens[:]
            for p in parents:
                left = p.left
                right = p.right
                p.left = TreeNode(v)
                p.left.left = left
                p.right = TreeNode(v)
                p.right.right = right
        return root
