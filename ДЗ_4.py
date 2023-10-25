print("Задание №4")
s = input("Введите строку:")
print(s.replace(" ",""))
if s == s[::-1]:
    print("Pallindrom")
else:
    print("Ne pallindrom")


print("Задание №5")
s = input("Введите строку:")
s_1 = s.find(" ")
print(s[s_1:], s[:(s_1+1)])
print(s.replace("1", "one"))

#ДЗ
s = input("Введите строку:")
print(f"1) {s[2]}")
print(f"2) {s[-2]}")
print(f"3) {s[0:6]}")
print(f"4) {s[0:-2]}")
print(f"5) {s[::2]}")
print(f"6) {s[1::2]}")
print(f"7) {s[::-1]}")
print(f"8) {s[-1::-2]}")
print(f"9) {len(s)}")

