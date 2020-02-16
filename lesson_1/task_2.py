# https://drive.google.com/open?id=17rMdXIgyqDzSi87yiKt9C9I205-LCP2b
# Выполнить логические побитовые операции «И», «ИЛИ» и др.
# над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака.
a = 5
b = 6

and_ = a & b
or_ = a | b
xor_ = a ^ b
not_a = ~a
not_b = ~b

shift_left = a << 2
shift_right = a >> 2

print(f'and_ = {and_}')
print(f'or_ = {or_}')
print(f'xor_ = {xor_}')
print(f'not_a = {not_a}')
print(f'not_b = {not_b}')
print(f'shift_left = {shift_left}')
print(f'shift_right = {shift_right}')


