import pytest
import sys
sys.path.append("../../")
from worksheets.misc.fibonnaci import fibonnaci
from worksheets_answers.misc.fibonnaci import fibonnaci as fibonnaci_a

class TestMisc:
    def test_fibonacci(self):
        assert fibonnaci(5) is not None
        assert fibonnaci(0) == fibonnaci_a(0)
        assert fibonnaci(1) == fibonnaci_a(1)
        assert fibonnaci(2) == fibonnaci_a(2)
        assert fibonnaci(10) == fibonnaci_a(10)
        assert fibonnaci(20) == fibonnaci_a(20)
        assert fibonnaci(79) == fibonnaci_a(79)

