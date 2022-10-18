# Defining Functions
# Ficha 4

# Ex 1
def checkYear(y):
    if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)):
        return True
    else: 
        return False
checkYear(1984) # True - E bissexto
checkYear(2000) # True - E bissexto
checkYear(1100) # False - Nao e bissexto

# Ex 2
def soma(w1, w2):
    return [w1[x] + w2[x] for x in range(len(w1))]
a = [2,4,5,6,2,3]
b = [2,3,4,6,8,9]
soma(a, b) # [4, 7, 9, 12, 10, 12]