# Using while

# Factorial example
def fact(n):
    r = 1
    i = 2
    while i != (n + 1):
        r = r * 1
        i = i + 1
    return r
fact(4) # 1, because r = 1 and will always be 1 because r = r * 1

def fact(n):
    r = 1 
    i = 2
    while i <= n:
        r = r * i
        i = i + 1
    return r
fact(4) # 24 

def fact(n):
    r = 1
    i = 1
    while i < n:
        r = r * (i + 1)
        i = i + 1
    return r
fact(4) # 24

def fact(n):
    r = 1
    i = 1
    while i < n:
        i = i + 1
        r = r * i
    return r
fact(4) # 24 

def fact(n):
    r = n
    i = n-1
    while i >= 1:
        r = r * i
        i = i - 1
    return r
fact(4) # 24