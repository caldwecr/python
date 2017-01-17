def number_needed(a, b):
    """ Returns the number of characters you must delete to make the two strings anagrams of each other """
    letters = {}
    for l in a:
        letters[l] = letters[l] + 1 if l in letters and letters[l] else 1

    for l in b:
        letters[l] = letters[l] - 1 if l in letters and letters[l] else -1

    return sum([abs(x) for x in letters.values()])
