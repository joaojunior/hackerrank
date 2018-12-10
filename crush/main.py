def crush(m, queries):
    data = {}
    max_ = 0
    for query in queries:
        start = query[0]
        end = query[1]
        value = query[2]
        for i in range(end-start+1):
            data[i+start] = data.get(i+start, 0) + value
            if data[i+start] > max_:
                max_ = data[i+start]
    return max_


print(crush(3, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
