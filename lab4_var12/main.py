
from validation import input_s, input_v, input_i
from menu import show_menu, select_mode, mode_name
from operations import elect_diam, heat_inp, depos_rate, thick_class

def main() -> None:
    """Главный сценарий."""
    print("=== Расчёт праметров сварки ===")
    while True:
        show_menu()
        k = select_mode()
        if k is None:
            print("Работа завершена.")
            break

        s = input_s()
        v = input_v()
        i = input_i()

        d_e = elect_diam(i)
        is_tig = (k==0.85)
        p = heat_inp(k, i, v, is_tig)
        v_dep = depos_rate(k, i, v)
        cls = thick_class(s)

        print("\n Результаты ")
        print(f"Способ сварки: {mode_name(k)} (k = {k})")
        print(f"d_e (диаметр электрода): {d_e:.2f} мм")
        print(f"П (погонная энергия): {p:.2f}")
        print(f"V_напл (производительность): {v_dep:.2f} г/ч")
        print(f"Класс толщины: {cls}")
        print("\n")
        
if __name__ == "__main__":
    main()