from sys import stdin


def largest_sum_subarray_of_size_at_least_k(array, k):
    start = 0
    sum_ = sum(array)

    while len(array) - start >= k:
        last = start + k
        while last <= len(array):
            sum_aux = sum(array[start:last])
            if sum_aux > sum_:
                sum_ = sum_aux
            last += 1
        start += 1
    return sum_


if __name__ == '__main__':
    quantity = int(stdin.readline())

    for i in range(quantity):
        n = int(stdin.readline())
        line = stdin.readline()
        line = line.replace('\n', '')
        array = []
        for i in line.split():
            array.append(int(i))
        k = int(stdin.readline())
        print(largest_sum_subarray_of_size_at_least_k(array, k))
