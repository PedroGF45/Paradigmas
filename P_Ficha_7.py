#Functional Programming

# Ex 1
def divs(w, d):
    return sum((map(lambda x: x, w))) / d
divs([1, 2, 3, 4, 5], 3)