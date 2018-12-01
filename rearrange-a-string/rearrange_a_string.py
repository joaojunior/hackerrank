from sys import stdin


def rearrange_a_string(string):
    sum_ = 0
    result = []
    for i in string:
        if i.isdigit():
            sum_ += int(i)
        else:
            result.append(i)
    result.sort()
    result.append(str(sum_))
    return ''.join(result)


if __name__ == '__main__':
    quantity = int(stdin.readline())

    for i in range(quantity):
        line = stdin.readline()
        line = line.replace('\n', '')
        print(rearrange_a_string(line))
