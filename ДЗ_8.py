print("Задание №5")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True


print("Задание №6")
import random
def mass(m):
    n =[]
    x = 0
    for i in m:
        x += i
        n.append(i)
    res = x / len(n)
    return res
mass(random.randint(1,10)for a in range(10))

print('Домашнее задание')
def calculator(num_1,oper,num_2):
    if oper == "+":
        res =(num_1 + num_2)
    elif oper == "-":
        res = (num_1 - num_2)
    elif oper == "*":
        res = (num_1 * num_2)
    elif oper == "/" and num_2 == 0:
        res = ("На ноль делить нельзя")
    elif oper == "/":
        res = (num_1 / num_2)
    else:
        res = ("Ошибка в правильности выбора операции")
    return res