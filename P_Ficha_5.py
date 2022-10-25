# Defining recursive functions

# Ex 1
a = [64, 79, 75, 87]
def soma(w):
    if w == []:
        return 0
    else:
        return w[0] + soma(w[1:])
soma(a) # 305

# Ex 2
a = [64, 79, 75, 87]
def invert(w):
    if w == []:
        return [] # must return an empty list
    else:
        return [w[-1]] + invert(w[:-1])
invert(a) # [87, 75, 79, 64]

# Ex 3
a = (0, 23, 46, 88, 95)
def count_even(w):
    if w == ():
        return 0
    elif w[0] % 2 == 0:
        return 1 + count_even(w[1:])
    else:
       return count_even(w[1:])
count_even(a) # 3

# Ex 4
a = (0, 23, 46, 88, 95)
def t_even(w):
    if w == ():
        return ()
    elif w[0] % 2 == 0:
        return (w[0],) + t_even(w[1:])
    else:
       return t_even(w[1:])
t_even(a) # (0, 46, 88)

# Ex 5
a = [0, 23, 46, 88, 0, 95, 46]
b = [0, 1, 2, 3]
def tem_repetidos(w):
    if len(w) == 0:
        return True
    elif w[0] in w[1:]:
        return True
    else:
        return False
tem_repetidos(a) # True
tem_repetidos(b) # False

# Ex 6
a = [['Joao',10],['Maria',9],['Jose',12]]
def nomes(w):
    if w == []:
        return []
    else:
        return [w[0][0]] + nomes(w[1:])
nomes(a) # ['Joao', 'Maria', 'Jose']