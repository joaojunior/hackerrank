class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes = []
        self.qty = 0
        self.actual = 0
        self.in_order(root)

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            self.nodes.append(root.val)
            self.qty += 1
            self.in_order(root.right)

    def next(self) -> int:
        self.actual += 1
        return self.nodes[self.actual - 1]

    def hasNext(self) -> 'bool':
        return self.actual < self.qty


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    bst_iterator = BSTIterator(root)
    print(bst_iterator.next())
    print(bst_iterator.next())
    print(bst_iterator.next())
    print(bst_iterator.hasNext())
