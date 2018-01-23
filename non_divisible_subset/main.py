from collections import defaultdict


def nonDivisibleSubset(k, arr):
    result = defaultdict(list)
    for number in arr:
        rest = number % k
        result[rest].append(number)
    max_size = 0
    if len(result[0]) > 0:
        max_size = 1
    middle = k // 2
    for i in range(1, middle + 1):
        if i == k - i:
            max_size += min(1, len(result[i]))
        elif len(result[i]) > len(result[k - i]):
            max_size += len(result[i])
        else:
            max_size += len(result[k - i])
    return max_size


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
