def ta(w, k):
    i = 0
    r = ()
    while i < len(w):
        if w[i][2] <= k:
            r += (w[i][0],)
        i += 1
    return r
apartamentos = [('AAA',2,600), ('AV',3,850), ('BBB',1,450), ('AC',1,650),
('xpto',3,1200)]
ta(apartamentos, 600)
ta(apartamentos, 400)

def ta2(w, k):
    return tuple(map(lambda x: x[0], filter(lambda x: x[2] <= k, w)))
apartamentos = [('AAA',2,600), ('AV',3,850), ('BBB',1,450), ('AC',1,650),
('xpto',3,1200)]
ta2(apartamentos, 600)
ta2(apartamentos, 400)

def nova():
    return ()

def entra(f, x):
    return f + (x,)

def primeiro(f):
    if len(f) == 0:
        print('Erro: fila vazia')
    else:
        return f[0]

def sai(f):
    if len(f) == 0:
        print('Erro: fila vazia')
    else:
        return f[1:]

def vaziaQ(f):
    return len(f) == 0

def num(f):
    return len(f)

def ocorreQ(f, k):
    return any(map(lambda x: x['tipo'] == k, f))

def prim(f, k):
    i = 0
    r = 0
    while i < len(f):
        if f[i]['tipo'] == k:
            return 1
        i += 1
    return r

def ultimo(f):
    if vaziaQ(f):
        print('Erro: fila vazia')
    elif num(f) == 1:
        return primeiro(f)
    else:
        return ultimo(sai(f))