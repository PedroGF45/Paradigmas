# Imperative 

# Ex 1
def soma_quadrados_while(n):
    i = 0
    r = 0
    while i <= n:
        r = r + i*i
        i += 1
    return r

def soma_quadrados_for(n):
    r = 0
    for i in range(n+1):
        r = r + i*i
        i += 1
    return r
a = 5
soma_quadrados_for(a) # 55
soma_quadrados_for(a) # 55

# Ex 2
def indices_lista(w, e):
    i = 0
    r = []
    while i < len(w):
        if w[i] == e:
            r = r + [i]
        i += 1
    return r
indices_lista(['a', 2, 'b', 'a'], 'a') # [0, 3]

# Ex 3
def filtra_pares_while(t):
    x = 0
    r = ()
    while x < len(t):
        if (t[x] % 2 == 0):
            r = r + (t[x],)
        x += 1
    return r  

def filtra_pares_for(t):
    r = ()
    for i in range(len(t)):
        if (t[i] % 2 == 0):
            r = r + (t[i],)
    return r
a = (81, 55, 80, 62, 49) 
filtra_pares_while(a) # (80, 62)
filtra_pares_for(a) # (80, 62)

# Ex 4
def maximo(w):
    i = 0
    r = w[0]
    while i < (len(w) - 1):
        if w[i] > w[i+1]:
            r = w[i]
        i += 1
    return r
maximo([-3, -1, -8]) # -1

# Ex 5
def substitui(w, v, p):
    i = 0
    r = []
    while i < len(w):
        if w[i] == v:
            r = r + [p]
        else:
            r = r + [w[i]]
        i += 1
    return r
substitui ([1, 2, 3, 2, 4], 2, 'a') # [1, 'a', 3, 'a', 4]

# Ex 6
def unico(t):
    i = 0
    r = ()
    while i < len(t):
        if t[i] not in r:
            r = r + (t[i],)
        i += 1
    return r
unico((2, 4, 3, 2, 2, 2, 3)) # (2, 4, 3)

# Ex 7
def intercala_while(t1, t2):
    i = 0
    r = ()
    while i < len(t1):
        r = r + (t1[i],) + (t2[-i-1],)
        i += 1
    return r
intercala_while((6,0,2,8,9), (1,4,7,6,3)) # (6, 3, 0, 6, 2, 7, 8, 4, 9, 1)
def intercala_for(t1, t2):
    r = ()
    for i in range(len(t1)):
        r = r + (t1[i],) + (t2[-i-1],)
    return r
intercala_for((6,0,2,8,9), (1,4,7,6,3)) # (6, 3, 0, 6, 2, 7, 8, 4, 9, 1)

# Ex 8
def palindromoQ(w):
    i = 0
    r = True
    while i < (len(w) / 2): 
        if w[i] == w[-i-1]:
            r = True
        else:
            r = False
        i += 1
    return r
palindromoQ(['r','a','d','a','r']) # True

# Ex 9
def soma_positivos(w):
    i = 0
    r = 0
    while i < len(w):
        if w[i] > 0:
            r = r + w[i]
        i += 1
    return r
soma_positivos([4, 3, 5, -1, -8]) # 12

# Ex 10
def num_pares_igual_impares_Q(w):
    i = 0
    num_pares = 0
    num_impares = 0
    while i < len(w):
        if w[i] % 2 == 0:
            num_pares += 1
        else:
            num_impares += 1
        i += 1
    if num_pares == num_impares:
        return True
    else:
        return False
num_pares_igual_impares_Q([2, 1, 4, 3, 7, 6]) # True

# Ex 11
def tuplo_ordenado_Q(t):
    i = 0
    r = True
    while i < (len(t) - 1):
        if t[i] > t[i+1]:
            r = False
        else:
            r = True
        i += 1
    return r
tuplo_ordenado_Q((16, 42, 43, 68, 82)) # True

# Ex 12
a = [['Joao',10],['Maria',19],['Jose',12], ['João',19]]

def nomes(w):
    i = 0
    max_nota = 0
    r = []
    while i < (len(w) - 1):
        if w[i][1] <= w[i+1][1]:
            max_nota = w[i+1][1]
        i += 1
    i = 0
    while i < len(w):
        if w[i][1] == max_nota:
            r = r + [w[i][0]]
        i += 1
    return r
nomes(a) #  ['Maria','João']