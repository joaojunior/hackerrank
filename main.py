def k_factorization(numbers, n):
    numbers = sorted(numbers, reverse=True)
    n_bck = n
    divisors = []
    for divisor in numbers:
        if n % divisor == 0:
            divisors.append(divisor)
    result = []
    while divisors:
        divisor = divisors.pop(0)
        while n % divisor == 0:
            result.append(divisor)
            n = n / divisor
    result.append(1)
    for i in range(len(result) - 2, -1, -1):
        result[i] = result[i] * result[i+1]
    result.reverse()
    if result and result[-1] == n_bck:
        return result
    else:
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
