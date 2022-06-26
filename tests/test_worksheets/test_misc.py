import pytest
import sys
sys.path.append("../../")
import random
from worksheets.misc.fibonnaci import fibonnaci
from worksheets.misc.make_trie_from_words import make_trie
from worksheets.misc.get_words_from_trie import get_words_from_trie
from worksheets.misc.longest_common_substring import longest_common_substring
from protected.worksheets_answers.misc.fibonnaci import fibonnaci as fibonnaci_a
from protected.worksheets_answers.misc.make_trie_from_words import make_trie as make_trie_a
from protected.worksheets_answers.misc.get_words_from_trie import get_words_from_trie as get_words_from_trie_a
from protected.worksheets_answers.misc.longest_common_substring import longest_common_substring as longest_common_substring_a



class TestMisc:
    def test_fibonacci(self):
        assert fibonnaci(5) is not None, "solution not yet provided"

        assert fibonnaci_a(5) is not None
        assert fibonnaci(0) == fibonnaci_a(0) == 0
        assert fibonnaci(1) == fibonnaci_a(1) == 1
        assert fibonnaci(2) == fibonnaci_a(2) == 1
        assert fibonnaci(10) == fibonnaci_a(10)
        assert fibonnaci(20) == fibonnaci_a(20)
        assert fibonnaci(79) == fibonnaci_a(79)

    def test_make_trie(self, list_of_words):
        random_list_1 = random.choices(list_of_words, k=10)
        random_list_2 = random.choices(list_of_words, k=10)
        random_list_3 = random.choices(list_of_words, k=10)
        assert make_trie(random_list_1) is not None, "solution not yet provided"

        assert make_trie_a(random_list_1) is not None
        assert make_trie(random_list_1) == make_trie_a(random_list_1)
        assert make_trie(random_list_2) == make_trie_a(random_list_2)
        assert make_trie(random_list_3) == make_trie_a(random_list_3)

    def test_get_words_from_trie(self, trie):
        user = get_words_from_trie(trie)
        answer = get_words_from_trie_a(trie)
        assert user is not None, "solution not yet provided"

        assert answer is not None
        assert user == answer

    def test_longest_common_subtring(self, list_of_words):
        words = [
            random.choices(list_of_words, k=2),
            random.choices(list_of_words, k=2),
            random.choices(list_of_words, k=2)
        ]
        for word_group in words:
            user = longest_common_substring(word_group[0], word_group[1])
            answer = longest_common_substring_a(word_group[0], word_group[1])
            assert user is not None, "solution not yet provided"

            assert answer is not None
            assert user == answer





