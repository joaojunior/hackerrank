def find_largest_word(words, target):
    words = sorted(words, key=len, reverse=True)
    for word in words:
        i = 0
        j = 0
        while i < len(word) and j < len(target):
            if word[i] == target[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(word):
            return word


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        quantity_words = int(input())
        words = input().split()
        target = input()
        print(find_largest_word(words, target))
