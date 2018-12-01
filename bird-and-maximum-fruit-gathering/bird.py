from sys import stdin


def bird(values, size_pass):
    result = 0

    n = len(values)
    if size_pass > n:
        size_pass = n
    for i in range(n):
        if i + size_pass < n:
            result_aux = sum(values[i:i+size_pass])
        else:
            result_aux = sum(values[i:n]) + sum(values[0:size_pass-(n-i)])
        if result_aux > result:
            result = result_aux
    return result


if __name__ == '__main__':
    quantity = int(stdin.readline())

    for i in range(quantity):
        line = stdin.readline()
        line = line.replace('\n', '')
        line = line.split()
        size_pass = int(line[1])

        line = stdin.readline()
        values = []
        for value in line.split():
            values.append(int(value))

        print(bird(values, size_pass))
