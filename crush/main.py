def crush(n, queries):
    data = {}
    max_ = 0
    aux = 0
    for query in queries:
        start = query[0]
        end = query[1]
        value = query[2]
        data[start] = data.get(start, 0) + value
        if end + 1 <= n:
            data[end+1] = data.get(end+1, 0) - value
    for i in range(1, n+1):
        aux += data.get(i, 0)
        if aux > max_:
            max_ = aux
    return max_
