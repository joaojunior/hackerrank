def get_minimum_cost(n, k, costs):
    costs = sorted(costs)
    result = 0
    quantity = 0
    by_one = n // k
    if n % k != 0:
        by_one += 1
    end = by_one
    while quantity < n:
        for i in range(by_one):
            result += (i + 1) * costs[end - i - 1]
            quantity += 1
            print(end -i - 1, i)
        end += by_one
        if end > n:
            by_one = n - quantity
            end = n
    return result


if __name__ == '__main__':
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    minimumCost = get_minimum_cost(n, k, c)
    print(minimumCost)
