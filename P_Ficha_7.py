#Functional Programming

# Ex 1
def divs(w, d):
    return list((map(lambda x: x/d, w))) 
divs([1, 2, 3, 4, 5], 3) # [0.3333333333333333, 0.6666666666666666, 1.0, 1.3333333333333333, 1.6666666666666667]

# Ex 2
def primeiros(w):
    return tuple(map(lambda x: x[0], w))
primeiros([[4, 5, 6, 0],[2, 3, 7, 8],[3, 4, 5, -1]]) # (4, 2, 3)

# Ex 3
def maiores_iguais_10(w):
    return list(map(lambda x: x, filter(lambda x: x >= 10, w)))
maiores_iguais_10([0, 10, -20, 45, 23, 2, 4]) # [10, 45, 23]
#or
def maiores_iguais_10(w):
    return list(filter(lambda x: x >= 10, w)) # [10, 45, 23]

# Ex 4
def soma_listas(w):
    return list(map(lambda x: sum(x), w))
soma_listas([[4, 5, 6, 0],[2, 3, 7, 8],[3, 4, 5, -1]]) # [15, 20, 11]
# or
def soma_listas(w):
    return list(map(sum, w))

# Ex 5
a = [['Joao',10],['Maria',17],['Jose',12], ['João',17]]
def media(w):
    return sum(map(lambda x: x[1], w)) / len(w)
media(a) # 14.0

def minima(w):
    return min(map(lambda x: x[1], w))
minima(a) # 10

# Ex 6
def indices_lista(w, e):
    return list(filter(lambda x: w[x] == e, range(len(w))))
indices_lista(['a', 2, 'b', 'a'], 'a') # [0, 3]

# Ex 7
def todos_aprovadosQ(w):
    return all(map(lambda x: x[1] >= 10, w))
todos_aprovadosQ([['Tomas',10],['Maria',17],['Jose',12], ['João',17]]) # False

def dezoitosQ(w):
    return any(map(lambda x: x[1] >= 18, w))
dezoitosQ([['Tomas',10],['Maria',17],['Jose',12], ['João',18]]) # True

def inscritoQ(w, s):
    return any(map(lambda x: x[0] == s, w))
inscritoQ([['Tomas',10],['Maria',17],['Jose',12], ['João',18]], 'Bia') # False

# Ex 8
def temp_media(w, t):
    return list(map(lambda x: x[0], filter(lambda x: (x[1] + x[2]) / 2 >= t, w)))
r = [('Funchal', 23, 22), ('Lisboa', 19, 15), ('Porto', 12, 14)]
temp_media(r, 16) # ['Funchal', 'Lisboa']

# Ex 9
def substitui(w, v, p):
    return list(map(lambda x: p if x == v else x, w))
substitui([1, 2, 3, 2, 4], 2, 'a') # [1, 'a', 3, 'a', 4]

# Ex 10
def conta_pares(w):
    return sum(map(lambda x: 1 if x % 2 == 0 else 0, w))
conta_pares([4, 3, 5, 1, 8]) # 2

# Ex 11
def inscritos(w):
    return list(map(lambda x: (x[0],len(x[1])), w))
inscritos([['Cálculo', ['Cátia','Maria','Vera']], ['PP', ['Joao','Maria']] ]) # [('Cálculo', 3), ('PP', 2)]

# Ex 12
from functools import reduce
def aplana(w):
    def concatena(x, y):
        return x + y
    return list(reduce(concatena, map(lambda x: x, w)))
aplana([[2,3,8],[5,6]]) # [2, 3, 8, 5, 6]

# Ex 13
def produto_impares(w):
    def prod(x, y):
        return x * y
    return reduce(prod, filter(lambda x: x % 2 != 0, w))
produto_impares([1, 2, 3, 4, -5, 6]) # -15