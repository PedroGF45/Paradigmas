# Imperative 

# Ex 3
def filtra_pares(t):
    x = 0
    r = ()
    while x < len(t):
        if (t[x] % 2 == 0):
            r = r + (t[x],)
        x += 1
    return r  
a = (81, 55, 80, 62, 49) # (80, 62)
filtra_pares(a)
