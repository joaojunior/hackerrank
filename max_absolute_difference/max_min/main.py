def max_min(k, arr):
    arr = sorted(arr)
    result = 10**9
    for i in range(len(arr) - k + 1):
        min_ = arr[i]
        max_ = arr[i+k-1]
        if max_ - min_ < result:
            result = max_ - min_
    return result


if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
        arr_t = int(input().strip())
        arr.append(arr_t)
    result = max_min(k, arr)
    print(result)
