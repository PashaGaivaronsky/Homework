print("Домашнее задание")
lst = [15,48,"hello", 6, 19, "world",]
summ = []
glas = 0
soglas = 0
for i in lst:
    if type(i) == str:
        y = str(i)
        for b in y:
            if b == 'a' or b == 'e' or b == 'i' or b == 'o' or b == 'u':
                glas += 1
            else:
                soglas += 1
    else:
        if i % 2 == 0:
            x = str(i)
            num = map(int,x)
            s = sum(num)
            summ.append(s)
        elif i % 2 != 0:
            lst.insert(lst.index(i), 1)
            lst.remove(i)
print(summ)# Сумма цифр четного числа
print(f"Согласных:{soglas},Гласных:{glas}") #Количество гласных и согласных
print(lst) # Замена всех нечетных цифр на еденицу

