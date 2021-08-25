# Закодируйте любую строку по алгоритму Хаффмана.


class my_node():
    def __init__(self, value=None, left=None, right=None, code=None, is_parent=True):
        self.value = value
        self.left = left
        self.right = right
        self.is_parent = is_parent
        self.code = code

    def init_code(self, dictionary, code_=''):
        if self.is_parent:
            code_0 = code_+'0'
            self.left.init_code(dictionary, code_=code_0)
            code_1 = code_+'1'
            self.right.init_code(dictionary, code_=code_1)
        else:
            dictionary[self.value] = code_


def my_sort(array_key, array_sort):
    for j in range(len(array_sort)-1):
        for i in range(len(array_sort)-1-j):
            if array_sort[i] < array_sort[i+1]:
                array_sort[i], array_sort[i+1] = array_sort[i+1], array_sort[i]
                array_key[i], array_key[i+1] = array_key[i+1], array_key[i]


def create_b_tree(array_key, array_sort):
    for _ in range(len(array_sort)-1):
        array_sort.append(array_sort.pop()+array_sort.pop())

        ak1 = array_key.pop()
        if type(ak1) is str:
            ak1 = my_node(value=ak1, is_parent=False)
        ak2 = array_key.pop()
        if type(ak2) is str:
            ak2 = my_node(value=ak2, is_parent=False)

        array_key.append(my_node(None, ak1, ak2))

        n = len(array_sort) - 1
        for j in range(n):
            if array_sort[n - j-1] < array_sort[n-j]:
                array_sort[n - j-1], array_sort[n-j] = array_sort[n-j], array_sort[n-j-1]
                array_key[n - j - 1], array_key[n - j] = array_key[n - j], array_key[n - j - 1]
            else:
                break
    return array_key[0]


def my_zip(string):
    my_str = string
    spam = []
    q_spam = []

    for i in my_str:
        if i in spam:
            q_spam[spam.index(i)] += 1
        else:
            spam.append(i)
            q_spam.append(1)

    my_sort(spam, q_spam)
    tree = create_b_tree(spam, q_spam)

    dict_ = {}
    tree.init_code(dict_)

    res_str = ''
    for i in my_str:
        res_str = res_str + dict_[i]

    return dict_, res_str


def my_unzip(string, dict_):
    str_res = ''
    undict = {v: k for k, v in dict_.items()}
    spam_str = ''
    for i in string:
        spam_str = spam_str + i
        if spam_str in undict:
            str_res = str_res + undict[spam_str]
            spam_str = ''
    return  str_res

string = input("Введите текст для архивации: \n")

dict_zip, str_zip = my_zip(string)
# print(dict_zip)
print("РЕЗУЛЬТАТ")
print(str_zip)
print("\nРАСШИФРОВКА")
print(my_unzip(str_zip, dict_zip))

