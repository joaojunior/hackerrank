def check_bst(root):
    frequency = {root.data: 1}
    result = True
    if root.left is not None:
        if root.data > root.left.data:
            result = check_bst_in_left(root.left, root.data, frequency)
        else:
            result = False
    if result and root.right is not None:
        if root.data < root.right.data:
            result = check_bst_in_right(root.right, root.data, frequency)
        else:
            result = False
    return result


def check_bst_in_left(parent, max_value, frequency):
    max_value = max(max_value, parent.data)
    if parent.left is not None:
        result = check_bst_in_left(parent.left, max_value, frequency)
        if (result is False or parent.data <= parent.left.data or
                parent.left.data >= max_value):
            return False
        if parent.left.data in frequency:
            return False
        frequency[parent.left.data] = 1
    if parent.right is not None:
        result = check_bst_in_left(parent.right, max_value, frequency)
        if (result is False or parent.data >= parent.right.data or
                parent.right.data >= max_value):
            return False
        if parent.right.data in frequency:
            return False
        frequency[parent.right.data] = 1
    return True


def check_bst_in_right(parent, min_value, frequency):
    min_value = min(min_value, parent.data)
    if parent.left is not None:
        result = check_bst_in_right(parent.left, min_value, frequency)
        if (result is False or parent.data <= parent.left.data or
                parent.left.data <= min_value):
            return False
        if parent.left.data in frequency:
            return False
        frequency[parent.left.data] = 1
    if parent.right is not None:
        result = check_bst_in_right(parent.right, min_value, frequency)
        if (result is False or parent.data >= parent.right.data or
                parent.right.data <= min_value):
            return False
        if parent.right.data in frequency:
            return False
        frequency[parent.right.data] = 1
    return True
