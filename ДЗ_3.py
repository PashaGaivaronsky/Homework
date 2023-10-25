side_1 = int(input("Введите первое значение стороны треугольника:"))
side_2 = int(input("Введите второе значение стороны треугольника:"))
side_3 = int(input("Введите третье значение стороны треугольника:"))
if (side_1 + side_2) > side_3 and (side_2 + side_3) > side_1 and (side_3 + side_1) > side_2:
    print("треугольник существует")
else:
    print("треугольника с такими значениями не существует")
#
num_1 = float(input("Введите первое число:"))
oper = str(input("Выберите операцию:+,-,*,/:"))
num_2 = float(input("Введите второе число:"))
if oper == "+":
    print(num_1 + num_2)
elif oper == "-":
    print(num_1 - num_2)
elif oper == "*":
    print(num_1 * num_2)
elif oper == "/":
    print(num_1 / num_2)
else:
    print("Ошибка в правильности выбора операции")


word = input("Введите слово:")
is_mister = (word == "Mister")
print(is_mister)

print("Выберите цвет доспехов:red,yellow,black")
armor = input(":")
print("Выберите цвет щита:red,yellow,black")
shield = input(":")
res = (armor == "yellow" or "black" and shield == "black")
print(res)


print("Задание №1")
import random
num_user =int(input("Введите число от 1 до 10:"))
num_comp = random.randint(1,10)
print("Выигрышное чиcло",num_comp)
if num_comp == num_user:
    print("Поздравляем, вы выиграли!!!")
else:
    print("В другой раз повезет")

print("Задание №2")
day = int(input("Введите число рождения:"))
month = int(input("Введите месяц рождения:"))
if day >= 21 and month == 3 or day <= 20 and month == 4:
    print("Oven")
elif day >= 21 and month == 4 or day <= 20 and month == 5:
    print("Telec")
elif day >= 21 and month == 5 or day <= 21 and month == 6:
    print("Blizneci")
elif day >= 22 and month == 6 or day <= 22 and month == 7:
    print("Rak")
elif day >= 23 and month == 7 or day <= 23 and month == 8:
    print("Lev")
elif day >= 24 and month == 8 or day <= 23 and month ==9:
    print("Deva")
elif day >= 24 and month == 9 or day <= 23 and month == 10:
    print("Vesi")
elif day >= 24 and month == 10 or day <= 22 and month == 11:
    print("Skorpion")
elif day >= 23 and month == 11 or day <= 21 and month == 12:
    print("Strelec")
elif day >= 22 and month == 12 or day <= 20 and month == 1:
    print("Kozerog")
elif day >= 21 and month == 1 or day <= 20 and month == 2:
    print("Vodoley")
elif day >= 21 and month == 2 or day <= 20 and month == 3:
    print("Riba")
else:
    print("Жаль др не будет(((")

print("Творческое задание")
sum_1 = float(input("Введите баланс на карте:"))
cost_ticket = "0.9р"
print("Стоимость билета:",cost_ticket)
cost_ticket = 0.90
quantity_ticket = int(input("Введите количество билетов к покупке:"))
sum_2 = sum_1 - float(quantity_ticket * cost_ticket)
if sum_1 < sum_2:
       print("Недостаточно средств")
elif sum_2 < 0:
       print("Недостаточно средств")
else:
       print(f"Остаток на балансе:{sum_2}")
