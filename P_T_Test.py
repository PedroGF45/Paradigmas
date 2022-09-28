# Theory to be in the test

# Range function
a = tuple(range(1, 6)) # creates a tuple of the sequence generated by the range function between 1 and 6-1(5) with increments of 1
print(a) # (1, 2, 3, 4, 5)

b = range(-3, 2 - 1) # generates a sequence of numbers between -3 and 2 - 1 - 1 (0) with increments of 1
print(tuple(b)) # (-3, -2, -1, 0)

c = tuple(range(10, 24, 6)) # creates a tuples of the sequence generated between 10 and 24-1(23) with increments of 6. The last number must be less or equal than 23.
print(c) # (10, 16, 22)

# For loops
d = (x ** 2 for x in range(5))
print(d) # <generator object <genexpr> at 0x10bb0f6f0> As range() we need to add a tuple

e = tuple((x ** 2 for x in range(5))) #sequence of (0, 1, 2, 3, 4) result will be (0, 1, 2, 3, 4)**2
print(e) # (0, 1, 4, 9, 16)

f = tuple(2 * z for z in range(1, 10, 3)) # sequence of (1, 4, 7) result will be 2*(1, 4, 7)
print(f) # (2, 8, 14)

g = tuple(1 for x in range(3)) # sequence of (0, 1, 2) result will be 1 for every time 
print(g) # (1, 1, 1)

h = tuple((1, 2) * b for b in (1, 3)) # sequence (1, 3) result will be (1,3) * 1 + (1,3) * 3
print(h) # ((1, 2), (1, 2, 1, 2, 1, 2))

i = tuple(x[1] for x in ((4, 5), (7,2,8), (14, 7))) # sequence (4, 5), (7,2,8), (14, 7)) result will be the second element of each subtuple
print(i) # (5, 2, 7)

j = (('Joao', 18, 9), ('Ana', 17, 12), ('Pedro', 19, 17), ('Diogo', 18, 4), ('Martim', 17, 9), ('Joana', 18, 16), ('Beatriz', 19, 15))
nomes = tuple(j[0] for j in j)
idades = tuple(j[1] for j in j)
notas = tuple(j[2] for j in j)
nomes_idades = tuple((j[0], j[1]) for j in j)
print(nomes) # ('Joao', 'Ana', 'Pedro', 'Diogo', 'Martim', 'Joana', 'Beatriz')
print(idades) # (18, 17, 19, 18, 17, 18, 19)
print(notas) # (9, 12, 17, 4, 9, 16, 15)
print(nomes_idades) # (('Joao', 18), ('Ana', 17), ('Pedro', 19), ('Diogo', 18), ('Martim', 17), ('Joana', 18), ('Beatriz', 19))

# Strings

k = 'xpto'
print(k[0]) # 'x'

l = 'ab c' 
m = ''
print(l) # 'ab c'
print(m) # ''
print(l[2]) # ''
print(l[2] == m) # False
print(len(l)) # 4
print('' in l) # True
print(l[0:2]) # 'ab'
print('la13' + '3b') # la133b
print('a' * 3) # 'aaa'

print('4 + 7') # '4 + 7'

n = str(4 + 7) # Evaluate first the expression inside ()
print(n) # 11

o = tuple(x * 2 for x in 'ab1c') # a * 2 + b * 2 + 1 * 2 + c * 1
print(o) # ('aa', 'bb', '11', 'cc')


