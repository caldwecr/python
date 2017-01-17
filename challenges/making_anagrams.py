from functools import reduce

def number_needed(a, b):
    letters = {}
    for l in a:
        letters[l] = letters[l] + 1 if l in letters and letters[l] else 1

    for l in b:
        letters[l] = letters[l] - 1 if l in letters and letters[l] else -1

    return reduce(lambda x, y: abs(x) + abs(y), letters.values(), 0)
