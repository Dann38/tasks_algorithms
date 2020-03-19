import sys
from task_1 import read_def_in_file as test

size = []
a = 456
b = 'aaaaaa'
print(sys.getsizeof(a)+sys.getsizeof(b))
test('test', size)
print(sum(size))