def jimOrders(orders):
    times = []
    for key, order in enumerate(orders):
        times.append((key+1, order[0] + order[1]))
    times = sorted(times, key=lambda x: (x[1], x[0]))
    return times


if __name__ == "__main__":
    n = int(input().strip())
    orders = []
    for orders_i in range(n):
        o_t = [int(orders_temp) for orders_temp in input().strip().split(' ')]
        orders.append(o_t)
    result = jimOrders(orders)
    for key, value in result:
        print(key, end=' ')
