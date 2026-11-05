# variant 12

# 1 задача
def get_class(p, min_v=None):
    while True:
        try:
            v=int(input(p))
            if min_v is not None and v<min_v:
                print(f"ошибка: кол-во учеников должно быть не меньше {min_v}")
                continue
            return v
        except ValueError:
            print('ошибка: введите целое число учеников без посторонних символов')

def get_int(p, min_v=None, max_v=None):
    while True:
        try:
            v=int(input(p))
            if min_v is not None and v<min_v or max_v is not None and v>max_v:
                print(f"ошибка: число должно быть не меньше {min_v} и не больше {max_v}")
                continue
            return v
        except ValueError:
            print('ошибка: введите целое число без посторонних символов')

def task_1():
    k=get_class('введите кол-во учеников в каждом классе: ', min_v=1)
    sum_1=0
    sum_2=0

    print("\nвведите оценки 1 класса: ")
    for i in range(k):
        grade=get_int(f"введите оценку {i+1} ученика 1 класса: ", min_v=1, max_v=5)
        sum_1+=grade

    print("\nвведите оценки 2 класса: ")
    for i in range(k):
        grade=get_int(f"введите оценку {i+1} ученика 2 класса: ", min_v=1, max_v=5)
        sum_2+=grade

    sr_1=sum_1/k
    sr_2=sum_2/k

    print(f"\nсредняя оценка в 1 классе: {sr_1:.2f}")
    print(f"средняя оценка во 2 классе: {sr_2:.2f}")


# 2 задача
def task_2():
    p=0
    while p<=20:
        r=2**p
        print(f"2^{p} = {r}")
        p+=1

# 3 задача
import string
def task_3():
    stroka=input('введите строку: ')

    for c in string.punctuation:
        stroka=stroka.replace(c,' ')

    slova=stroka.split()
    print('\nслова, которые заканчиваются на "я": ')
    f=False
    for s in slova:
        s=s.lower()
        if s[-1]=='я':
            print(s)
            f=True
    if f==False:
        print('таких слов не найдено')

# 4 задача
# нечётными могут быть только целые числа!
def task_4():
    numbers = []
    print("Вводите целые числа по одному (для завершения введите 'stop'):")

    while True:
        user_input = input("Введите число: ")
        if user_input.lower() == 'stop':
            break
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
           print("Ошибка. Введите целое число или 'stop'.")

    odd_num = [x for x in numbers if x % 2 != 0]

    if not odd_num:
        print("В списке нет нечетных чисел (или список пуст).")
    else:
        small_odd = min(odd_num)
        print(f"Наименьший нечетный элемент: {small_odd}")

# 5 задача
import ast

def get_array(name):
    arr = []
    print(f"\nВведите 10 элементов для массива {name}:")
    while len(arr) < 10:
        user_in = input(f"Элемент {len(arr) + 1} из 10: ").strip()
        user_in = user_in.replace(',','.')
        try:
            elem = ast.literal_eval(user_in)
            arr.append(elem)
        except (ValueError, SyntaxError):
            if user_in and not user_in.startswith(('"',"'")):
                arr.append(user_in)
            else:
                print("Ошибка. Проверьте ввод, строки берите в кавычки")
    return arr

def task_5():
    A = get_array('A')
    B = get_array('B')
    print(f"\nИсходный массив A: {A}")
    print(f"Исходный массив B: {B}")

    A_2 = [x for x in A]
    A = [x for x in B]
    B = [x for x in A_2] 

    print("\nРезультат:")
    print(f"Преобразованный массив A: {A}")
    print(f"Преобразованный массив B: {B}")


# выбор задачи
choise=get_int('выберите задачу: ', min_v=1, max_v=5)
match choise:
    case 1:
        task_1()
    case 2:
        task_2()
    case 3:
        task_3()
    case 4:
        task_4()
    case 5:
        task_5()
