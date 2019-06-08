class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_complete_tree(self, root: TreeNode) -> bool:
        level = 0
        parents = [[root]]
        parents_leaf = []
        while parents:
            nodes = parents.pop(0)
            children = []
            for p in nodes:
                if p.left is not None:
                    children.append(p.left)
                if p.right is not None:
                    children.append(p.right)
            if children:
                parents.append(children)
                parents_leaf = nodes
            if len(children) > 0 and len(nodes) != 2 ** level:
                return False
            level += 1
        finded_none = False
        for p in parents_leaf:
            if ((p.left is not None or p.right is not None) and
                    finded_none is True):
                return False
            elif p.left is None and p.right is not None:
                return False
            elif p.left is None or p.right is None:
                finded_none = True
        return True
