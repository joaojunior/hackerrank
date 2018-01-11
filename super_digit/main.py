def super_digit(p):
    if len(p) == 1:
        return int(p)
    else:
        sum_ = 0
        for digit in p:
            sum_ += int(digit)
        return super_digit(str(sum_))


if __name__ == '__main__':
    n, k = input().split()
    k = int(k)
    p = n * k
    print(super_digit(p))
