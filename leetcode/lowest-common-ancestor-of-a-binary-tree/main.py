from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root: TreeNode,
                               p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.dfs(root, p.val)
        path_q = self.dfs(root, q.val)
        i = len(path_p) - 1
        j = len(path_q) - 1
        founded = -1
        while founded == -1:
            if path_p[i] == path_q[j]:
                founded = path_p[i]
            if i < j:
                j -= 1
            elif j < i:
                i -= 1
            else:
                i -= 1
                j -= 1
        return founded

    def dfs(self, root: TreeNode, value: int) -> List[TreeNode]:
        if root is None:
            return []
        elif root.val == value:
            return [root]
        else:
            result = self.dfs(root.left, value)
            if result:
                result.insert(0, root)
            else:
                result = self.dfs(root.right, value)
                if result:
                    result.insert(0, root)
            return result
