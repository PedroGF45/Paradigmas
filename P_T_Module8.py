# Ordenacao

# Algoritmo da Insercao Direta
a = (1, 7, 4, 5, 7, 2, 10)
def ins_dir(w):
    n = len(w)
    r = ()
    i = 0
    while i < n:
        j = i-1
        while j >= 0 and r[j] <= w[i]:
            j = j - 1
        r = r[:(j+1)] + (w[i],) + r[(j+1):] # Update the answer
        i = i + 1
    return r
ins_dir(a) # (10, 7, 7, 5, 4, 2, 1)

# Algoritmo da Selecao Direta
a = (9, -6, 4, 5, 7, 2, 10)
def self_dir(w):
    r = w
    n = len(r)
    i = 0
    while i<n-1:
        imin=i
        j=i+1
        while j<n:
            if r[j]<r[imin]:
                imin=j
            j=j+1
        r = r[:i]+(r[imin],)+r[i+1:imin]+(r[i],)+r[imin+1:]
        i = i + 1
    return r
self_dir(a)

# Advanced Algorithms
# Quicksort 
a = (9, -6, 4, 5, 7, 2, 10)
def quicksort(w):
    def particao(w):
        e=w[0]
        return [list(filter(lambda x: x<e, w)), \
                list(filter(lambda x: x==e, w)), \
                list(filter(lambda x: x>e, w))]
    def qs(w):
        if len(w)<2:
            return w # lista ordenada
        else:
            return qs(particao(w)[0]) + \
                    qs(particao(w)[1]) + \
                    qs(particao(w)[2])
    return qs(w)
quicksort(a) # [-6, 2, 4, 5, 7, 9, 10]

# Mergesort
def funde(x,y):
    # assume-se que as listas x e y estão ordenadas
    n=len(x)
    k=len(y)
    if n==0:
        r=y
    elif k==0:
        r=x
    else:
        r=[]
        i=0
        j=0
        while i<n and j<k:
            if x[i]<=y[j]:
                r=r+[x[i]]
                i=i+1
            else:
                r=r+[y[j]]
                j=j+1
 # juntar a r eventuais elementos restantes
# de uma das listas
        if i<n:
            r=r+x[i:n]
        else:
            r=r+y[j:k]
    return r
def fb(w):
    if len(w) <= 1:
        return w
    else:
        k = len(w)//2 # quociente da divisao inteira por 2
        v1 = fb(w[:k])
        v2 = fb(w[k:])
        return funde(v1, v2)
a = (9, -6, 4, 5, 7, 2, 10)
fb(a)