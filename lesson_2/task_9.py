# https://drive.google.com/open?id=1suBUcJGygvtxpJnDTD-9SckHgJpGl0nC
# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def len_int(num):
    n = 1
    while True:
        num = num // 10
        if num == 0:
            return n
        n += 1


def get_sum_el(num):
    n = len_int(num)
    if n == 1:
        return num
    else:
        k1 = num // 10**(n-1)
        num = num % 10**(n-1)
        k2 = get_sum_el(num)
        sum = k1 + k2
        return sum


max_ = int(input("Введите числа (по окончании нажмите дважды ENTER)\n"))
sum_max = get_sum_el(max)

num = input('')
while num != '':
    num = int(num)
    sum_num = get_sum_el(num)
    if sum_num > sum_max:
        sum_max = sum_num
        max_ = num
    num = input()


print(f'Максимальная сумма {sum_max} у числа {max_}')
