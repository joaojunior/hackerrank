def frequency_query(queries):
    data = {}
    result = []
    frequency = {}
    for query in queries:
        type_ = query[0]
        value = query[1]
        if type_ == 1:
            data[value] = data.get(value, 0) + 1
            if frequency.get(data[value]-1, 0) > 0:
                frequency[data[value]-1] -= 1
            frequency[data[value]] = frequency.get(data[value], 0) + 1
        elif type_ == 2:
            if data.get(value, 0) > 0:
                if frequency.get(data[value], 0) > 0:
                    frequency[data[value]] -= 1
                frequency[data[value]-1] = frequency.get(data[value]-1, 0) + 1
                data[value] -= 1
        else:
            if frequency.get(value, 0) > 0:
                result.append(1)
            else:
                result.append(0)
    return result
