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
    return longest_common_subsequence(s1, s2)


def longest_common_subsequence(s1, s2, memoization=None):
    if memoization is None:
        memoization = {}
    if (s1, s2) in memoization:
        return memoization[(s1, s2)]
    if len(s1) == 0 or len(s2) == 0:
        return 0
    elif s1[-1] == s2[-1]:
        memoization[(s1, s2)] = longest_common_subsequence(
            s1[:-1], s2[:-1], memoization) + 1
        return memoization[(s1, s2)]
    else:
        memoization[(s1, s2)] = max(
            longest_common_subsequence(s1, s2[:-1], memoization),
            longest_common_subsequence(s1[:-1], s2, memoization)
        )
        return memoization[(s1, s2)]
