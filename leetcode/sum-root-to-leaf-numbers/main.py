class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sum_numbers(self, root: TreeNode) -> int:
        self.result = 0
        self.find(root, '')
        return self.result

    def find(self, root, s):
        if root is not None:
            s += str(root.val)
            if root.left is None and root.right is None:
                self.result += int(s)
            else:
                self.find(root.left, s)
                self.find(root.right, s)
