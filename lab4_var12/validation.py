
from __future__ import annotations
from constants import S_MIN, S_MAX, V_MIN, V_MAX, I_MIN, I_MAX
from logger import log_error

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""

def input_number(prompt: str, low: float, high: float) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue
        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)

def input_s() -> float:
    return input_number(
        "Введите толщину металла s, мм (0,5..20): ",
        S_MIN, S_MAX,
    )

def input_v() -> float:
    return input_number(
        "Введите скорость сварки v, м/ч (5..80): ",
        V_MIN, V_MAX,
    )

def input_i() -> float:
    return input_number(
        "Введите сварочный ток I, A (20..400): ",
        I_MIN, I_MAX,
    )