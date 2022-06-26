


"""
given a list of words, 
make a trie
"""

def make_trie(words):
    tr = {}

    for word in words:
        node = tr
        for ch in word:
            node[ch] = node.get(ch, {})
            node = node[ch]
        node['*'] = {}
    return tr