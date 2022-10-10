# Alternative Composition

a = 7
if a > 5: # True
# print(2 * a) # Indentation error: expected idented block 
    print(2 * a) # 14

b = 9
c = 16
if b < 9: # False
    c = 2 * b
    print(c)
elif b + c < 25: # False
    c = b + c
    print(c)
else: # Then True
    c = 2 * c
    print(c) # 32

