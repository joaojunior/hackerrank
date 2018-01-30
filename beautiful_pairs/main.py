from collections import Counter


def beautifulPairs(A, B):
    count_a = Counter(A)
    count_b = Counter(B)
    size = len(A)
    if sorted(A) == sorted(B):
        return size - 1
    result = 0
    for key, quantity in count_a.items():
        result += min(quantity, count_b.get(key, 0))
    if result < len(A):
        result += 1
    return result


if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    result = beautifulPairs(A, B)
    print(result)
