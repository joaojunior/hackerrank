def recursive_staircase(available, steps=(1, 2, 3)):
    if available < 0:
        return 0
    elif available == 0:
        return 1
    else:
        result = 0
        for step in steps:
            result += recursive_staircase(available - step)
        return result
