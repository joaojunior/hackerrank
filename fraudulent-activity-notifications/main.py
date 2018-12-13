def activity_notifications(expenditure, d):
    notifications = 0
    mid = d // 2
    residual = d % 2
    for i in range(d, len(expenditure)):
        window = expenditure[i-d: i]
        window.sort()
        if residual == 0:
            median = (window[mid-1] + window[mid]) / 2
        else:
            median = window[mid]
        if expenditure[i] >= 2 * median:
            notifications += 1
    return notifications
