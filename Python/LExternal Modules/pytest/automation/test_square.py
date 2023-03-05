import pytest
import math


@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.square
def testsquare():
    num = 7
    math.pow(num, 2) == 49


@pytest.mark.others
def testequality():
    assert 10 == 11
