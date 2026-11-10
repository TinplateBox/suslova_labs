from __future__ import annotations 
 
import argparse 
import csv
import sys 
from typing import List, Optional, Tuple
 
from num_series import ( 
 random_series, sine_series, trend_series, 
 summarize, 
 simple_moving_average, centered_moving_average, 
 exponential_moving_average, save_series_json, load_series_auto,
) 
# --------------------------------------------------------------------------- 
# Фабрика ряда 
# --------------------------------------------------------------------------- 
 
def build_series(kind: str, n: int, seed: int) -> List[float]: 
 """Возвращает числовой ряд заданного типа. 
 
 kind = "random" — равномерное распределение на [-50, 50]; 
 kind = "sine"  — синусоида с амплитудой 10, частотой 2 и шумом 1.5; 
 kind = "trend" — линейный тренд с шагом 1.0 и шумом 0.5. 
 """ 
 if kind == "random": 
  return random_series(n, low=-50, high=50, seed=seed) 
 if kind == "sine": 
  return sine_series(n, amplitude=10, frequency=2, noise=1.5, seed=seed) 
 if kind == "trend": 
  return trend_series(n, start=0, step=1.0, noise=0.5, seed=seed) 
 raise ValueError(f"Неизвестный тип ряда: {kind!r}") 

def obtain_series(args: argparse.Namespace) -> Tuple[List[float], str]: 
    """Возвращает (ряд, описание источника).""" 
    if args.load: 
        data = load_series_auto(args.load) 
        return data, f"файл: {args.load}" 
    data = build_series(args.kind, args.n, args.seed) 
    return data, f"сгенерирован ({args.kind}, n={args.n}, seed={args.seed})"
 
# --------------------------------------------------------------------------- 
# Печать 
# --------------------------------------------------------------------------- 
def export_series_csv(path: str, data: List[float]) -> None: 
    """Экспорт ряда в CSV: столбцы i, value. Ошибки нормализуются в ValueError.""" 
    try: 
        with open(path, "w", newline="", encoding="utf-8") as f: 
            w = csv.writer(f) 
            w.writerow(["i", "value"]) 
            for i, v in enumerate(data): 
                w.writerow([i, v]) 
    except OSError as err: 
        raise ValueError(f"Не удалось записать CSV {path}: {err}") from err
    
def print_series(title: str, values: List[float], fmt: str = "{:>10.3f}") -> None: 
 """Печатает ряд в одну строку с выравниванием.""" 
 print(f"\n{title} (n={len(values)}):") 
 formated_values = [fmt.format(v) if v is not None else "      None" for v in values]
 print(" " + " ".join(formated_values)) 
 
def print_header(kind: str, n: int) -> None: 
 print("=" * 60) 
 print(f"Тип ряда: {kind}, n = {n}") 
 print("-" * 60) 
 
def print_stats(stats: dict) -> None: 
 """Печатает блок базовых статистических показателей.""" 
 print(f"Среднее арифметическое : {stats['mean']:>10.4f}") 
 print(f"Медиана    : {stats['median']:>10.4f}") 
 print(f"Размах (max - min)  : {stats['spread']:>10.4f}") 
 print(f"min / max    : {stats['min']:>10.4f} / {stats['max']:.4f}") 
 
def print_footer() -> None: 
 print("=" * 60) 
 
# --------------------------------------------------------------------------- 
# Разбор аргументов 
# --------------------------------------------------------------------------- 
 
def build_parser() -> argparse.ArgumentParser: 
    parser = argparse.ArgumentParser( 
        description="Алгоритмическая обработка числовых рядов", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
        epilog="Пример: python main.py --kind sine --n 20 --save data/s.json", 
    ) 
    # источники 
    parser.add_argument("--kind", choices=["random", "sine", "trend"], default="sine", 
                        help="тип генерируемого ряда") 
    parser.add_argument("--n", type=int, default=20, 
                        help="количество точек в ряде") 
    parser.add_argument("--seed", type=int, default=42, 
                        help="зерно ГПСЧ для воспроизводимости") 
    parser.add_argument("--load", metavar="PATH", 
                        help="загрузить ряд из файла (.json/.txt/.csv); " 
                             "отменяет --kind/--n/--seed") 
    # экспорт 
    parser.add_argument("--save", metavar="PATH", 
                        help="сохранить ряд в JSON-файл") 
    parser.add_argument("--export", metavar="FILE", 
                        help="экспортировать ряд в CSV (i, value)") 
    # анализ 
    parser.add_argument("--window", type=int, default=3, 
                        help="размер окна для скользящей средней") 
    parser.add_argument("--alpha", type=float, default=0.3, 
                        help="коэффициент сглаживания для EMA, 0 < alpha <= 1") 
    return parser 
 
# --------------------------------------------------------------------------- 
# main 
# --------------------------------------------------------------------------- 
 
def main(argv: Optional[List[str]] = None) -> int: 
    args = build_parser().parse_args(argv) 
 
    # --- 1. Получаем ряд --- 
    try: 
        data, source = obtain_series(args) 
    except ValueError as err: 
        print(f"Ошибка получения ряда: {err}", file=sys.stderr) 
        return 1 
 
    # --- 2. Сохраняем (до анализа — данные на диске даже при ошибке анализа) --- 
    if args.save: 
        meta = {"source": source} 
        if not args.load: 
            meta.update({"kind": args.kind, "seed": args.seed}) 
        try: 
            save_series_json(data, args.save, meta=meta) 
            print(f"[сохранено] {args.save} ({len(data)} точек)") 
        except ValueError as err: 
            print(f"Ошибка сохранения: {err}", file=sys.stderr) 
            return 1 
 
    if args.export: 
        try: 
            export_series_csv(args.export, data) 
            print(f"[экспортировано] {args.export} ({len(data)} точек)") 
        except ValueError as err: 
            print(f"Ошибка экспорта: {err}", file=sys.stderr) 
            return 1 
 
    # --- 3. Анализ --- 
    try: 
        stats = summarize(data) 
        sma = simple_moving_average(data, args.window) 
        ema = exponential_moving_average(data, args.alpha) 
        cma = ( 
            centered_moving_average(data, args.window) 
            if args.window % 2 == 1 else None 
        ) 
    except ValueError as err: 
        print(f"Ошибка анализа: {err}", file=sys.stderr) 
        return 1 
 
    # --- 4. Вывод --- 
    print_header(source) 
    print_stats(stats) 
 
    print_series("Исходный ряд", data) 
    print_series(f"SMA (window={args.window})", sma) 
    print_series(f"EMA (alpha={args.alpha})", ema) 
    if cma is not None: 
        print_series(f"Центрированное MA (window={args.window})", cma) 
 
    print_footer() 
    return 0 
 
if __name__ == "__main__": 
 raise SystemExit(main())