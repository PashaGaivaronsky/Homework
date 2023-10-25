
print("Домашнее задание!!!")
import random
x = ("c")
while x == ("c"):
 num_comp = random.randint(1,10)
 num_color = random.randint(1,2)
 if num_color == 1:
     num_color = ("black")
 elif num_color == 2:
     num_color = ("red")
 num_h = int(input("Введите число от 1 до 10:"))
 if num_h > 10 or num_h < 0:
     print("Вы выбрали неверное число,попробуйте еще раз")
     continue
 color_h = input("Выберите цвет: red или black:")
 if color_h != "red" and color_h != "black":
     print("Вы указали неверный цвет,попробуйте еще раз")
     continue
 if num_h == num_comp and color_h == num_color:
         print("Поздравляем,вы выиграли!")
 else:
     print("Повезет в другой раз")
 print(f"Число компьютера:{num_comp}, Цвет:{num_color}")
 x = input("Если хотите попробовать еще раз нажмите 'c',чтобы закончить нажмите любую клавишу: ")

print("Задание №6")
x = 'c'
while x == 'c':
 num_1 = float(input("Введите первое число:"))
 oper = str(input("Выберите операцию:+,-,*,/:"))
 num_2 = float(input("Введите второе число:"))
 if oper == "+":
    print(num_1 + num_2)
 elif oper == "-":
    print(num_1 - num_2)
 elif oper == "*":
    print(num_1 * num_2)
 elif oper == "/" and num_2 == 0:
    print("На ноль делить нельзя")
 elif oper == "/":
    print(num_1 / num_2)
 else:
    print("Ошибка в правильности выбора операции")
 x = input("Eсли желаете завершить операцию, нажмите '0',чтобы продолжить 'c' ")

print("Задание №4")
num_1 = int(input("Введите отрицательное число:"))
num_2 = int(input("Введите положительное число:"))
while num_1 < num_2:
    print(num_1)
    num_1 += 1
    if num_1 == 0:
        break




