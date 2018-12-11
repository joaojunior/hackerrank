def make_anagrams(a, b):
    d_a = {}
    d_b = {}
    qty = 0
    for c in a:
        d_a[c] = d_a.get(c, 0) + 1
    for c in b:
        d_b[c] = d_b.get(c, 0) + 1
    for c, frequency in d_a.items():
        qty += abs(frequency - d_b.get(c, 0))
    for c, frequency in d_b.items():
        if c not in d_a:
            qty += frequency
    return qty
