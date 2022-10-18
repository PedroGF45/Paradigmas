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