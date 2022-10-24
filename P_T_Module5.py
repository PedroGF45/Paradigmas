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

a = [('Ana', 12), ('Antonio', 14), ('Joao', 10), ('Maria', 7)]

# Counting functinos
# Define a function which returns the number of approved students when the grade is >=10
def na(p):
    if p == []:
        return 0
    else:
        if p[0][1] >= 10:
            return 1 + na(p[1:])
        else:
            return na(p[1:])
na(a) # 3

# Return lists, tuples, dictionaries
# Define a function which returns a list with the name of approved students
def la(p):
    if len(p) == 0:
        return []
    elif p[0][1] >= 10:
        return [p[0][0]] + la(p[1:])
    else:
        return la(p[1:])
la(a) # ['Ana', 'Antonio', 'Joao']

# Bigger or equal or minor
# Define a function 'maior_nota' which return the biggest grade on the provided sheet
def maior_nota(p):
    if len(p) == 0:
        return 'Pauta vazia'
    elif len(p) == 1:
        return p[0][1]
    elif p[0][1] > maior_nota(p[1:]):
        return p[0][1]
    else:
        return maior_nota(p[1:])
maior_nota(a) # 14
#or more efficientl but not a recursion
def maior_nota_option(p):
    if len(p) == 0:
        return 'Pauta vazia'
    elif len(p) == 1:
        return p[0][1]
    else:
        x = maior_nota_option(p[1:]) # assign the recursion to a variable. It will only calculate the recursion one time instead of two
        if p[0][1] > x:
            return p[0][1]
        else:
            return x
maior_nota_option(a) # 14
#or more eficcient and still a recursion
def maior_nota_recursion(p):
    if len(p) == 0:
        return 'Pauta vazia'
    elif len(p) == 1:
        return p[0][1]
    else:
        return max(p[0][1], maior_nota_recursion(p[1:])) # use the max function
maior_nota_recursion(a) # 14

# Check conditions
# Define a function which sees if all students are approved
def approvedQ(p):
    if len(p) == 0:
        return True # Is there any repproved in an empty list? No, then it's True
    elif p[0][1] >= 10 and approvedQ(p[1:]):
        return True
    else:
        return False
approvedQ(a) # False


a = [1, 2, 3, 4, 5, (1, 2), -1]
b = (1, 2)
c = [3, -1]
d = [2, 3, 4]
e = [a, b, 1]

# Define a function to check if a list is a sub part of other list
def subQ(w, v):
    if len(v) == 0:
        return True
    elif v[0] in w:
        return subQ(w, v[1:])
    else:
        return False
subQ(a, b) # True
subQ(a, c) # True
subQ(a, d) # True
subQ(a, e) # False