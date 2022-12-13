# Exercise 1
def nova(w):
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

