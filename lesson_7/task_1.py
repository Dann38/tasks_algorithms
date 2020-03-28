# 1). Отсортируйте ПО УБЫВАНИЮ методом пузырька одномерный ЦЕЛОЧИСЛЕННЫЙ массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random
import timeit

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
Z = [i for i in range(MIN_ITEM, MAX_ITEM+1)]
array_random = [random.choice(Z) for _ in range(SIZE)]
# print(array_random)


def bubble_sort1(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


def bubble_sort2(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1-j):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]



print(array_random)
res_time = timeit.timeit('bubble_sort1(array_random)', number=100, globals=globals())
print(f'Вариант №1\n{array_random}')
random.shuffle(array_random)
res_time2 = timeit.timeit('bubble_sort2(array_random)', number=100, globals=globals())
print(f'Вариант №2\n{array_random}')

print(f'Вариант №2 быстрее Варианта №1 в {round(res_time/res_time2, 2)} раз (на {round(res_time-res_time2, 3)} сек)')