# https://drive.google.com/open?id=17rMdXIgyqDzSi87yiKt9C9I205-LCP2b
# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

num = int(input("Введите целое трехзначное число: "))

ctg1 = num//100
num = num % 100

ctg2 = num//10
num = num % 10

ctg3 = num

sum_ = ctg1 + ctg2 + ctg3
comp = ctg1 * ctg2 * ctg3

print(f'sum = {sum_}')
print(f'comp = {comp}')
