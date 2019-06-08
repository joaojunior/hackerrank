class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.result = ''
        self.pre_order(root, '')
        return self.result

    def pre_order(self, root: TreeNode, word: str):
        if root is not None:
            word = chr(97 + root.val) + word
            self.pre_order(root.left, word)
            self.pre_order(root.right, word)
            if root.left is None and root.right is None:
                if word < self.result or self.result == '':
                    self.result = word
