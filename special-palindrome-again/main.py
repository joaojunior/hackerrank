def _generate_substring(s):
    size = len(s)
    i = 0
    while i < size:
        j = i + 1
        while j <= size:
            yield s[i:j]
            j += 1
        i += 1


def _is_palindrome(s, memoize={}):
    if s in memoize:
        return memoize[s]
    size = len(s)
    mid = size // 2
    result = False
    if size == 1:
        result = True
    else:
        count = 1
        c = s[0]
        i = 0
        while i < size and count == 1:
            if s[i] != c:
                count += 1
            i += 1
        if count == 1:
            result = True
        else:
            result = s[0:mid] == s[mid+1:size]
    memoize[s] = result
    return result


def substr_count(s):
    count = 0
    memoize = {}
    for substr in _generate_substring(s):
        if _is_palindrome(substr, memoize):
            count += 1
    return count
