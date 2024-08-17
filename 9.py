from collections import Counter

def top_n_frequent_words(filename, n):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    word_count = Counter(words)
    return word_count.most_common(n)
