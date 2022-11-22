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
    return sum(map(lambda x: x[1], w)) / len(a)
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
    return all(map(lambda x: x[1] > 10, w))
todos_aprovadosQ([['Tomas',10],['Maria',17],['Jose',12], ['João',17]]) # False