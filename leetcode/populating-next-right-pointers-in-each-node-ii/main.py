class TreeLinkNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: TreeLinkNode):
        if root is not None:
            queue = [[root]]
            while queue:
                next_ = []
                nodes = queue.pop(0)
                while nodes:
                    node = nodes.pop(0)
                    if len(nodes) > 0:
                        node.next = nodes[0]
                    if node.left is not None:
                        next_.append(node.left)
                    if node.right is not None:
                        next_.append(node.right)
                if next_:
                    queue.append(next_)
