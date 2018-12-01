from sys import stdin


def fibonacci(size):
    f_1 = 0
    f_2 = 1
    result = {f_1: True, f_2: True}
    for i in range(2, size + 1):
        sum_ = f_1 + f_2
        result[sum_] = True
        f_1 = f_2
        f_2 = sum_

    return result


def largest_fibonacci_subsequence(array):
    fibonacci_numbers = fibonacci(len(array))
    result = []
    for i in array:
        if fibonacci_numbers.get(i, False) is True:
            result.append(i)
    return result


if __name__ == '__main__':
    quantity = int(stdin.readline())

    for i in range(quantity):
        n = int(stdin.readline())
        line = stdin.readline()
        line = line.replace('\n', '')
        array = []
        for value in line.split():
            array.append(int(value))
        result = largest_fibonacci_subsequence(array)
        for number in result:
            print(number, end=' ')
        if i + 1 < quantity:
            print('')
