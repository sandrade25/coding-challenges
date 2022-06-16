import pytest
import sys
sys.path.append("../../")
from worksheets.misc.fibonnaci import fibonacci

class TestMisc:
    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(10) == 55
        assert fibonacci(20) == 6765
        assert fibonacci(79) == 14472334024676221

