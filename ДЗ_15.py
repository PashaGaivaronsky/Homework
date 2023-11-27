import json
import demjson3

def mrkt():
    name_product_lst = []
    cost_product_lst = []
    a = 0
    while a != "стоп":
        name_product = input("название продукта:")
        cost_product = input("стоимость продукта:")
        a = input("'enter'для продолжения ,'стоп' для выхода с программы:")
        name_product_lst.append(name_product)
        cost_product_lst.append(cost_product)
    dict_name = dict.setdefault("название",name_product)
    dict_cost = dict.fromkeys(["стоимость"],cost_product)
    return dict_name, dict_cost

with open("market.json","w",encoding="utf-8") as f:
    json.dump(mrkt(), f, ensure_ascii=False)

mrkt()
