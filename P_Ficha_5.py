# Defining recursive functions

# Ex 1
a = [64, 79, 75, 87]
def soma(w):
    if w == []:
        return 0
    else:
        return w[0] + soma(w[1:])
soma(a)