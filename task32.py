# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n = int(input("Введите количество элементов: "))
min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))
list_1 = [randint(-10,10) for i in range(n)]
print(*list_1)

for i in range(len(list_1)):
    if list_1[i] in range(min,max + 1):
        print(i)