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


# Arrays

a1 = [] # empty array
b1 = [5, ]
print(a1) # []
print(b1) # [5]

c1 = [5, 'a', [2, 4.5], (9, 12)] # int, cadeia, array, tuple
print(len(c1)) # 4

d1 = [5, (7, 2), [9, 3, 4]]
print(d1[0]) # 5
print(d1[2][1]) # 3
print((7, 2) in d1) # True

e1 = [5] * 3 # Operations with arrays
print(e1) # [5, 5, 5]

f1 = [5, 7] + [[6, 8]]
print(f1) # [5, 7, [6, 8]]

g1 = [5, 2, 8, 9][1:3] # between positions 1 and 3-1 = 2
print(g1) # [2, 8]

h1 = list(range(2, 5)) # sequence stating in 2 and ending in 5-1 with increments of 1
print(h1) # [2, 3, 4]

i1 = list(range(20, 0, -8)) # sequence starting in 20 ending in 0-1 with increments of -8
print(i1) # [20, 12, 4]

j1 = list(z * 2 for z in '1b2') # double the cadeia and form a list
print(j1) # ['11', 'bb', '22']

k1 = [len(x) for x in ((3, 2), (5,), (7, 9, 8))] # length of each position
print(k1) # [2, 1, 3]

l1 = tuple(x[1] for x in [[2, 1], [0, 5, 4]]) # Second position of each character
print(l1) # [1, 5]

m1 = list((x, x) for x in 'ab') # form a tuple when x is a with (a,a)
print(m1) # [('a', 'a'), ('b', 'b')]

n1 = [1 for x in [[2, 4], [5,3]]]
print(n1) # [1, 1]

# Objects

print(id(5)) # 4562043248 Every new session of Python this value will change
print(id(4 + 1)) # 4562043248 same as before because it has the same output (5)
print(id(5.0)) # 4612368240 different because 5.0 is a float and 5 is an integer

print( 5 == 5.0) # True because operator == checks if 2 entities have the same value

o1 = 3 + 2
print(id(o1)) # will have the same id as 5

p1 = o1 # will have the same value as o1
print(p1 is o1) # True because they have the same object

print(3 is o1) # False because it isn't the same object


