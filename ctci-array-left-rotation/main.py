def rot_left(array, d):
    copy_array = array[:]
    for i in range(len(array)):
        array[i-d] = copy_array[i]
    return array


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    array = list(map(int, input().rstrip().split()))
    result = rot_left(array, d)
    print(' '.join(map(str, result)))
