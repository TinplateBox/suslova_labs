# 12 вариант

def get_float(prompt, min_val, max_val):
    while True:
        try:
            val=float(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f'ошибка: значение должно быть в диапазоне от {min_val} до {max_val}.')
        except ValueError:
            print('ошибка: введите числовое значение')

def class_tolsh(s):
    if s<2:
        return "тонкий металл"
    elif 2<=s<=8:
        return "средний металл"
    else:
        return "толстый металл"


print("расчёт параметров сварки")
print("выберите способ сварки:")
print("1 - ручная дуговая")
print("2 - MIG/MAG")
print("3 - TIG")

while True:
    try:
        choice=int(input('введите номер режима (1-3): '))
        if choice in (1, 2, 3):
            break
        else:
            print('ошибка: введите целое число.')
    except ValueError:
        print('Ошибка: введите целое число.')

match choice:
    case 1:
        method='ручная дуговая'
        k=1.0
        U=25.0
    case 2:
        method='MIG/MAG'
        k=1.15
        U=25.0
    case 3:
        method='TIG'
        k=0.85
        U=20/0

print(f'выбран способ: {method}, k={k}, U={U}')

s=get_float('введите толщину металла, мм (0.5-20.0): ', 0.5, 20.0)
v=get_float('введите скорость сварки, м/ч (5.0-80.0): ', 5.0, 80.0)
I=get_float('введите сварочный ток, А (20-400): ', 20.0, 400.0)

d_e=0.036*(I**0.5)
n=0.8
P=k*I*U*n/v
a_n=10.0
V_napl=k*I*a_n/v

class_t=class_tolsh(s)

print("\nРезультаты:")
print(f"способ сварки: {method}")
print(f"диаметр электрода = {d_e:.3f} мм")
print(f"погонная энергия = {P:.3f} (усл. ед.)")
print(f"производительность наплавки = {V_napl:.3f} г/м")
print(f"класс толщины = {class_t}")