class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flip_equiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            if root1.val == root2.val:
                result = (self.flip_equiv(root1.left, root2.left) and
                          self.flip_equiv(root1.right, root2.right))
                return result or (self.flip_equiv(root1.left, root2.right) and
                                  self.flip_equiv(root1.right, root2.left))
            else:
                return False
        else:
            return False
