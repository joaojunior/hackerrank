def what_flavors(costs, money):
    costs_index = {}
    for key, value in enumerate(costs):
        costs_value = costs_index.get(value, [])
        costs_value.append(key + 1)
        costs_index[value] = costs_value
    for value, keys in costs_index.items():
        keys2 = costs_index.get(money - value)
        if keys2:
            key = min(keys)
            key2 = max(keys2)
            if key < key2:
                return key, key2
            elif key > key2:
                key2, key
