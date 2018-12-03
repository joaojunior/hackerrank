def recursive_staircase(available, steps=(1, 2, 3), memoization={}):
    if available in memoization:
        return memoization[available]
    elif available < 0:
        return 0
    elif available == 0:
        return 1
    else:
        result = 0
        for step in steps:
            result_aux = recursive_staircase(available - step)
            memoization[available-step] = result_aux
            result += result_aux
        return result
