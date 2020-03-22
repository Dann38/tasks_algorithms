# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random
M = 7
SIZE = 2*M + 1
MIN_ITEM = 1
MAX_ITEM = 100
J = M

N = [i for i in range(MIN_ITEM, MAX_ITEM+1)]
array_random = [random.choice(N) for _ in range(SIZE)]


def my_sort(array):
    max_array = []
    for j in range(M+1):
        for k in range(SIZE):
            if k not in max_array:
                max_ = k
        for i in range(SIZE):
            if array[max_] < array[i] and i not in max_array:
                max_ = i
        max_array.append(max_)
    t = max_array.pop()
    return t, array[t]


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


index, res = my_sort(array_random)

print(array_random)
str1 = ' '*(len(str(array_random[0:index+1]))-3) + '_^_'
print(str1)

merge_sorting(array_random)
print(f'Медиана:{res} (индекс: {index})')
print('Проверка:', array_random, sep='\n')
str2 = ' '*(len(str(array_random[0:M+1]))-3) + '_^_'
print(str2)





