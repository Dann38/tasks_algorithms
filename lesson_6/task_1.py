# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.

import random
import sys

size_prog = []


def read_def_in_file(name_file, size_prog):
    '''
    Просматривает код файла и находит в нем строки и целые числа, по окончании записывает размер памяти
    занимаемый этими элементами
    :param name_file: имя файла
    :param size_prog: массив куда записывать размер
    '''
    f = open(f'{name_file}.py')
    for line in f:
        for i in range(len(line)):
            if line[i] == '=' and line[i-1] == ' ' and line[i+1] == ' ':
                if line[i+2] == "'":
                    str_ = ''
                    i += 3
                    while line[i] != "'":
                        str_ = str_ + line[i]
                        i += 1
                    size_prog.append(sys.getsizeof(str_))
                    continue
                elif line[i+2] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    str_ = '0'
                    i += 3
                    while i != len(line):
                        str_ = str_ + str(line[i])
                        i += 1

                    num = int(str_)
                    size_prog.append(sys.getsizeof(num))
                    continue
                else:
                    continue


def size_list(l, res_list):
    res_list.append(sys.getsizeof(l))
    for i in l:
        res_list.append(sys.getsizeof(i))
        if isinstance(i, list):
            size_list(i, res_list)


SIZE = 2000
MIN_ITEM = 0
MAX_ITEM = 900

nums0 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
nums1 = [random.randint(MIN_ITEM*2, MAX_ITEM*2) for _ in range(SIZE*2)]
nums2 = [random.randint(MIN_ITEM*4, MAX_ITEM*4) for _ in range(SIZE*4)]
nums3 = [random.randint(MIN_ITEM*8, MAX_ITEM*8) for _ in range(SIZE*8)]
all_nums = [nums0, nums1, nums2, nums3]

# считаем размер списков
size_list(all_nums, size_prog)


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


# Вариант2
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


# Вариант3
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


read_def_in_file('task_1', size_prog)
print(sum(size_prog))
