def super_digit(n, k):
    p = n
    queue = [p]
    while queue:
        p = queue.pop(0)
        if len(p) == 1:
            return int(p)
        else:
            sum_ = 0
            for digit in p:
                sum_ += int(digit)
            sum_ = str(sum_)
            if len(sum_) == 1:
                sum_ = sum_ * k
                k = 1
            queue.append(sum_)


if __name__ == '__main__':
    n, k = input().split()
    k = int(k)
    print(super_digit(n, k))
