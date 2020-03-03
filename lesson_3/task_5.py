# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 20
MIN_ITEM = -9
MAX_ITEM = 9

nums = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(nums)

max_negative_num = MIN_ITEM -1
visit_log = False

for i in nums:
    if i < 0 and i > max_negative_num:
        max_negative_num = i
        visit_log = True

if visit_log:
    print(f"максимальное отрицательное  число: {max_negative_num}")
else:
    print("Нет отрицательных элементов")