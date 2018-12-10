def check_magazine(magazine, note):
    count = {}
    for word in magazine:
        count[word] = count.get(word, 0) + 1

    for word in note:
        if count.get(word, 0) > 0:
            count[word] -= 1
        else:
            return 'No'
    return 'Yes'
