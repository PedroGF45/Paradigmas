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

# Ex 3
r = {'Funchal': [23,22,24,25,21,22,22],
    'Lisboa': [15,16,18,18,17,19,15],
    'Porto': [12,15,18,14,10,12,14]}

def quarta(w):
    return {x: w[x][2] for x in w}
quarta(r) # {'Funchal': 24, 'Lisboa': 18, 'Porto': 18}

def weekend(w):
    return [(w[x][-2], w[x][-1]) for x in w]
weekend(r) # [(22, 22), (19, 15), (12, 14)]