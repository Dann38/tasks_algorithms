# пределить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 9

nums = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(nums)
max_q_unit = 1
max_unit = nums[0]
for i in range(MIN_ITEM, MAX_ITEM+1):
    q_unit = 0
    for j in nums:
        if i == j:
            q_unit += 1

    if q_unit > max_q_unit:
        max_q_unit = q_unit
        max_unit = i

print(f"число {max_unit} встретилось {max_q_unit} раз")