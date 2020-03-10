# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

import random
import timeit
import cProfile

SIZE = 2000
MIN_ITEM = 0
MAX_ITEM = 900

nums = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
nums1 = [random.randint(MIN_ITEM*2, MAX_ITEM*2) for _ in range(SIZE*2)]
nums2 = [random.randint(MIN_ITEM*4, MAX_ITEM*4) for _ in range(SIZE*4)]
nums3 = [random.randint(MIN_ITEM*8, MAX_ITEM*8) for _ in range(SIZE*8)]


# Вариант1
def frequent_num(nums):
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
    return max_unit, max_q_unit


def frequent_num2(nums):
    item_array = {
        '_': float('-inf')
    }
    max_q = '_'
    for i in nums:
        if i in item_array:
            item_array[i] += 1
            if item_array[i] > item_array[max_q]:
                max_q = i
        else:
            item_array[i] = 1
    if max_q == '_':
        return None, None
    return max_q, item_array[max_q]



def frequent_num3(nums):
    item_array = {
        '_': float('-inf')
    }
    for i in nums:
        if i in item_array:
            item_array[i] = item_array[i] + 1
        else:
            item_array[i] = 1
    max_q = '_'
    for i in item_array:
        if item_array[i] > item_array[max_q]:
            max_q = i
    if max_q == '_':
        return None, None
    return max_q, item_array[max_q]






# ВАРИАНТ 1 О(N)
print(timeit.timeit('frequent_num(nums)', number=100, globals=globals()))  # 4.1582901980000315
print(timeit.timeit('frequent_num(nums1)', number=100, globals=globals()))  # 8.0436241110001
print(timeit.timeit('frequent_num(nums2)', number=100, globals=globals()))  # 15.395211061000737
print(timeit.timeit('frequent_num(nums3)', number=100, globals=globals()))  # 33.14110618700033


print(cProfile.run('frequent_num(nums)'))   #1    0.044    0.044    0.044    0.044 task_1.py:24(frequent_num)
print(cProfile.run('frequent_num(nums1)'))  #1    0.087    0.087    0.087    0.087 task_1.py:24(frequent_num)
print(cProfile.run('frequent_num(nums2)'))  #1    0.165    0.165    0.165    0.165 task_1.py:24(frequent_num)
print(cProfile.run('frequent_num(nums3)'))  #1    0.330    0.330    0.330    0.330 task_1.py:24(frequent_num)

# ВАРИАНТ 2 О(N) но быстрее предыдущего O2(133*N) = 01(N)
print(timeit.timeit('frequent_num2(nums)', number=100, globals=globals()))  # 0.03126329800034
print(timeit.timeit('frequent_num2(nums1)', number=100, globals=globals()))  # 0.057844230001137475
print(timeit.timeit('frequent_num2(nums2)', number=100, globals=globals()))  # 0.12785812599940982
print(timeit.timeit('frequent_num2(nums3)', number=100, globals=globals()))  # 0.25562749299933785

print(cProfile.run('frequent_num2(nums)'))   #1    0.000    0.000    0.000    0.000 task_1.py:39(frequent_num2)
print(cProfile.run('frequent_num2(nums1)'))  #1    0.001    0.001    0.001    0.001 task_1.py:39(frequent_num2)
print(cProfile.run('frequent_num2(nums2)'))  #1    0.001    0.001    0.001    0.001 task_1.py:39(frequent_num2)
print(cProfile.run('frequent_num2(nums3)'))  #1    0.003    0.003    0.003    0.003 task_1.py:39(frequent_num2)


# ВАРИАНТ 3 О(N), работает быстрее при малом разбросе чисел, т.к. проще пробежать по количесту каждых чисел и узнать 
# какое из них самое большое, а не проверять при прибавление нового повторяющего числа. 

print(timeit.timeit('frequent_num3(nums)', number=100, globals=globals()))  # 0.022806988999946043
print(timeit.timeit('frequent_num3(nums1)', number=100, globals=globals()))  # 0.0473409990008804
print(timeit.timeit('frequent_num3(nums2)', number=100, globals=globals()))  # 0.10336040500078525
print(timeit.timeit('frequent_num3(nums3)', number=100, globals=globals()))  # 0.21897145799994178

print(cProfile.run('frequent_num3(nums)'))   #1    0.000    0.000    0.000    0.000 task_1.py:57(frequent_num3)
print(cProfile.run('frequent_num3(nums1)'))  #1    0.000    0.000    0.000    0.000 task_1.py:57(frequent_num3)
print(cProfile.run('frequent_num3(nums2)'))  #1    0.001    0.001    0.001    0.001 task_1.py:57(frequent_num3)
print(cProfile.run('frequent_num3(nums3)'))  #1    0.002    0.002    0.002    0.002 task_1.py:57(frequent_num3)


#Все алгоритмы имеют линейную зависимость, но первый зависит линейно от двух оргументов, а 2-й и 3-й, только от длины 
# чисел, при этом, если диапозон маленький лучше подойдет 3-й, а если он большой, то лучше 2-й
