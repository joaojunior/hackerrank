def alternating_characters(s):
    qty = 0
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        qty += j - i - 1
        i = j
    return qty
