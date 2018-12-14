def height(root):
    h = 0
    queue = [[root]]
    while queue:
        parents = queue.pop(0)
        childrens = []
        for parent in parents:
            if parent.left is not None:
                childrens.append(parent.left)
            if parent.right is not None:
                childrens.append(parent.right)
        if childrens:
            h += 1
            queue.append(childrens)
    return h
