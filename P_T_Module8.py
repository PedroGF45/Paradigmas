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
            r = r[:(j+1)] + (w[i],) + r[(j+1):]
        i = i + 1
    return r
ins_dir(a)