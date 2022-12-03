# 3/12/2022

p = [('Ana', 14), ('Ze', 18), ('Joao', 9), ('Martim', 12)]
q = [{'nome': 'Ana', 'nota': 14}, {'nome': 'Ze', 'nota': 18}, {'nome': 'Joao', 'nota': 9}, {'nome': 'Martim', 'nota': 12}]

# Counting problems with a list of tuples and a list of dictionaries using while and for
# using while with list of tuples
def f(w, x):
    i = 0
    r = 0
    while i < len(w):
        if (w[i][1] > x):
            r += 1
        i += 1
    return r
f(p, 10) # 3 

# using for with list of tuples
def f_for(w, x):
    r = 0
    for i in range(len(w)):
        if (w[i][1] > x):
            r += 1
    return r
f_for(p, 10) # 3

# simlifying with for
def f_for_simple(w, x):
    r = 0
    for z in w:
        if z[1] > x:
            r += 1
    return r
f_for_simple(p, 10) # 3

# using while with list of dictionaries
def f_o(w, x):
    i = 0 
    r = 0
    while i < len(w):
        if (w[i]['nota'] > x):
            r += 1
        i += 1
    return r
f_o(q, 10) # 3

# using for with list of dictionaries
def f_o_for(w, x):
    r = 0
    for i in range(len(w)):
        if (w[i]['nota'] > x):
            r += 1
    return r
f_o_for(q, 10) # 3

# simplifying with for
def f_o_for_simple(w, x):
    r = 0
    for z in w:
        if z['nota'] > x:
            r += 1
    return r
f_o_for_simple(q, 10) # 3


# Create a list of elements
p = [('Ana', 14), ('Ze', 18), ('Joao', 9), ('Martim', 12)]

# using while 
def list_names(w, x):
    i = 0
    r = []
    while i < len(w):
        if (w[i][1] > x):
            r += [w[i][0]]
        i += 1
    return r
list_names(p, 10) # ['Ana', 'Ze', 'Martim']

# using for
def list_names_for(w, x):
    r = []
    for i in range(len(w)):
        if (w[i][1] > x):
            r += [w[i][0]]
    return r
list_names_for(p, 10) # ['Ana', 'Ze', 'Martim']

# using for simplified
def list_names_for_simple(w, x):
    r = []
    for z in w:
        if z[1] > x:
            r += [z[0]]
    return r
list_names_for_simple(p, 10) # ['Ana', 'Ze', 'Martim']

q = [{'nome': 'Ana', 'nota': 14}, {'nome': 'Ze', 'nota': 18}, {'nome': 'Joao', 'nota': 9}, {'nome': 'Martim', 'nota': 12}]
 
 # using while
def list_while(w, x):
    r = []
    i = 0
    while i < len(w):
        if (w[i]['nota'] > x):
            r += [w[i]['nome']]
        i += 1
    return r
list_while(q, 10) # ['Ana', 'Ze', 'Martim']

# using for
def list_for(w, x):
    r = []
    for i in range(len(w)):
        if (w[i]['nota'] > x):
            r += [w[i]['nome']]
    return r
list_for(q, 10) # ['Ana', 'Ze', 'Martim']

# using for simplified
def list_for_simple(w, x):
    r = []
    for z in w:
        if z['nota'] > x:
            r += [z['nome']]
    return r
list_for_simple(q, 10) # ['Ana', 'Ze', 'Martim']


# Check if some/all check some condition
p = [('Ana', 14), ('Ze', 18), ('Joao', 9), ('Martim', 12)]

# using while
def cond_list(w, x):
    i = 0
    r = False
    while i < len(w) and not r: # or -> '..and r == False'
        if w[i][1] > x:
            r = True
        i += 1
    return r
cond_list(p, 10) # True

# using while simplified
def cond_list(w, x):
    i = 0
    r = False
    while i < len(w) and w[i][1] > x:
        r = True
        i += 1
    return r
cond_list(p, 19) # False

def aprovadosQ(w):
    i = 0
    r = True
    while i < len(w) and r: # or -> '..and r == True'
        if w[i][1] < 10:
            r = False
        i += 1
    return r
aprovadosQ(p) # False


# Get maximum or minimum
p = [('Ana', 14), ('Ze', 18), ('Joao', 9), ('Martim', 12)]

# using while
def nota_max(w):
    if w == []:
        print('Erro: Pauta sem alunos') # empty list. Can use '.. if len(w) == 0'
    i = 0
    r = 0
    while i < (len(w) - 1):
        if w[i][1] > w[i + 1][1]:
            r = w[i][1]
        i += 1
    return r
nota_max(p) # 18

# different option
def nota_max(w):
    if w == []:
        print('Erro: Pauta sem alunos') # empty list. Can use '.. if len(w) == 0'
    r = w[0][1] # Assuming the first element is the biggest
    i = 0
    while i < len(w):
        if w[i][1] > r:
            r = w[i][1]
        i += 1
    return r

# using for
def nota_max_for(w):
    if w == []:
        print('Erro: Pauta sem alunos') # empty list. Can use '.. if len(w) == 0'
    r = 0
    for i in range(len(w) - 1):
        if w[i][1] > w[i + 1][1]:
            r = w[i][1]
    return r
nota_max_for(p) # 18


# Functional programming

p = [('Ana', 14), ('Ze', 18), ('Joao', 9), ('Martim', 12)]

# Count number of approved
def f(w, x):
    return len(list(filter(lambda z: z[1] > x, w)))
f(p, 10) # 3

def f(w, x):
    return sum(map(lambda z: 1 if z[1] > 12 else 0, w))
f(p, 10) # 2