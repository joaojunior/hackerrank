def activity_notifications(expenditure, d):
    notifications = 0
    mid = d // 2
    residual = d % 2

    window = expenditure[0: d]
    to_remove = window[:]
    window.sort()
    for i in range(d, len(expenditure)):
        if residual == 0:
            median = (window[mid-1] + window[mid]) / 2.0
        else:
            median = window[mid]
        if expenditure[i] >= 2 * median:
            notifications += 1
        remove = to_remove.pop(0)
        if expenditure[i] != remove:
            window.remove(remove)
            binary_search(window, expenditure[i])
        to_remove.append(expenditure[i])

    return notifications


def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left < right:
        m = (left + right) // 2
        if data[m] < value:
            left = m + 1
        elif data[m] > value:
            right = m
        else:
            data.insert(m, value)
            return
    if left == len(data) - 1:
        if data[left] < value:
            data.insert(left+1, value)
        else:
            data.insert(left, value)
    else:
        data.insert(left, value)


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activity_notifications(expenditure, d)

    print(result)
