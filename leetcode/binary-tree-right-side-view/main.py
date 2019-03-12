from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def right_side_view(self, root: TreeNode) -> List[int]:
        result = []
        if root is not None:
            queue = [[root]]
            while queue:
                nodes = queue.pop(0)
                result.append(nodes[-1].val)
                childrens = []
                for node in nodes:
                    if node.left is not None:
                        childrens.append(node.left)
                    if node.right is not None:
                        childrens.append(node.right)
                if childrens:
                    queue.append(childrens)
        return result
