print("Домашнее задание №17")
class Data:
    def __init__(self, x):
        self.x = x
    def len_str(self):
        if type(self.x) == str:
            lenn = len(self.x)
        elif type(self.x) == int:
            lenn = len(str(self.x))
        return lenn

    def str_1(self):
        vowels = 0
        cons = 0
        str_vowels = []
        str_cons = []
        summ = 0
        if type(self.x) == str:
            for j in self.x:
                if j in "aeiou":
                    vowels += 1
                    str_vowels.append(j)
                elif j in "bcdfghjklmnpqrstvwxyz":
                    cons += 1
                    str_cons.append(j)
            if (vowels * cons) <= self.len_str():
                return str_vowels
            else:
                return str_cons
        elif type(self.x) == int:
            lst = list(str(self.x))
            for i in lst:
                if int(i) % 2 == 0:
                    summ += int(i)
            return summ * self.len_str()

oper = Data(1234)
print(oper.str_1())





