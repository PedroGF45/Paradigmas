# Alternative Composition

a = 7
if a > 5: # True
# print(2 * a) # Indentation error: expected idented block 
    print(2 * a) # 14

b = 9
c = 16
if b < 9: # False
    c = 2 * b
    print(c)
elif b + c < 25: # False
    c = b + c
    print(c)
else: # Then True
    c = 2 * c
    print(c) # 32

# Functions

def cubo(x):
    x = x ** 3 
    print(x)
cubo(2) # 8
cubo(5-2) # 27

def f(x): # defining functions by branches
    if x < 0:
        x = x ** 2
        print(x)
    else:
        cubo(x) # calling function cubo with return x ** 3
f(-1) # 1
f(0) # 0
f(2) # 8