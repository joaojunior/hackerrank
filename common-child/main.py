def common_child(s1, s2):
    size = len(s1)
    frequencies_s1 = {}
    frequencies_s2 = {}
    for c in s1:
        frequencies_s1[c] = frequencies_s1.get(c, 0) + 1
    for c in s2:
        frequencies_s2[c] = frequencies_s2.get(c, 0) + 1
    if frequencies_s1 == frequencies_s2:
        return size
    frequency_equals = 0
    for c, frequency_s1 in frequencies_s1.items():
        frequency_s2 = frequencies_s2.get(c, 0)
        frequency_equals += min(frequency_s1, frequency_s2)
    if frequency_equals == 0:
        return 0
    new_s1 = []
    new_s2 = []
    for c in s1:
        if c in frequencies_s2:
            new_s1.append(c)
    for c in s2:
        if c in frequencies_s1:
            new_s2.append(c)
    return longest_common_subsequence(''.join(new_s1), ''.join(new_s2))


def longest_common_subsequence(s1, s2):
    memoization = {}
    size_s1 = len(s1)
    size_s2 = len(s2)
    for i in range(1, size_s1+1):
        for j in range(1, size_s2+1):
            if s1[i-1] == s2[j-1]:
                memoization[(i, j)] = memoization.get((i-1, j-1), 0) + 1
            else:
                memoization[(i, j)] = max(memoization.get((i, j-1), 0),
                                          memoization.get((i-1, j), 0))
    return memoization[(size_s1, size_s2)]
