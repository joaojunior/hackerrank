def get_minimum_cost(n, k, costs):
    costs = sorted(costs)
    result = 0
    quantity = 0
    buyed = 0
    while quantity < n:
        for i in range(min(k, len(costs))):
            result += (buyed + 1) * costs.pop(-1)
            quantity += 1
        buyed += 1
    return result


if __name__ == '__main__':
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    minimumCost = get_minimum_cost(n, k, c)
    print(minimumCost)
