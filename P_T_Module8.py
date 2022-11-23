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