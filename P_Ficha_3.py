# Tuple, Arrays and Dictonary edits
# Ficha 3

# Ex 1

alunosNotas = {'Joao': 10, 'Maria': 14, 'Jose': 8}
notas = tuple(alunosNotas[x] for x in alunosNotas) # tuple with each grade
print(notas) #(10, 14, 8)

x = input('Escreva o seu nome: ',)
if x not in alunosNotas: 
    print('Erro: esse nome nao consta do registo')
elif (x in alunosNotas) & (alunosNotas[x] >= 10):
    print(alunosNotas[x])
else:
    print('Rep')
