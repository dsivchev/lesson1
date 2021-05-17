# Functions - Задание 1
def get_summ(one, two, delimiter='&'):
    result = str(one) + delimiter + str(two)
    return result

p = get_summ('Learn', 'python')
print(p)
print(p.upper())
