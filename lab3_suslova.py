# variant 12

#1 задача
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


#2 задача
def task_2():
    p=0
    while p<=20:
        r=2**p
        print(f"2^{p} = {r}")
        p+=1

choise=get_int('выберите задачу (1 или 2): ', min_v=1, max_v=2)
match choise:
    case 1:
        task_1()
    case 2:
        task_2()