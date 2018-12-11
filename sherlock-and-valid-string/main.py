def is_valid(s):
    frequencies = {}
    result = 'NO'
    for c in s:
        frequencies[c] = frequencies.get(c, 0) + 1

    values = sorted(frequencies.values())
    min_ = values[0]
    max_ = values[-1]
    if min_ == max_:
        result = 'YES'
    elif min_ == 1 and max_ == values[1]:
        result = 'YES'
    elif min_ == max_ - 1 and min_ == values[-2]:
        result = 'YES'
    return result
