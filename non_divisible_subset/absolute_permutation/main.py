def absolute_permutation(n, k):
    numbers = range(1,n + 1)
    permutation = [None] * (n + 1)
    finded = True
    quantity = 0
    add = k
    for number in numbers:
        position = number + add
        quantity += 1
        if quantity == k:
            quantity = 0
            add = -add
        if(position > 0 and position <= n and permutation[position] is None):
            permutation[position] = number
        else:
            finded = False
    if finded is True:
        for number in permutation[1:]:
            print(number, end=' ')
    else:
        print(-1, end=' ')


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        absolute_permutation(n, k)
        print()
