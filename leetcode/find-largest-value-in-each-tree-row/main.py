from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largest_values(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        nodes = [[root]]
        while nodes:
            parents = nodes.pop(0)
            childrens = []
            largest = parents[0].val
            for p in parents:
                if p.val > largest:
                    largest = p.val
                if p.left is not None:
                    childrens.append(p.left)
                if p.right is not None:
                    childrens.append(p.right)
            result.append(largest)
            if childrens:
                nodes.append(childrens)
        return result
