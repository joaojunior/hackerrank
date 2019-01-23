def arithmetic_expression(array):
    size = len(array)
    queue = [(array[0], str(array[0]))]
    start = 0
    i = 1
    cache = {array[0]: True}
    while i < size:
        end = len(queue)
        j = start
        while j < end:
            sum_, response = queue[j]
            sum_plus = (sum_ + array[i]) % 101
            sum_times = (sum_ * array[i]) % 101
            sum_minus = (sum_ - array[i]) % 101
            if sum_ % 101 == 0:
                queue = [[sum_times, response + '*' + str(array[i])]]
                j = 0
                end = 0
            else:
                all_in_cache = (
                    sum_plus in cache and sum_times in cache and
                    sum_minus in cache
                )
                if all_in_cache:
                    queue.append(
                        [sum_plus, response + '+' + str(array[i])]
                    )
                else:
                    if sum_plus not in cache:
                        queue.append(
                            [sum_plus, response + '+' + str(array[i])]
                        )
                        cache[sum_plus] = True
                    if sum_times not in cache:
                        queue.append(
                            [sum_times, response + '*' + str(array[i])]
                        )
                        cache[sum_times] = True
                    if sum_minus not in cache:
                        queue.append(
                            [sum_minus, response + '-' + str(array[i])]
                        )
                        cache[sum_minus] = True
            j += 1
        start = end
        i += 1
    for sum_, response in queue:
        if sum_ % 101 == 0:
            return response


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().rstrip().split()))
    print(arithmetic_expression(numbers))
