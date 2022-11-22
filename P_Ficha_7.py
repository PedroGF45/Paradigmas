#Functional Programming

# Ex 1
def divs(w, d):
    return sum((map(lambda x: x, w))) / d
divs([1, 2, 3, 4, 5], 3) # 5.0

# Ex 2
def primeiros(w):
    return tuple(map(lambda x: x[0], w))
primeiros([[4, 5, 6, 0],[2, 3, 7, 8],[3, 4, 5, -1]]) # (4, 2, 3)