# https://drive.google.com/open?id=1suBUcJGygvtxpJnDTD-9SckHgJpGl0nC
# Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486, надо вывести
# 6843.

def len_int(num):
    n = 1
    while True:
        num = num // 10
        if num == 0:
            return n
        n += 1


def print_reflex(num, n1): #пришлось делать проверку на нули
    n = len_int(num)
    if n == 1:
        print(num, end='')
    else:
        k1 = num // 10**(n-1)
        num = num % 10**(n-1)
        print_reflex(num, n-1)
        print(k1, end='')
        if n != n1: #сама проверка на нули
            print('0'*(n1-n), end='')


num = int(input("Введите число: "))
print_reflex(num, len_int(num))