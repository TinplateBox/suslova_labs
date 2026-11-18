
from typing import Dict, Sequence 

def _ensure_not_empty(data: Sequence[float]) -> None: 
  if not data: 
    raise ValueError("Ряд пуст: расчёт статистики невозможен")
  
def mean(data: Sequence[float]) -> float: 
  """Среднее арифметическое.""" 
  _ensure_not_empty(data) 
  return sum(data) / len(data) 
 
def median(data: Sequence[float]) -> float: 
  """Медиана (устойчива к выбросам).""" 
  _ensure_not_empty(data) 
  s = sorted(data) 
  k = len(s) // 2 
  if len(s) % 2: 
    return float(s[k]) 
  return (s[k - 1] + s[k]) / 2.0 

def spread(data: Sequence[float]) -> float: 
  """Размах ряда: max - min.""" 
  _ensure_not_empty(data) 
  return float(max(data) - min(data)) 

def variance(data: Sequence[float]) -> float:
  """выборочная дисперсия (вариант 1)"""
  _ensure_not_empty(data)
  if len(data) < 2:
    return 0.0
  m = mean(data)
  return sum((x - m) ** 2 for x in data) / (len(data) - 1)

def stdev(data: Sequence[float]) -> float:
  """выборочное стандартное отклонение (вариант 1)"""
  return (variance(data))**0.5

 
def summarize(data: Sequence[float]) -> Dict[str, float]: 
  """Сводный отчёт: count, mean, median, spread, min, max.""" 
  _ensure_not_empty(data) 
  return { 
    "count": len(data), 
    "mean": mean(data), 
    "median": median(data), 
    "spread": spread(data), 
    "variance": variance(data),
    "stdev": stdev(data),
    "min": float(min(data)), 
    "max": float(max(data)), 
  } 