# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² +  *x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k1 = int(input('Введите введите натуральную степень k1 : '))
k2 = int(input('Введите введите натуральную степень k2 : '))

def equation(k: int):

    my_list = []
    
    for _ in range(k):
        number = random.randint(-100, 100)
        if number == 0:
            continue
        elif k == 1:
            my_list.append(f'{number} * x')            
        else:
            my_list.append(f'{number} * x ** {k}')
        k -= 1
    number = random.randint(-100, 100)
    my_list.append(f'{number}')
    equation = ''
    for i in range(len(my_list)):
        equation += my_list[i]
        if i < len(my_list) - 1:
            if '-' in my_list[i + 1]:
                equation += ' '
            elif i < len(my_list) - 1:
                equation += ' + '
        elif i == len(my_list) - 1:
            equation += ' = 0'

    return equation

with open('equation1.txt', 'w', encoding = 'UTF-8') as data:
    data.write(equation(k1))

with open('equation2.txt', 'w', encoding = 'UTF-8') as data:
    data.write(equation(k2))