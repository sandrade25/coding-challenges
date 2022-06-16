


"""
given a trie, get all words in the trie
"""

def get_words_from_trie(trie):
    words = []
    for k, v in trie.items():
        if k != '*':
            for el in get_words_from_trie(v):
                words.append(k + el)
        else:
            words.append('')
    return words