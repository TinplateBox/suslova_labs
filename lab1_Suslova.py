# import math as m
# # 13 вариант

# # 1 задача
# '''
# a=float(input ('Введите переменную a:'))
# z=float(input ('Введите переменную z:'))
# z2=z**2
# za=((z2)+a)**0.5
# mlogz=m.log(z)
# x=(za)/(a*mlogz)
# x2=x**2
# xa=((x2)+a)**0.5
# b=m.log(x*(xa))
# print("x={0:.2f}".format(x))
# print("b={0:.2f}".format(b))
# '''
# # 2 задача

# a=float(input ('Введите сторону a:'))
# b=float(input ('Введите сторону b:'))
# c=float(input ('Введите сторону c:'))

# if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:

#     p=(a+b+c)/2
#     s=(p*(p-a)*(p-b)*(p-c))**0.5

#     r=s/p
#     Svp=(m.pi)*(r**2)

#     R=(a*b*c)/(4*s)
#     Sop=(m.pi)*(R**2)

#     otn=Sop/Svp
#     print("otn={0:.2f}".format(otn))
# else:
#     print('нет такого треугольника')


# Задание 8
from math import *
x = float(input("Введите переменную x: "))
a = float(input("Введите переменную a: "))
c = 1.35
d = 0.87
Y = sqrt(e**(x + 1) + x)
x = (a + d)/(c * d) * sin(c*d)
a = log(c + sin(d)**2)
print("Y = {0:.2f}".format(Y))
print("x = {0:.2f}".format(x))
print("a = {0:.3f}".format(a))
