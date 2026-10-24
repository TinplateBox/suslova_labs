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

# выбор задачи
choise=get_int('выберите задачу: ', min_v=1, max_v=3)
match choise:
    case 1:
        task_1()
    case 2:
        task_2()
    case 3:
        task_3()