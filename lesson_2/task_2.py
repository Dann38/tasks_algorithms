# https://drive.google.com/open?id=1suBUcJGygvtxpJnDTD-9SckHgJpGl0nC
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2
# нечетные (3 и 5).

def len_int(num):
    n = 1
    while True:
        num = num // 10
        if num == 0:
            return n
        n += 1


def num_i(i, num):
    n = num % 10**i
    n = n // 10**(i-1)
    return n


num = int(input("Введите натуральное число: "))

n = len_int(num)

even = 0
odd = 0

while n > 0:
    i = num_i(n, num)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    n -= 1

print(f'четных: {even} нечетных: {odd}')


