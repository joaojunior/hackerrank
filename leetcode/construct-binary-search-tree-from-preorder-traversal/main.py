from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bst_from_preorder(self, preorder: List[int]) -> TreeNode:
        val = preorder.pop(0)
        root = TreeNode(val)
        i = self.position_val_is_greater_than(val, preorder)
        if i is not None:
            left_preorder = preorder[:i]
            right_preorder = preorder[i:]
        else:
            left_preorder = preorder
            right_preorder = []
        if left_preorder:
            root.left = self.bst_from_preorder(left_preorder)
        if right_preorder:
            root.right = self.bst_from_preorder(right_preorder)
        return root

    def position_val_is_greater_than(self, val: int, data: List[int]) -> int:
        for i, v in enumerate(data):
            if v > val:
                return i
