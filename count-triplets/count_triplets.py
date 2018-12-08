def all_subsets_size_3(array):
    size = len(array)
    for i in range(size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                yield array[i], array[j], array[k]


def count_triplets(array, r):
    result = 0
    for x, y, z in all_subsets_size_3(array):
        if y == x * r and z == y * r:
            result += 1
    return result


if __name__ == '__main__':
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    print(count_triplets(arr, r))
