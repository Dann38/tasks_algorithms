# В массиве случайных целых чисел поменять
# местами минимальный и максимальный элементы.

import random

SIZE = 5
MIN_ITEM = 1
MAX_ITEM = 100

nums = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
index_max = 0
index_min = 0
max_el = nums[0]
min_el = nums[0]
print(nums)

for i in range(SIZE):
    if nums[i] < min_el:
        min_el = nums[i]
        index_min = i
    elif nums[i] > max_el:
        max_el = nums[i]
        index_max = i

nums[index_max], nums[index_min] = nums[index_min], nums[index_max]
print(nums)
