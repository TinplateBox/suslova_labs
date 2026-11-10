import pytest 
from num_series import mean, median, spread, summarize

def test_mean():
    assert mean([1, 2, 3]) == 2.0

def test_median_odd():
    assert median ([3, 1, 2]) == 2.0

def test_median_even():
    assert median ([1, 2, 3, 4]) == 2.5

def test_spread():
    assert spread([10, 2, 5]) == 8.0

def test_empty_series():
