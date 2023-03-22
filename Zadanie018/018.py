# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# Создание списка чисел
from random import randint
list = []
listLength = int(input("Введите размер массива (кол-во элементов)  "))

for i in range(listLength):
    list.append(randint(1, 10))
print()
print(list)
print()

# Поиск ближайшего по величине элемента в массиве
number = int(input("Введите число "))
result = (number+1)*1000
digit = 0

for i in range(len(list)):
    if (abs(number-list[i])) < result:
        result = abs(number-list[i])
        digit = list[i]

print(f"Число {digit} в массиве ближайшее к числу {number} ")
