from sys import stdin


def maximum_integer_value(string):
    result = int(string[0])

    for i in string[1:]:
        i = int(i)

        if result == 1:
            result += i
        elif i < 2 or result == 0:
            result += i
        else:
            result *= i
    return result


if __name__ == '__main__':
    quantity = int(stdin.readline())
    for i in range(quantity):
        string = stdin.readline()
        string = string.replace('\n', '')
        print(maximum_integer_value(string))
