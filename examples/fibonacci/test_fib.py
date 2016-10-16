import pytest
from fib import *


def test_raises_when_index_is_negative():
    with pytest.raises(ValueError):
        fib(-1)


def test_first_number_is_one():
    assert fib(0) == 1


def test_second_number_is_one():
    # Not necessary?
    assert fib(1) == 1


def test_number_is_sum_of_previous_numbers():
    assert fib(4) == fib(2) + fib(3)
