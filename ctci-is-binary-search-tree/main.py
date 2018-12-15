def check_bst(root):
    return check(root, 0, 10**4)


def check(n, min_, max_):
    if n is None:
        return True
    if(n.data <= min_ or n.data >= max_):
        return False
    return check(n.left, min_, n.data) and check(n.right, n.data, max_)
