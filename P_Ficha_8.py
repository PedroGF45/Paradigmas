# Exercise 1
def nova():
    return []

def acr(s, n):
    return [n] + s

def vaziaQ(s):
    if len(s) == 0:
        return True
    else:
        return False

def primeiro(s):
    if len(s) == 0:
        print('Erro: lista vazia')
    else:
        return s[0]

def tiraPrim(s):
    if len(s) == 0:
        print('Erro: lista vazia')
    else:
        return s[1:]

def comp(s):
    return len(s)

def retPares(s):
    return list(filter(lambda x: x % 2 != 0, s))

def insereOrdenada(s, n):
    i = 0
    while i < len(s):
        if s[i] >= n:
            return s[:i] + [n] + s[i:] 
        i += 1

def ordenadaQ(s):
    return all(map(lambda x: s[x] <= s[x+1], range(len(s) - 1)))

# Exercise 2
def nova():
    return []

def entra(f, x):
    return f + [x]

def vaziaQ(f):
    if len(f) == 0:
        return True
    else:
        return False

def primeiro(f):
    if len(f) == 0:
        print('sequencia vazia')
    else:
        return f[0]

def sai(f):
    if len(f) == 0:
        print('sequencia vazia')
    else: 
        return f[1:]

def desUlt(f):
    if len(f) == 0:
        print('sequencia vazia')
    else:
        return f[:-1]

def comp(f):
    return sum(map(lambda x: 1 if x else 0, f))

# Exercise 3
def nova():
    return []

def sobrepoe(p, n):
    return p + [n]

def vaziaQ(p):
    if len(p) == 0:
        return True
    else:
        return False

def topo(p):
    if len(p) == 0:
        print('Erro: sequencia vazia')
    else:
        return p[-1]

def retira(p):
    if len(p) == 0:
        print('Erro: sequencia vazia')
    else:
        return p[:-1]

def tot(p):
    return len(p)

def base(p):
    if len(p) == 0:
        print('Erro: sequencia vazia')
    else:
        return p[0]    

def existeQ(w, k):
    i = 0
    r = False
    while i < len(w):
        if w[i][2] <= k:
            return True
        i += 1
    return r

def existe2Q(w, k):
    return any(map(lambda x: True if x[2] <= k else False, w))

def nova():
    return []

def acr(s, n):
    return s + [n]

def ultimo(s):
    if len(s) == 0:
        print('Erro: sequencia vazia')
    else:
        return s[-1]
    
def tiraUlt(s):
    if len(s) == 0:
        print('Erro: sequencia vazia')
    else:
        return s[:-1]

def vaziaQ(s):
    return len(s) == 0

def conta(s, k):
    return sum(map(lambda x: 1 if x == k else 0, s))

def ret(s, k):
    return list(filter(lambda x: x != k, s))

def ordenadaQ(s):
    return all(map(lambda x: s[x] <= s[x+1], range(len(s)-1)))

def igualQ(s1, s2):
    if vaziaQ(s1) and vaziaQ(s2):
        return True
    elif ultimo(s1) == ultimo(s2):
        return igualQ(tiraUlt(s1), tiraUlt(s2))
    else:
        return False    