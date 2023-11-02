# print("задание №4")
# diction = {a : a+1 for a in range(5)}
# prod_of_val = 1
# for k , v in diction.items():
#     prod_of_val *= v
# print(prod_of_val)

# print("задание №5")
# l = [ a+1 for a in range(10)]
# l_2 = [a for a in range(10,30,2)]
# dictionary = dict(zip(l,l_2))
# print(dictionary)

# print("задание №6")
# wrd = "pythonist"
# keys = []
# value = []
# for i in wrd:
#     keys.append(i)
#     value.append(wrd.count(i))
# dictionary = (dict(zip(keys,value)))
# print(keys)
# print(value)
# print(dictionary)
# # Не понимаю куда пропадает последняя t в словаре

print("Домашнее задание")
price_mrkt = {"milk":["2",100],"sugar":["2",50],"salt":["1",30],"bread":["1",20]}
for k,v in price_mrkt.items():
    count = v[1]
    price = v[0]
    price_mrkt = f"{k} - {f'{price} - {count}'}"
    print(price_mrkt)
name_prdcts = []
count_prdcts = []
bskt =0
x = 0
while x != "n":
    name_prdct = input("Введите название продукта:")
    if name_prdct == "milk":
        name_prdcts.append("milk")
        prc_prdct = 2
    elif name_prdct == "bread":
        name_prdcts.append("bread")
        prc_prdct = 1
    elif name_prdct == "salt":
        name_prdcts.append("salt")
        prc_prdct = 1
    elif name_prdct == "sugar":
        name_prdcts.append("sugar")
        prc_prdct = 2
    else:
        print("Выбранного товара нету в наличии")
        continue
    count_prdct = int(input("Количество товара:"))
    if name_prdct == "milk":
        blnc = 100
        count_prdcts.append(blnc - count_prdct)
        if count_prdct > blnc:
            print("Указанного кол-ва товара в наличии нету")
            continue
    elif name_prdct == "bread":
        blnc = 20
        count_prdcts.append(blnc - count_prdct)
        if count_prdct > blnc:
            print("Указанного кол-ва товара в наличии нету")
            continue
    elif name_prdct == "salt":
        blnc = 30
        count_prdcts.append(blnc - count_prdct)
        if count_prdct > blnc:
            print("Указанного кол-ва товара в наличии нету")
            continue
    elif name_prdct == "sugar":
        blnc = 50
        count_prdcts.append(blnc - count_prdct)
        if count_prdct > blnc:
            print("Указанного кол-ва товара в наличии нету")
            continue
    total = prc_prdct * count_prdct
    bskt += total
    print(f"Сумма к оплате :{total}")
    x = input("Чтобы выбрать следующий товар нажмите любую клавишу,чтобы выйти из магазина нажмите 'n':")
print(f"Итоговая сумма к оплате : {bskt}")
blnc_market = (dict(zip(name_prdcts,count_prdcts)))
print(f"Остаток:{blnc_market}")




