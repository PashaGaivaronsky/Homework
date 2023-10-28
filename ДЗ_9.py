print("Домашнее задание")
lst = [15,48,"hello", 6, 19, "world"]
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
        if i % 2 == 0 and i > 9:
            x = str(i)
            sum = int(x[0])+int(x[1])
            print(sum) # Сумма цифр четного числа

        elif i % 2 != 0:
            lst.insert(lst.index(i), 1)
            lst.remove(i)
print(f"Согласных:{soglas},Гласных:{glas}") #Количество гласных и согласных
print(lst) # Замена всех нечетных цифр на еденицу

