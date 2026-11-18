from __future__ import annotations
import argparse
import sys
from typing import List

from num_series import (
    random_series, summarize,
    simple_moving_average, simple_moving_average_deque,
    exponential_moving_average, calculate_mse
)

def build_series(n: int, seed: int | None = None, negative_test: bool = False) -> List[float]:
    """Генерация ряда (вариант 1)"""
    if negative_test:
        # Краевой кейс из В1: генерация отрицательных чисел
        return random_series(n, low=-100.0, high=100.0, seed=seed)
    else:
        # Стандартная генерация: [0, 100)
        return random_series(n, low=0.0, high=100.0, seed=seed)

def print_header(n: int, is_negative: bool) -> None:
    print("=" * 70)
    mode = "[-100, 100) (Краевой кейс В1)" if is_negative else "[0, 100)"
    print(f"Ряд: n = {n}, равномерное распределение {mode}")
    print("-" * 70)

def print_stats(stats: dict) -> None:
    print(f"Среднее арифметическое : {stats['mean']:>10.4f}")
    print(f"Медиана : {stats['median']:>10.4f}")
    print(f"Размах (max - min) : {stats['spread']:>10.4f}")
    print(f"Дисперсия (выборочная): {stats['variance']:>10.4f}")
    print(f"СКО (std deviation) : {stats['stdev']:>10.4f}")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Вариант 12 (на базе Варианта 1)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--n", type=int, default=500, help="количество точек")
    # несколько окон 
    parser.add_argument(
        "--window", type=int, nargs='+', default=[10],
        help="размеры окон для SMA (например: --window 5 10 20)"
    )
    parser.add_argument("--seed", type=int, default=42, help="зерно ГПСЧ")
    # Краевой кейс В1
    parser.add_argument("--negative", action="store_true", help="тест с отрицательными числами (В1)")
    return parser

def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        data = build_series(args.n, args.seed, args.negative)
        stats = summarize(data)
    except ValueError as err:
        print(f"Ошибка: {err}", file=sys.stderr)
        return 1

    print_header(args.n, args.negative)
    print_stats(stats)
    
    # Краевой кейс из В12: обработка списка окон
    valid_windows = []
    for w in args.window:
        if w <= 0:
            print(f"\n[Предупреждение В12] Окно {w} <= 0 пропущено.", file=sys.stderr)
        elif w > args.n:
            print(f"\n[Предупреждение В12] Окно {w} > длины ряда ({args.n}) пропущено.", file=sys.stderr)
        else:
            valid_windows.append(w)

    if not valid_windows:
        print("\nОшибка: не осталось валидных окон для расчета.", file=sys.stderr)
        return 1

    # поиск лучшего окна по MSE
    print("\n--- Скользящие средние (SMA list & deque, EMA) ---")
    best_window = None
    min_mse = float('inf')
    
    for w in valid_windows:
        sma_list = simple_moving_average(data, w)
        sma_deque = simple_moving_average_deque(data, w)
        assert sma_list == sma_deque, "Ошибка реализации: list и deque дали разный результат"
        
        # EMA из В1
        alpha = 2.0 / (w + 1)
        ema = exponential_moving_average(data, alpha)
        
        mse = calculate_mse(data, sma_list, w)
        print(f"Окно {w:>2}: MSE = {mse:.4f}, EMA alpha = {alpha:.3f}")
        
        if mse < min_mse:
            min_mse = mse
            best_window = w

    print("-" * 70)
    if best_window:
        print(f"ЛУЧШЕЕ ОКНО (min MSE): {best_window} (MSE = {min_mse:.4f})")
        
        # Вывод
        w = best_window
        alpha = 2.0 / (w + 1)
        best_sma = simple_moving_average(data, w)
        best_ema = exponential_moving_average(data, alpha)
        
        print(f"\nПервые 10 значений исходного ряда:")
        print(" " + " ".join(f"{v:>8.2f}" for v in data[:10]))
        print(f"\nПервые 10 значений SMA (окно {w}):")
        print(" " + " ".join(f"{v:>8.2f}" for v in best_sma[:10]))
        print(f"\nПервые 10 значений EMA (alpha={alpha:.2f}):")
        print(" " + " ".join(f"{v:>8.2f}" for v in best_ema[:10]))

    print("=" * 70)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())