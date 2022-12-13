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