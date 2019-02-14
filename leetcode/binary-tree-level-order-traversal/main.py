from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [[root]]
        while queue:
            nodes = queue.pop(0)
            parcial = []
            level = []
            for node in nodes:
                level.append(node.val)
                if node.left is not None:
                    parcial.append(node.left)
                if node.right is not None:
                    parcial.append(node.right)
            result.append(level)
            if parcial:
                queue.append(parcial)
        return result
