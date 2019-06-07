class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtree_with_all_deepest(self, root: TreeNode) -> TreeNode:
        nodes, level = self.post_order(root)
        return nodes

    def post_order(self, root, level=0):
        if root is not None:
            left_parent, left_level = self.post_order(root.left, level + 1)
            right_parent, right_level = self.post_order(root.right, level + 1)
            if left_level == right_level:
                return root, left_level
            elif left_level > right_level:
                return left_parent, left_level
            else:
                return right_parent, right_level
        else:
            return None, level
