def lca(root, v1, v2):
    if v1 < root.info:
        if v2 > root.info:
            return root
        if v2 < root.info:
            return lca(root.left, v1, v2)
    elif v1 > root.info:
        if v2 < root.info:
            return root
        if v2 > root.info:
            return lca(root.right, v1, v2)
    else:
        return root
