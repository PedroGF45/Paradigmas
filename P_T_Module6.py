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

# Function that calculates the square of a list of numbers
# using while
def squareList(w):
    r = []
    j = 0
    while j < len(w):
        r = r + [w[j] * w[j]]
        j = j + 1
    return r
a = [1, 2, -3, 5, 10, 4]
squareList(a) # [1, 4, 9, 25, 100, 16]

# using for
def squareList(w):
    r = []
    for j in w:
        r = r + [j * j]
    return r
a = [1, 2, -3, 5, 10, 4]
squareList(a) # [1, 4, 9, 25, 100, 16]