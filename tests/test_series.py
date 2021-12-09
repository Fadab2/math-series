
from math_series.series import fibonacci, lucas, sum_series
import pytest

# fibonacci test
def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_fib_fifteen():
    actual = fibonacci(15)
    expected = 600
    assert actual != expected


# lucas test
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_ten():
    actual = lucas(10)
    expected = 123
    assert actual == expected

def test_lucas_fifteen():
    actual = lucas(15)
    expected = 1263
    assert actual != expected

# test sum_series
def test_sum_series_default_args():
    actual = sum_series(10)
    expected = 55
    assert actual == expected

def test_sum_series_with_two_and_one():
    actual = sum_series(10, 2, 1)
    expected = 123
    assert actual == expected

def test_sum_series_with_specific_args():
    actual = sum_series(4, 3, 6)
    expected = [3, 6, 9, 15]
    assert actual == expected