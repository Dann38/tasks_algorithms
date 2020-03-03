# В диапазоне натуральных чисел от 2 до 99
# определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.
MIN_ITEM = 2
MAX_ITEM = 99

nums = {i for i in range(MIN_ITEM, MAX_ITEM+1)}
resolt = [0]*8

for i in range(0, 8):
    for j in nums:
        if j % (i+2) == 0:
            resolt[i] += 1
    print(f'{i+2} > {resolt[i]}')
