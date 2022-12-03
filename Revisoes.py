# 3/12/2022

p = [('Ana', 14), ('Ze', 18), ('Joao', 9), ('Martim', 12)]
q = [{'nome': 'Ana', 'nota': 14}, {'nome': 'Ze', 'nota': 18}, {'nome': 'Joao', 'nota': 9}, {'nome': 'Martim', 'nota': 12}]

# Counting problems with a list of tuples and a list of dictionaries
def f(w, x):
    i = 0
    r = 0
    while i < len(w):
        if (w[i][1] > x):
            r += 1
        i += 1
    return r
f(p, 10) # 3 

def f_o(w, x):
    i = 0 
    r = 0
    while i < len(w):
        if (w[i]['nota'] > x):
            r += 1
        i += 1
    return r
f_o(q, 10) # 3