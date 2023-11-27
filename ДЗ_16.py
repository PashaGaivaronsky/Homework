while True:
    string = input("Введите данные:")
    for i in string.split():
        if i.isdigit():
            try:
                res = int(string.split()[0]) / int(string.split()[1])
                print(res)
            except ZeroDivisionError:
                print("Деление на ноль!!!")
            except ValueError:
                print("Введено не цифровое значение")
        break
    break









