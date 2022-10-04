# Tuple and Arrays edits
# Ficha 2

# Ex 1

a = (4, (2, 0, 7), (8, 9), 1, (5, ), (2, 1))
print(a + (2,0))
print(len(a))
print(a[1]) # second term of a (2, 0, 7)
print(a[2][0]) # third term of a (8, 9) and first term of it (8)
# print(a[len(a)]) # out of range because len(a) is 7 and last index on a is 6
print(9 in a) # 9 isn't on a but (8, 9) is, so false
print((1, 2) not in a) # (1, 2) isn't on a so it's true
# a[1] = 'xpto' # we cannot change tuples