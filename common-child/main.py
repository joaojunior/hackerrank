def common_child(s1, s2):
    size_s1 = len(s1)
    size_s2 = size_s1
    memoization = [[0]*(size_s1+1)]
    for i in range(1, size_s1+1):
        memoization.append([0]*(size_s1+1))
        for j in range(1, size_s2+1):
            if s1[i-1] == s2[j-1]:
                memoization[i][j] = memoization[i-1][j-1] + 1
            else:
                memoization[i][j] = max(memoization[i][j-1],
                                        memoization[i-1][j])
    return memoization[size_s1][size_s2]
