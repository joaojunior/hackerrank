def minimum_swaps(array):
    positions = {}
    result = 0
    for i, number in enumerate(array):
        positions[number] = i
    for i, value in enumerate(array):
        number = i + 1
        if number != value:
            aux = array[i]
            array[i] = number
            array[positions[number]] = aux
            positions[aux] = positions[number]
            result += 1
    return result
