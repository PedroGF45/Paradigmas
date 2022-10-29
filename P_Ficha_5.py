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
        # or return invert(w[1:]) + [w[o]]
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
        return False
    if w[0] == w[1]:
        return True
    if tem_repetidos([w[0]] + w[2:]):
        return True
    if tem_repetidos(w[1:]):
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

# Ex 7
a = [['Calculo', ['Cátia','Maria','Vera']], ['PP', ['Joao','Maria']]]
def inscritos(w):
    if w == []:
        return []
    else:
        return [len(w[0][1])] + inscritos(w[1:])
inscritos(a) # [3, 2]

# Ex 8
r = [('Funchal', [23, 22, 24, 25, 21, 22, 22]), ('Lisboa', [15, 16, 18, 18, 17, 19, 15]), ('Porto', [12, 15, 18, 14, 10, 12, 14])]
def existeQ(w, c, t):
    if w == []:
        return False
    elif c == w[0][0]:
        if t == w[0][1][-2]:
            return True
        else:
            return False
    else:
        return existeQ(w[1:], c, t)
existeQ(r, '', 21) # False
existeQ(r, 'Funchal', 21) # False
existeQ(r, 'Lisboa', 19) # True


r = [('Funchal', [23, 22, 24, 25, 21, 22, 22]), ('Lisboa', [15, 16, 18, 18, 17, 19, 15]), ('Porto', [12, 15, 18, 14, 10, 12, 14])]
def filtra(w, t):
    if w == []:
        return []
    elif ((w[0][1][-1] + w[0][1][-2]) / 2) >= t:
        return [w[0][0]] + filtra(w[1:], t)
    else:
        return filtra(w[1:], t)
filtra(r, 15.5) # ['Funchal', 'Lisboa']

# Ex 9
def maxima(w):
    if w == []:
        return 0
    elif w[0] > maxima(w[1:]):
        return w[0]
    else:
        return maxima(w[1:]) 
a = [23, 22, 24, 25, 21, 22, 22]
maxima(a) # 25

# Ex 10
def sublistas(w):
    if w == []:
        return 0
    elif isinstance(w[0], list):
        return 1 + sublistas(w[1:]) + sublistas(w[0]) # check also sublists on the first element
    else:
        return sublistas(w[1:])
a = [[1], 2, [3]]
sublistas(a) # 2       
b = [[[[[1]]]]]
sublistas(b) # 4
c = ['a', [2, 3, [[[1]], 6, 7], 'b']]
sublistas(c) # 4


# Ex 11
def filtra_numeros(w):
    def filtra_numeros_aux(r, x):
        if x == []:
            return r
        elif x[0] < 0:
            return filtra_numeros_aux (r + [x[0]], x[1:])
        else:
            return filtra_numeros_aux(r, x[1:])
    return filtra_numeros_aux([], w)
 
a = [0, -1, 2, -4, 4, 5, 6, -10]
filtra_numeros(a) # [-1, -4, -10]

# Ex 12
def filtra_numeros(w):
    def filtra_numeros_aux(i, r, x):
        if i >= len(x):
            return r
        elif x[i] < 0:
            return filtra_numeros_aux (i+1, r + [x[i]], x)
        else:
            return filtra_numeros_aux(i+1, r, x)
    return filtra_numeros_aux(0, [], w)
 
a = [0, -1, 2, -4, 4, 5, 6, -10]
filtra_numeros(a) # [-1, -4, -10]