import pytest

@pytest.fixture
def list_of_words():
    return ['you', 'your', 'cannot', 'can', 'cause', 'convey', 'corruptions', 'composition', 'create', 'first', 'for',
        'foundation', 'functions', 'familial', 'from', 'information', 'in', 'into', 'idea', 'ideas', 'is', 'important',
        'put', 'paragraphs', 'paragraph', 'particular', 'paper', 'process', 'progression', 'working', 'whole', 'where',
        'whichever', 'which', 'what', 'with', 'will', 'argument', 'are', 'as', 'an', 'and', 'any', 'about', 'all', 'a',
        'be', 'begins', 'begin', 'between', 'better', 'before', 'building', 'brainstorming', 'have', 'some', 'supports',
        'suppose', 'stage', 'statement', 'should', 'seed', 'other', 'of', 'organic', 'or', 'on', 'one', 'done',
        'development', 'develop', 'decide', 'decision', 'determine', 'many', 'mind', 'must', 'most', 'natural',
        'recurrent', 'relationship', 'relationships', 'related', 'reader', 'remind', 'keep', 'known', 'that', 'thesis',
        'the', 'there', 'this', 'techniques', 'trying', 'to', 'like', 'else', 'every', 'each', 'germination']

@pytest.fixture
def trie(list_of_words):
    tr = {}

    for word in list_of_words:
        node = tr
        for ch in word:
            node[ch] = node.get(ch, {})
            node = node[ch]
        node['*'] = {}
    return tr 

    