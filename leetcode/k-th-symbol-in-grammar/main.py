def find(N, K):
    data = [0]
    i = 1
    while i < N:
        size = len(data)
        for j in range(size):
            c = data[j]
            if c == 0:
                data.append(1)
            else:
                data.append(0)
        i += 1
    return data[K - 1]


if __name__ == '__main__':
    print(find(30, 434991989))
