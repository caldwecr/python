from collections import Counter

def ransom_note(magazine, ransom):
    """Returns true if every string in ransom is also present in magazine"""
    magazine_words = Counter(magazine)
    ransom_words = Counter(ransom)
    magazine_words.subtract(ransom_words)
    return all([w >= 0 for w in magazine_words.values()])