import pytest
import sys
sys.path.append("../../")
from worksheets.misc.fibonnaci import fibonnaci

class TestMisc:
    def test_fibonacci(self):
        assert fibonnaci(0) == 0
        assert fibonnaci(1) == 1
        assert fibonnaci(2) == 1
        assert fibonnaci(10) == 55
        assert fibonnaci(20) == 6765
        assert fibonnaci(79) == 14472334024676221

