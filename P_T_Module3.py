# Alternative Composition
from itertools import count


a = 7
if a > 5: # True
# print(2 * a) # Indentation error: expected idented block 
    print(2 * a) # 14

b = 9
c = 16
if b < 9: # False
    c = 2 * b
    print(c)
elif b + c < 25: # False
    c = b + c
    print(c)
else: # Then True
    c = 2 * c
    print(c) # 32

# Functions
def cubo(x):
    x = x ** 3 
    print(x)
cubo(2) # 8
cubo(5-2) # 27

def f(x): # defining functions by branches
    if x < 0:
        x = x ** 2
        print(x)
    else:
        cubo(x) # calling function cubo with return x ** 3
f(-1) # 1
f(0) # 0
f(2) # 8

# or

def f_alternative(x):
    return x ** 2 if x < 0 else x ** 3

# Function with 3 branches
def h(x):
    if x < 0:
        return -5
    elif x >= 20:
        return x ** 2
    else:
        return x + 7
h(1) # 8
h(-1) # -5
h(30) # 900

# Example of finding a max number given 2 numbers
def maximo(x, y):
    if x < y:
        return y
    else:
        return x
maximo(2, 4) # 4

# Some functions might be in our interested to have no arguments (when we want constants)
def c():
    return 20
c() # invoking integer with value 20

# Defining a function C which receiving a list with tuples will return a list with the number
# of elements of each of the tuples
a = [(5, 4, 2), ((3, 4), 8), (5,), (), (7, 8, (9, 5))]
def countElements(lista):
    return [len(x) for x in lista] # when x is each element of the list - take the lenght of that element and form a list
countElements(a) # [3, 2, 1, 0, 3]

# Define a function 'la' of which receiving a sheet from a subject returns a tuple with the names of the
# students on the sheet
studentsGrades = [{'nome': 'antonio', 'nota': 10},
                {'nome': 'maria', 'nota': 17},
                {'nome': 'felisberta', 'nota': 1}]
def la(list):
    return tuple(x['nome'] for x in studentsGrades) # when x is each element of the dictionary / take the value of the key 'nome'
la(studentsGrades) # ('antonio', 'maria', 'felisberta')

# Define a function 'la' which creates a tuple with only the grades of each student
studentsGrades = [('Ana', 14), ('Joao', 7), ('Jose', 18)]
def la(list):
    return tuple(x[1] for x in list)
la(studentsGrades) # (14, 7, 18)

# Define a function which creates a list of dictionaries of the form [{'nome': x, 'nota': y}]
def generateDict(list):
    return [{'nome': x[0], 'nota': x[1]} for x in list]
generateDict(studentsGrades) # [{'nome': 'Ana', 'nota': 14}, {'nome': 'Joao', 'nota': 7}, {'nome': 'Jose', 'nota': 18}]

# Define a function f which receiving a sheet, returns a diciontary in the form {'name': 'apr'/'repr'}
studentsGrades = [('Joao', 10), ('Mario', 4), ('Ana', 18)]
def f(sheet):
    return {x[0]: ('apr' if x[1] >= 10 else 'rep') for x in sheet}
f(studentsGrades)
