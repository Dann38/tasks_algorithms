# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random
import timeit

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array_random = [random.random()*(MAX_ITEM-MIN_ITEM) for _ in range(SIZE)]


def merge_sorting(array):
    if len(array) == 1:
        return
    l1 = len(array)//2
    array_left = array[:l1]
    array_rigth = array[l1:]
    l2 = len(array_rigth)
    merge_sorting(array_left)
    merge_sorting(array_rigth)
    j = 0
    k = 0
    for i in range(len(array)):
        if array_left[j] < array_rigth[k]:
            array[i] = array_left[j]
            j += 1
            if l1 == j:
                for i_ in range(i+1, len(array)):
                    array[i_] = array_rigth[k]
                    k += 1
                return
        else:
            array[i] = array_rigth[k]
            k += 1
            if l2 == k:
                for i_ in range(i+1, len(array)):
                    array[i_] = array_left[j]
                    j += 1
                return


def bubble_sort2(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1-j):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


print(array_random)

res_time2 = timeit.timeit('bubble_sort2(array_random)', number=100, globals=globals())
random.shuffle(array_random)
res_time = timeit.timeit('merge_sorting(array_random)', number=100, globals=globals())

print(f'Вариант merge_sorting  быстрее bubble_sort2 в {round(res_time/res_time2, 2)} раз (на {round(res_time-res_time2, 3)} сек)')
print(f'Результат сортировки: \n{array_random}')