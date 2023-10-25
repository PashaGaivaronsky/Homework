print("Задание №1")
ann_app = 2
pol_app = 5
print(f'Pol have {pol_app} apples,Ann have {ann_app} apples')

print("Задание №2")
import math
side_cube = float(input("Введите длину ребра куба:"))
v = math.pow(side_cube, 3)
s = (4*(math.pow(side_cube, 2)))
print(f"Объем куба = {v}")
print(f'Площадь боковой поверхности куба = {s}')

print("Задание №3")
day_m = 2
night_m = -1
full_day = day_m + night_m
tree_h = 20
res = tree_h // full_day
print(f"Количество дней = {res}")

print("Творческое задание")
#Напишите программу для вычисления площади и периметра квадрата со случайным значение стороны квадрата от 1 до 10.
import math
import random
side = random.randint(1,10)
print(f"Сторона квадрата = {side}")
s = math.pow(side,2)
p = side*4
print(f"Периметр квадрата = {p},Площадь квадрата = {s}")