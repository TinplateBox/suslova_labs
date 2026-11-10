import pytest 
from num_series import simple_moving_average, exponential_moving_average

def test_sma_correctness():
    assert simple_moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]

def test_sma_invalid_window():
    with pytest.raises(ValueError): simple_moving_average([1, 2], 3)

def test_ema_correctness():
    res = exponential_moving_average([2.0, 4.0], 0.5)
    assert res == [2.0, 3.0]