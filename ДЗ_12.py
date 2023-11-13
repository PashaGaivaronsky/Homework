print("Задание №6")
import math
def sum_number(n):
    n = int(n)
    summ = n + (math.pow(n,2)) + (math.pow(n,3))
    return summ
sum_number(2)

print("Задание №6.2")
import random
import math
x = random.randint(-10, 10)
def num(x):
    if -5 <= x <= 5:
        y = math.pow(x, 2)
        return y
    elif x < -5:
        y = 2 * abs(x)-1
        return y
    elif x > 5:
        y = 2 * x
        return y
    else:
        pass
num(x)

print("Домашнее задание")
tpl = (2, 3, "world", 6, 78,"hello")
lst = [2, 3, "world", 6, 78, "hello"]
number = 213456127849
string = "hello world"
def test(x):
    if type(x) == tuple:
        new_str = ""
        new_lst = list(x)
        for i in new_lst:
            if type(i) == str:
                new_str += i
        long = len(new_str)
        return f"длинна слов в кортеже:{long}"
    elif type(x) == list:
        num = 0
        let = 0
        for i in x:
            if type(i) == int:
                num += 1
                continue
            else:
                for j in str(i):
                    let += 1
                continue
        return f"сумма букв:{let},сумма цифр:{num}"
    elif type(x) == int:
        count_num = 0
        num_str = str(x)
        for num in num_str:
            if int(num) % 2 != 0:
                count_num += 1
        return f"количество нечетных цифр:{count_num}"
    elif type(x) == str:
        count_let = len([let for let in x if let.isalpha()])
        return f"количество букв в строке:{count_let}"

print(test(tpl),"\n",test(lst),"\n",test(number),"\n",test(string),"\n")




