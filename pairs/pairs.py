def pairs(k, data):
    index = {}
    result = 0
    for i, value in enumerate(data):
        index[value] = i
    for number in data:
        if number - k in index:
            result += 1
    return result


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)
