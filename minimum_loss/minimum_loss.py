def minimumLoss(price):
    index = {}
    for key, i in enumerate(price):
        index[i] = key
    price_sorted = sorted(price)
    result = max(price)
    for i in range(len(price_sorted) - 1):
        less = price_sorted[i]
        great = price_sorted[i+1]
        if great - less < result and index[great] < index[less]:
            result = great - less
    return result


if __name__ == "__main__":
    n = int(input().strip())
    price = list(map(int, input().strip().split(' ')))
    result = minimumLoss(price)
    print(result)
