class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode):
        if root is not None:
            self.queue = []
            self.preorder(root)
            root = self.queue.pop(0)
            while self.queue:
                root.right = self.queue.pop(0)
                root.left = None
                root = root.right

    def preorder(self, root: TreeNode):
        if root is not None:
            self.queue.append(root)
            self.preorder(root.left)
            self.preorder(root.right)
