# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import random
import timeit
import cProfile


n1 = 20
n2 = 40
n3 = 80
n4 = 160

def re_er(n1):
    n = n1**2
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        print(m)
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b[n1-1]


def prime(k):
    i = 1
    num = 2

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True

    while k != i:
        num += 1
        if is_prime(num):
            i += 1

    return num

#переделанное Решето Эратосфена работает как O(N**2)
print(timeit.timeit('re_er(n1)', number=100, globals=globals()))  # 0.018233597998914775
print(timeit.timeit('re_er(n2)', number=100, globals=globals()))  # 0.06685210499927052
print(timeit.timeit('re_er(n3)', number=100, globals=globals()))  # 0.23032468800010975
print(timeit.timeit('re_er(n4)', number=100, globals=globals()))  # 1.0154066840004816

print(cProfile.run('re_er(n1)'))   #82 function calls in 0.000 seconds
print(cProfile.run('re_er(n2)'))  #255 function calls in 0.001 seconds
print(cProfile.run('re_er(n3)'))  #838 function calls in 0.002 seconds
print(cProfile.run('re_er(n4)'))  #2822 function calls in 0.009 seconds

#обычная проверка работает как O(N!)
print(timeit.timeit('prime(n1)', number=100, globals=globals()))  # 0.007364836998021929
print(timeit.timeit('prime(n2)', number=100, globals=globals()))  # 0.02171156600161339
print(timeit.timeit('prime(n3)', number=100, globals=globals()))  # 0.07882094699743902
print(timeit.timeit('prime(n4)', number=100, globals=globals()))  # 0.3851455160001933

print(cProfile.run('prime(n1)'))   #73 function calls in 0.000 seconds
print(cProfile.run('prime(n2)'))  #175 function calls in 0.000 seconds
print(cProfile.run('prime(n3)'))  #411 function calls in 0.001 seconds
print(cProfile.run('prime(n4)'))  #943 function calls in 0.004 seconds
