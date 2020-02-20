# https://drive.google.com/open?id=1suBUcJGygvtxpJnDTD-9SckHgJpGl0nC
# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

def get_S_n(b1, q, n):
    S_n = b1*(q**n - 1) / (q-1)
    return S_n

n = int(input("Введите число элементов: "))
n2 = n // 2
if n % 2 == 0:
    n1 = n2
else:
    n1 = n2+1
S_n1 = get_S_n(1, 0.25, n1)
S_n2 = get_S_n(0.5, 0.25, n2)

S_n = S_n1 - S_n2
print(f'S_n = {S_n}')