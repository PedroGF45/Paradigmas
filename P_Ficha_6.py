# Imperative 

# Ex 1
def soma_quadrados_while(n):
    i = 0
    r = 0
    while i <= n:
        r = r + i*i
        i += 1
    return r

def soma_quadrados_for(n):
    r = 0
    for i in range(n+1):
        r = r + i*i
        i += 1
    return r
a = 5
soma_quadrados_for(a) # 55
soma_quadrados_for(a) # 55

# Ex 3
def filtra_pares_while(t):
    x = 0
    r = ()
    while x < len(t):
        if (t[x] % 2 == 0):
            r = r + (t[x],)
        x += 1
    return r  

def filtra_pares_for(t):
    i = 0
    r = ()
    for i in range(len(t)):
        if (t[i] % 2 == 0):
            r = r + (t[i],)
        i += 1
    return r
a = (81, 55, 80, 62, 49) 
filtra_pares_while(a) # (80, 62)
filtra_pares_for(a) # (80, 62)
