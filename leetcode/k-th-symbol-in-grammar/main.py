def generate(string, n, N):
    if n == N:
        return string
    else:
        new_string = ''
        for c in string:
            if c == '0':
                new_string += '01'
            else:
                new_string += '10'
        return generate(new_string, n + 1, N)


def find(N, K):
    string = generate('0', 1, N)
    return string[K - 1]


if __name__ == '__main__':
    print(find(4, 5))
