def password_cracker(passwords, word):
    i = 0
    j = 1
    result = []
    size = len(word)
    while j <= size:
        if word[i:j] in passwords:
            result.append(word[i:j])
            i = j
        j += 1
    if i == j - 1:
        return ' '.join(result)
    else:
        return 'WRONG PASSWORD'


if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n = int(input())
        passwords = input().split()
        word = input()
        print(password_cracker(passwords, word))
