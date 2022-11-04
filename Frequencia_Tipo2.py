x = [('aaa',10,40), ('bbb',150,450), ('ccc',25,85)]

# Ex 1
def nd1(v):
    return {v[0][0]: v[0][1]}
nd1(x) # {'aaa': 10}

# Ex 2
def g(x, y, z):
    return [(x[i], y[i], z[i]) for i in range(len(x))]
g(['aaa','bbb','ccc'], [10,150,25], [40,450,85]) # [('aaa', 10, 40), ('bbb', 150, 450), ('ccc', 25, 85)]

# Ex 3
def f(x):
    if len(x) == 1:
        return x[0][2]
    elif x[0][2] > f(x[1:]):
        return x[0][2]
    else:
        return f(x[1:])
f(x) # 450

# Ex 4        
def ins_ord(w, n):
    def aux(i, y, k):
        if i == len(y):
            return y
        elif k >= y[i] and k < y[i+1]:
            return aux(i + 2, y[:i+1] + (k,) + y[i+1:], k)
        else:
            return aux(i + 1, y, k)
    return aux(0, w, n)
x = (-88,-6,-5,0,9,66)
ins_ord(x,4) # (-88,-6,-5,0,4,9,66)
ins_ord(x,9) # (-88,-6,-5,0,9,9,66)