from collections import defaultdict


def k_factorization(numbers, n):
    numbers = sorted(numbers)
    memoization = defaultdict(list)
    size = len(numbers)
    for number in numbers:
        memoization[1].append((number, [1, number]))
        if number == n:
            return n
    for i in range(2, size + 1):
        for value, multiply in memoization[i-1]:
            for number in numbers:
                new_value = number * value
                new_multiply = multiply[:]
                new_multiply.append(new_value)
                if new_value == n:
                    return new_multiply
                memoization[i].append((new_value, new_multiply))
    return [-1]


if __name__ == "__main__":
    n, size = input().split()
    n = int(n)
    size = int(size)
    numbers = input().split()
    for i in range(size):
        numbers[i] = int(numbers[i])
    result = k_factorization(numbers, n)
    for number in result:
        print(number, end=" ")
