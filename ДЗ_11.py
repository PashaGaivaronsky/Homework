print("Задание №1")
cort = tuple(i for i in range(10))
sum_cort = sum(cort)
print(sum_cort)

print("Задание №2")
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
long_word_lst = list(long_word)
new_word_lst = []
count_word = []
for i in long_word_lst:
 if long_word_lst.count(i) not in count_word:
  count_word.append(long_word_lst.count(i))
 for j in long_word_lst:
  if i == j and long_word_lst.count(i) > 1:
   if i not in new_word_lst:
    new_word_lst.append(i)
dict_1 = dict(zip(new_word_lst,count_word))
print(dict_1)

long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
long_word_set = set(long_word)
for i in long_word_set:
 print(i, long_word.count(i))


print("Задание №3")
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))

