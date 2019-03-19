class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_bottom_left_value(self, root: TreeNode) -> int:
        queue = [[root]]
        result = None
        while queue:
            nodes = queue.pop(0)
            result = nodes[0].val
            childrens = []
            for root in nodes:
                if root.left is not None:
                    childrens.append(root.left)
                if root.right is not None:
                    childrens.append(root.right)
            if childrens:
                queue.append(childrens)
        return result
