def count_triplets(array, r):
    result = 0
    quantity = {}
    for i in array:
        quantity[i] = quantity.get(i, 0) + 1
    for key, value in quantity.items():
        if r == 1:
            result += (value * (value - 1) * (value - 2)) // 6
        else:
            value2 = quantity.get(key * r, 0)
            value3 = quantity.get(key * r * r, 0)
            result += value * value2 * value3
    return result


if __name__ == '__main__':
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    print(count_triplets(arr, r))
