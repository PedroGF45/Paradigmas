def p1(x, k):
    i = 0
    r = True
    while i < len(x):
        if len(x[i]['pass']) < k:
            return False
        i += 1
    return r
w = [{'voo': 'TP1711', 'pass': ['Maria','Carlos','António']}, {'voo': 'BA2711', 'pass':['Ana','Pedro','Charles','Silva']}, {'voo': 'EJ2744', 'pass':['John','Afonso','Jorge','Peter']}]
p1(w, 4)

v = [('a',7),('c',-25),('e',8)]
def atoa(x):
    return tuple(filter(lambda z: z[1]>0,v))
atoa(v)

def p2(x, k):
    return all(map(lambda y: False if len(y['pass']) < k else True, x))
w = [{'voo': 'TP1711', 'pass': ['Maria','Carlos','António']}, {'voo': 'BA2711', 'pass':['Ana','Pedro','Charles','Silva']}, {'voo': 'EJ2744', 'pass':['John','Afonso','Jorge','Peter']}]
p2(w, 4)

def nova():
    return []

def acr(s, n):
    return s + [n]

def ultimo(s):
    if len(s) == 0:
        print('xd')
    else:
        return s[-1]

def tiraUlt(s):
    if len(s) == 0:
        print('xd')
    return s[:-1]

def vaziaQ(s):
    return len(s) == 0

def conta(s, k):
    return sum(map(lambda x: 1 if x == k else 0, s))

def ret(s, k):
    return list(filter(lambda x: x != k, s))

def igualQ(s1, s2):
    if vaziaQ(s1) and vaziaQ(s2):
        return True
    elif ultimo(s1) == ultimo(s2):
        return igualQ(tiraUlt(s1), tiraUlt(s2))
    else:
        return False

igualQ([1,2,3], [1,2,4])