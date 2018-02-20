def minimumLoss(price):
    result = max(price)
    for key, i in enumerate(price):
        min_ = result
        for j in price[key+1:]:
            if j < i and (i - j) < min_:
                min_ = i - j
        if min_ < result:
            result = min_
    return result


if __name__ == "__main__":
    n = int(input().strip())
    price = list(map(int, input().strip().split(' ')))
    result = minimumLoss(price)
    print(result)
