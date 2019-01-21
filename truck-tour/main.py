def truck_tour(petrolpumps):
    size = len(petrolpumps)
    initial = 0
    founded = False

    while founded is False and initial < size:
        total = 0
        for i in range(size):
            position = (i + initial) % size
            total += petrolpumps[position][0] - petrolpumps[position][1]
            if total < 0:
                break
        if total >= 0:
            founded = True
        else:
            initial += 1
    return initial


if __name__ == '__main__':
    petrolpumps = [[1, 5], [10, 3], [3, 4]]
    print(truck_tour(petrolpumps))
