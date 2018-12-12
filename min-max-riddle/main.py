def riddle(array):
    result = []
    for size in range(1, len(array) + 1):
        max_ = 0
        for start in range(len(array) - size + 1):
            min_ = min(array[start:start+size])
            if min_ > max_:
                max_ = min_
        result.append(max_)
    return result
