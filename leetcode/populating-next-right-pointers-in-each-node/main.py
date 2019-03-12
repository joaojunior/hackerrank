class Node:
    def __init__(self, val: int, left: 'Node', right: 'Node', next: 'Node'):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is not None:
            queue = [[root]]
            while queue:
                nodes = queue.pop(0)
                size = len(nodes)
                childrens = []
                for i, node in enumerate(nodes):
                    if i < size - 1:
                        node.next = nodes[i+1]
                    if node.left is not None:
                        childrens.append(node.left)
                        childrens.append(node.right)
                if childrens:
                    queue.append(childrens)
        return root
