class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return ''
        result = []
        queue = [[root]]
        while queue:
            new_nodes = []
            nodes = queue.pop(0)
            for node in nodes:
                if node is not None:
                    result.append(str(node.val))
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                else:
                    result.append('null')
            if new_nodes:
                queue.append(new_nodes)
        return ','.join(result)

    def deserialize(self, data: str) -> TreeNode:
        if data == '':
            return None
        data = data.split(',')
        size = len(data)
        base_root = TreeNode(data[0])
        queue = [(base_root, 0)]
        while queue:
            root, i = queue.pop(0)
            left = 2*i+1
            right = 2*i+2
            if right < size:
                root.left = TreeNode(data[left])
                root.right = TreeNode(data[right])
                queue.append((root.left, left))
                queue.append((root.right, right))
        return base_root
