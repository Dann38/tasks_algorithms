# https://drive.google.com/open?id=17rMdXIgyqDzSi87yiKt9C9I205-LCP2b
# Написать программу, которая генерирует в указанных пользователем
# границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся
# эти символы. Программа должна вывести на экран любой символ алфавита от
# 'a' до 'f' включительно.
import random

print('можно использовать цифры(0-9) и буквы(a-z)')
from_ = input('генерировать от: ')
to_ = input('генерировать до: ')
r = random.random() #случайное число от 0 до 1

if from_.isnumeric() and to_.isnumeric():
    to_ = float(to_)
    from_ = float(from_)

    num2 = r*((to_ - from_)+1)+from_
    num1 = int(num2)

    print(f'num1={num1}')
    print(f'num2={num2}')
else:
    from_ = ord(from_)
    to_ = ord(to_)

    simbol = r * ((to_ - from_)+1) + from_
    simbol = chr(int(simbol))

    print(f'simbol={simbol}')