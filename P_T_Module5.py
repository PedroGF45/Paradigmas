# Recursive Programming

# Example of Fatorial function
def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n - 1) # function will call itself till reach fat(1)
fat(5) # 120

def fatOptional(n):
    return 1 if n == 1 else n * fatOptional(n-1) # function will call itself till reach fatOptional(1)
fat(4) # 24

# fat(-1) or fatOptional(-1) would get an infinite loop