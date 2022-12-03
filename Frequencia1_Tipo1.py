v = [{'voo': 'TP1714', 'tipo': 'D', 'horario': (11,0), 'pass': ['Marta','Jota','Marco']}, {'voo': 'BA2711', 'tipo': 'A', 'horario': (11,5), 'pass':['Ana','Pedro','Charles','Silva']}, {'voo': 'EJ1771', 'tipo': 'D', 'horario': (11,12), 'pass': ['Hugo','Ferdinando']}]
w = [{'voo': 'TP1711', 'tipo': 'A', 'horario': (10,50), 'pass': ['Maria', 'Carlos', 'Antonio']}, {'voo': 'BA2711', 'tipo': 'A', 'horario': (11,5), 'pass': ['Ana', 'Pedro', 'Charles', 'Silva']}] 

# Ex 1
def p1(w):
    return w[-1]['horario'][0]
p1(w) # 11

# Ex 2
def np(x):
    return [len(i['pass']) for i in x]
np(v) # [3, 4, 2]

# Ex 3
def q3(x, t):
    if x == []:
        return True
    elif x[0]['tipo'] == 'A' and q3(x[1:], t):
        return True
    else:
        return False
q3(w, 'A') # True
q3(v, 'A') # False
q3(v, 'D') # False

# Ex 4
def passageiros(x):
    def aux(r, y):
        if y == []:
            return r
        else: 
            return aux(r + y[0]['pass'], y[1:])
    return aux([], x)  
passageiros(v) # ['Marta', 'Jota', 'Marco', 'Ana', 'Pedro', 'Charles', 'Silva', 'Hugo', 'Ferdinando']