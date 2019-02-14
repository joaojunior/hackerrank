from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [[root]]
        zig = 1
        while queue:
            nodes = queue.pop(0)
            parcial = []
            level = []
            for node in nodes:
                if zig == 1:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left is not None:
                    parcial.append(node.left)
                if node.right is not None:
                    parcial.append(node.right)
            result.append(level)
            if parcial:
                queue.append(parcial)
            zig *= - 1
        return result
