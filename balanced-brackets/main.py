def is_balanced(s):
    size = len(s)
    if size == 1:
        return 'YES'
    if size % 2 != 0:
        return 'NO'
    stack = [''] * size
    i = 0
    for c in s:
        if c in ['{', '(', '[']:
            stack[i] = c
            i += 1
        else:
            top = stack[i-1]
            i -= 1
            if ((top == '{' and c != '}') or
                    (top == '[' and c != ']') or
                    (top == '(' and c != ')')):
                return 'NO'
        if i < 0:
            return 'NO'
    if i != 0:
        return 'NO'
    return 'YES'
