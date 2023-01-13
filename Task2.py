# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('equation1.txt', 'r') as data:
    st1 = data.read()
print(st1)

with open('equation2.txt', 'r') as data:
    st2 = data.read()
print(st2)

def koef(st: str):
    st = st.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -')
    st = st.split()
    new_list = []
    for item in st:
        if item.startswith('x'):
            new_list.append(1)
        elif item.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(item.split('*x')[0])

    return new_list


koef1 = koef(st1)
koef1 = [int (x) for x in koef1]
koef2 = koef(st2)
koef2 = [int (x) for x in koef2]

def completing_a_dictionary(koef):
    my_dictionary = {}
    my_count = len(koef) - 1
    for i in range(len(koef)):
        my_dictionary[my_count] = koef[i]
        my_count -= 1
    return my_dictionary

my_dictionary1 = completing_a_dictionary(koef1)
my_dictionary2 = completing_a_dictionary(koef2)

min_dict = len(my_dictionary1)
max_dict = len(my_dictionary2)

if len(my_dictionary1) > len(my_dictionary2):
    min_dict = len(my_dictionary2)
    max_dict = len(my_dictionary1)

my_dictionary3 = {}
for key in range(min_dict):
    if key < min_dict:
        my_dictionary3[key] = my_dictionary1[key] + my_dictionary2[key]
    else:
        my_dictionary3[key] = my_dictionary2[key]
my_list = []
for v in my_dictionary3.values():
    my_list.append(str(v))
my_list.reverse()

def equation(my_list):

    my_equation = []
    k = len(my_list)-1
    for i in range(len(my_list)):
        if my_list[i] == 0:
            k -= 1
        elif k == 0:
            my_equation.append(my_list[i])
            k -= 1
        elif k == 1:
            my_equation.append(f'{my_list[i]} * x')
            k -= 1
        else:
            my_equation.append(f'{my_list[i]} * x ** {k}')
            k -= 1

    equation = ''

    for i in range(len(my_equation)):
        equation += my_equation[i]
        if i < len(my_equation) - 1:
            if '-' in my_equation[i + 1]:
                equation += ' '
            elif i < len(my_equation) - 1:
                equation += ' + '
        elif i == len(my_equation) - 1:
            equation += ' = 0'
    
    return equation

print(equation(my_list))