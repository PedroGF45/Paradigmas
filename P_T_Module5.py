# Recursive Programming

# Example of Fatorial function
def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n - 1) # function will call itself till reach fat(1)
fat(5) # 120

def fatOptional(n):
    return 1 if n == 1 else n * fatOptional(n-1) # function will call itself till reach fatOptional(1)
fat(4) # 24

# fat(-1) or fatOptional(-1) would get an infinite loop

# Example of exponential function
def pot(x, n):
    if n == 0:
        return 1
    else:
        return x * pot(x, n - 1) # recursive
pot(4, 3) # 64

# Example of defining the len function
def comp(w):
    if w == []:
        return 0
    else:
        return 1 + comp(w[:-1]) # using recursive to calculate the list with less one element
comp([0, 3, 4, 5, 6, 7]) # 6
# defining the same function but using recursin from the left to right
def comp(w):
    if w == []:
        return 0
    else:
        return 1 + comp(w[1:]) # using recursion from left ro right
comp([0, 3, 4, 5, 6, 7]) # 6

# Example of definig the square of the elements in a tuple
# In comprehension:
def qt(t):
    return tuple(i * i for i in t)
qt((3, -1, 4)) # (9, 1, 16)
# Using recursion from left to right
def qt(t):
    if t == ():
        return ()
    else:
        return ((t[0] * t[0], ) + qt(t[1:]))
qt((3, -1, 4)) # (9, 1, 16)
# Using recursion from right to left
def qt(t):
    if len(t) == 0: # can use function len to see if the tuple is empty
        return ()
    else:
        return (qt(t[:-1]) + (t[-1] ** 2, ))
qt((3, -1, 4)) # (9, 1, 16)

def ocorreQ(x, w):
    if w == []:
        return False
    else: 
        return x == w[0] or ocorreQ(x, w[1:0])