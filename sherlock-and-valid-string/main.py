def is_valid(s):
    frequencies = {}
    min_ = len(s)
    max_ = 0
    qty_max = 0
    qty_min = 0
    result = 'NO'
    for c in s:
        frequencies[c] = frequencies.get(c, 0) + 1
    for frequency in frequencies.values():
        if frequency < min_:
            min_ = frequency
            qty_min = 1
        elif frequency == min_:
            qty_min += 1
        if frequency > max_:
            max_ = frequency
            qty_max = 1
        elif frequency == max_:
            qty_max += 1
    if max_ == min_:
        result = 'YES'
    elif (max_ - min_) == 1 and (qty_max == 1 or qty_min == 1):
        result = 'YES'
    elif (max_ - min_) >= 2 and (min_ == 1):
        result = 'YES'

    return result
