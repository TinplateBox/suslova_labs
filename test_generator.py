import pytest 
from num_series import random_series, sine_series, trend_series

def test_random_series_lenght():
    assert len(random_series(10)) == 10

def test_random_series_invalid_n():
    with pytest.raises(ValueError):
        random_series(-5)

def test_sine_series_bounds():
    data = sine_series(10, amplitude=1.0, noise=0.0)
    assert all(-1.0 <= x <= 1.0 for x in data)
