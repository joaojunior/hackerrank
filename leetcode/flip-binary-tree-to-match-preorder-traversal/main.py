from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flip_match_voyage(self, root: TreeNode,
                          voyage: List[int]) -> List[int]:
        self.i = 0
        self.result = []
        self.voyage = voyage
        result = self.pre_order(root)
        if result is True:
            return self.result
        else:
            return [-1]

    def pre_order(self, root):
        if root is None:
            return True
        else:
            val = self.voyage[self.i]
            self.i += 1
            last_i = self.i
            if root.val == val:
                result = (self.pre_order(root.left) and
                          self.pre_order(root.right))
                if result is False:
                    self.i = last_i
                    self.result.append(root.val)
                    result = (self.pre_order(root.right) and
                              self.pre_order(root.left))
                return result
            else:
                return False
