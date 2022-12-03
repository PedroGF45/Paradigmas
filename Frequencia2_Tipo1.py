def nova():
    return []

def acr(s, n):
    return s + [n]

def ultimo(s):
    if s == []:
        print('sequencia vazia')
    else:
        return s[-1]

def tiraUlt(s):
    if s == []:
        print('Erro: tentativa de retirar se sequencia vazia')
    else:
        return s[:-1]

def vaziaQ(s):
    return len(s) == 0

def conta(s, k):
    return len(filter(lambda x: x == k, s))

def ret(s, k):
    return list(filter(lambda x: x != k, s))

from functools import reduce

def ordenadaQ(s):
    return all(map(lambda x: s[x] <= s[x+1], range(len(s) - 1)))


def igualQ(s1, s2):
    if vaziaQ(s1) and vaziaQ(s2):
        return True
    elif vaziaQ(s1) or vaziaQ(s2):
        return False
    elif ultimo(s1) != ultimo(s2):
        return False
    else:
        return igualQ(tiraUlt(s1), tiraUlt(s2)) 