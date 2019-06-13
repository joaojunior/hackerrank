from typing import Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delete_node(self, root: TreeNode, key: int) -> TreeNode:
        self.root = root
        parent, node_to_remove = self.binary_search(None, root, key)
        if node_to_remove is None:
            return root
        if node_to_remove.left is None:
            self.transplant(node_to_remove, node_to_remove.right)
        elif node_to_remove.right is None:
            self.transplant(node_to_remove, node_to_remove.left)
        else:
            y = self.minimum(node_to_remove.right)
            if y != node_to_remove.right:
                self.transplant(y, y.right)
                y.right = node_to_remove.right
            self.transplant(node_to_remove, y)
            y.left = node_to_remove.left

        return self.root

    def binary_search(self, parent: TreeNode,
                      root: TreeNode, key: int) -> Tuple[TreeNode, TreeNode]:
        if root is not None:
            if root.val == key:
                return parent, root
            elif key < root.val:
                return self.binary_search(root, root.left, key)
            else:
                return self.binary_search(root, root.right, key)
        else:
            return parent, None

    def minimum(self, root: TreeNode) -> TreeNode:
        while root.left is not None:
            root = root.left
        return root

    def transplant(self, x: TreeNode, y: TreeNode):
        parent, _ = self.binary_search(None, self.root, x.val)
        if parent is None:
            self.root = y
        elif x == parent.left:
            parent.left = y
        else:
            parent.right = y
