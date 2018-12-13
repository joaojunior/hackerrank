def luck_balance(k, contests):
    contests.sort(key=lambda item: item[0])
    importances = 0
    for value, importance in contests:
        if importance == 1:
            importances += 1
    result = 0
    qty = 0
    for value, importance in contests:
        if importance == 0:
            result += value
        elif qty < importances - k:
            qty += 1
            result -= value
        else:
            result += value
    return result
