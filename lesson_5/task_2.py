# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections

hex_ = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
    "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15
}
dex_ = {
    10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
}


def print_expression(a, operation, b, c):
    a = get_hex(a)
    b = get_hex(b)
    c = get_hex(c)
    la = len(a)
    lb = len(b)
    lc = len(c)
    if la == 1 and lb == 1:
        print(a,operation, b, "=", c)
        return
    print(" "*(lc-la), operation, a, sep='')
    print(" "*(lc-lb+1), b, sep='')
    print(" ", "-"*lc, sep='')
    print(" ", c, sep='')
    return


def get_hex(num_array):
    str_ = ''
    start = True
    for i in num_array:
        if start and i == 0:
            continue
        else:
            start = False
        if i in dex_:
            str_ = str_ + dex_[i]
        else:
            str_ = str_ + str(i)
    return str_


def add_(num_array1, num_array2):
    a = num_array1.copy()
    b = num_array2.copy()
    a.reverse()
    b.reverse()

    la = len(a)
    lb = len(b)

    if la < lb:
        a.extend([0]*(lb-la))
        max_len = lb

    else:
        b.extend([0]*(la-lb))
        max_len = la
    c = collections.deque()
    remains = 0
    for i in range(max_len):
        number = a[i]+b[i]+remains
        remains = 0
        if number > 15:
            remains = number // 16
            number = number % 16
        c.append(number)
    if remains != 0:
        c.append(remains)
    return reversed(c)


def mul_(num_array1, num_array2):
    if len(num_array1) > len(num_array2):
        a = num_array1
        b = num_array2
    else:
        a = num_array2
        b = num_array1
    a.reverse()
    b.reverse()
    b.append(0)
    a.append(0)

    c = collections.deque([0])
    remains = 0
    for i in range(len(a)):
        for j in range(len(b)):
            number = b[j]*a[i]+remains
            remains = 0
            if number > 15:
                remains = number // 16
                number = number % 16
            if j+i > len(c)-1:
                c.append(number)
            else:
                number = c[j+i] + number
                if number > 15:
                    remains = remains + number // 16
                    number = number % 16
                c[j+i] = number
    b.pop()
    a.pop()
    c.pop()
    return reversed(c)

expression = input('Введите пример(операции "+" или "*" без пробела):\n')
a = collections.deque()
b = collections.deque()

c = a
for i in expression:
    if i == "*" or i == "+":
        operation = i
        c = b
    else:
        c.append(hex_[i])
        # a.append(hex_[i.upper()])

if operation == "*":
    c = mul_(a, b)
elif operation == "+":
    c = add_(a, b)

print_expression(a, operation, b, c)
