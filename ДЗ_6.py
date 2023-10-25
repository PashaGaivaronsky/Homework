print("Задание №1")
x = 1
for i in range(1,31):
    if i % 2 != 0:
        x *=i
        print(x)

print("Задание №2")
x =[]
for i in range(1,101):
    if i % 5 == 0:
        x.append (i)
print(x)

print("Задание №3")
for i in range(1,72):
    if i % 2 == 0:
        print(i)

print("Задание №4")
import random
x = [random.randint(1,30) for a in range(30)]
print(x)
y = []
for i in x:
    for j in x:
        if i == j and x.count(i) > 2 :
            if i not in y:
                y.append(i)
print("***********************************")
print(y)

print("Творческое задание")
# Разбейте список по типу элементов(int,float,str)
m = ["1",0.25,"hello",23,"11",0.44,57,"world",11]
s = []; n = []; f = []
for i in m:
    if type(i) == int:
        n.append(i)
    elif type(i) == float:
        f.append(i)
    elif type(i) == str:
        s.append(i)
print(s);print(n);print(f)