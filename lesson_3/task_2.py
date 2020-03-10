# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10

nums = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
index_even = []

for i in range(0, SIZE):
    if nums[i] % 2 == 0:
        index_even.append(i)

print(nums)
print(index_even)
