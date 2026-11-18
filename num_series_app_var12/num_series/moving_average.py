
import time 
from collections import deque 
from typing import List, Sequence 

def check_window(window, n):
    if not isinstance(window, int) or window < 1:
        raise ValueError("окно должно быть целым числом >= 1")
    if window > n:
        raise ValueError("окно не может превышать длину ряда")

def simple_moving_average(data, window):
    check_window(window,len(data))
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def exponential_moving_average(data, alpha):
    if not (0 < alpha <= 1):
        raise ValueError("коэффициент альфа должен быть в диапазоне (0, 1]")
    result = [data[0]]
    for i in range(1, len(data)):
        ema_val = alpha*data[i] + (1 - alpha)*result[i - 1]
        result.append(ema_val)
    return result

def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]: 
    """SMA с использованием deque (двусторонней очереди).""" 
    check_window(window, len(data)) 
    result = [] 
    d = deque() 
    running_sum = 0.0 
    for x in data: 
        d.append(x) 
        running_sum += x 
        if len(d) > window: 
            running_sum -= d.popleft() 
        if len(d) == window: 
            result.append(running_sum / window) 
    return result 

def calculate_mse(original: Sequence[float], sma: Sequence[float], window: int) -> float:
    """расчёт среднеквадратичной ошибки между исходным рядом и sma"""
    if not sma:
        return float('inf')
    squared_errors = []
    for i in range(window - 1, len(original)):
        sma_idx = i - (window - 1)
        error = original[i] - sma[sma_idx]
        squared_errors.append(error**2)
    return sum(squared_errors) / len(squared_errors)