# Formatacao de cadeias de caracteres (formatacao por %, str.format() e f-strings)

# Ex 3

nome = "Petra"
print(f"Ola! O meu nome e {nome}")

tempo = 65433998
print(f"{tempo} segundos correspondem a, aproximadamente, {(tempo / 3600 / 24):.2f}")

nota_Marcelo = 52.83
nota_Gabriel = 74.94
nota_Amanda = 87.75
nota_media = (nota_Marcelo + nota_Gabriel + nota_Amanda) / 3
print(f"O Marcelo obteve {nota_Marcelo} % na frequencia. \n O Gabriel obteve {nota_Gabriel} % na frequencia. \n A Amanda obteve {nota_Amanda} % na frequencia. \n A media da turma na frequencia foi de {nota_media:.0f} %, arredondada as unidades.")

# Ex 4

def soma_Inteiros():
    n = input("Escreva um numero inteiro: ") # receive the input from the user
    try:
        n = int(n) # see if the value is an integer. If not, go to line 25
        soma = ((n)*(n + 1))/2
        print(f"A soma de 1 a {n} e de {soma:.0f}")
    except ValueError: 
        print(f"{n} nao e um inteiro!")
        soma_Inteiros() # if not an integer run the function again

soma_Inteiros()

# Ex 5

def velocidadeMedia():
    distancia = input("Enter the distance you want to run in kilometers: ")
    time = input("Enter the time you want it to be completed in minutes: ")
    
    try:
        distancia = int(distancia) # See if the value is an integer
        time = int(time)

        velocidade_kmh = distancia / (time / 60) 
        velocidade_ms = (distancia * 1000 ) / (time * 60)

        print(f"A velocidade media em km/h e de {velocidade_kmh}")
        print(f"A velocidade media em m/s e de {velocidade_ms}")
        
    except ValueError:
        print("The values that you entered are not integers")
        velocidadeMedia() # if not an integer run the function again
        
velocidadeMedia()

# Ex 6

from math import log10 # from the framework math import the function log10

def operations():
    x = input("Enter a value for X: ")
    y = input("Enter a value for Y: ")
    
    try:
        x = int(x) # Check if x is an integer
        y = int(y) # Check if y is an integer

        addition = x + y
        subtraction= x - y
        multiplication = x * y
        division = x / y
        division_int = x // y
        division_rest = x % y
        logarithm = log10(x)
        exponencial = x**y

        print(f"{x} + {y} = {addition}\n{x} - {y} = {subtraction}\n{x} * {y} = {multiplication}\n{x} / {y} = {division}\n{x} // {y} = {division_int}\n{x} % {y} = {division_rest}\nlog10({x}) = {logarithm}\n{x}^{y} = {exponencial}")
        
    except ValueError:
        print("The values that you entered are not integers")
        operations()
        
operations()

