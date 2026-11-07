
from __future__ import annotations
from constants import K_1, K_2, K_3

def show_menu() -> None:
    print("\n Выберите способ сварки:")
    print(" 1 — ручная дуговая  (k = 1.0)")
    print(" 2 — MIG/MAG (k = 1.15)")
    print(" 3 — TIG (k = 0.85)")
    print(" 0 — выход")

def select_mode() -> float | None:
    while True:
        choice = input("Введите номер режима (от 0 до 3): ").strip()
        match choice:
            case "1": return K_1
            case "2": return K_2
            case "3": return K_3
            case "0": return None
            case _: print("Ошибка: неверный пункт меню. Повторите ввод.")

def mode_name(k: float) -> str:
    match k:
        case 1.0: return "ручная дуговая"
        case 1.15: return "MIG/MAG"
        case 0.85: return "TIG"
        case _: return "неизвестный"