# https://drive.google.com/open?id=17rMdXIgyqDzSi87yiKt9C9I205-LCP2b
# По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))

if x1 != x2:
    k = (y2-y1)/(x2-x1)
    b = y1-x1*k
    print(f'y={k}x+{b}')
else:
    print('Решения нет')
