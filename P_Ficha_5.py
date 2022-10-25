# Defining recursive functions

# Ex 1
from tkinter import W


a = [64, 79, 75, 87]
def soma(w):
    if w == []:
        return 0
    else:
        return w[0] + soma(w[1:])
soma(a) # 305

# Ex 2
a = [64, 79, 75, 87]
def invert(w):
    if w == []:
        return [] # must return an empty list
    else:
        return [w[-1]] + invert(w[:-1])
invert(a) # [87, 75, 79, 64]

# Ex 3
a = (0, 23, 46, 88, 95)
def count_even(w):
    if w == ():
        return 0
    elif w[0] % 2 == 0:
        return 1 + count_even(w[1:])
    else:
       return count_even(w[1:])
count_even(a) # 3