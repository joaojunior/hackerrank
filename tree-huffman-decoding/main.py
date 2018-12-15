def decode_huff(root, s):
    s = list(s)
    result = ''
    while s:
        result += decode(root, s)

    return result


def decode(parent, s):
    if parent.left is None and parent.right is None:
        return parent.data
    value = s.pop(0)
    if value == '0':
        return decode(s, parent.left)
    else:
        return decode(s, parent.right)
