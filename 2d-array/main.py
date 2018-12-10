def hourglass_sum(array):
    result = None
    size = len(array)
    for i in range(size-2):
        for j in range(size-2):
            sum_ = (array[i][j] + array[i][j+1] + array[i][j+2] +
                    array[i+2][j] + array[i+2][j+1] + array[i+2][j+2] +
                    array[i+1][j+1])
            if result is None or sum_ > result:
                result = sum_
    return result


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        result = hourglass_sum(arr)
    print(result)
