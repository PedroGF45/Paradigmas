#Conditional Programming (missing classes)
from functools import reduce

w = [{'cidade': 'Lisboa', 'temp': 25}, {'cidade': 'Porto', 'temp': -5}, {'cidade': 'Funchal', 'temp': 20}, {'cidade': 'Braga', 'temp': -2}]

a = list(filter( lambda x: x['temp'] < 0, w)) # list of cities which temperature is below 0
def numberNegativeCities(w):
    return len(w) 
numberNegativeCities(a) # 2
# Or
def nNC(w):
    return list(map(lambda x: 1 if x['temp'] < 0 else 0, w)) 
nNC(w) # [0, 1, 0, 1]

def lcnt(w): #List of cities with negative temperatura
    return list(map(lambda x: x['cidade'], filter(lambda x: x['temp'] < 0, w)))
lcnt(w) # ['Porto, 'Braga']

def cntQ(w): #Check if exists a city with negative tempature
    return any(map(lambda x: x['temp'] < 0, w))
cntQ(w) # True
#Or
def cntQo(w):
    return sum(map(lambda x: 1 if x['temp'] < 0 else 0, w)) > 0 # True if sum is > 0
cntQo(w) # True

def acntQ(w): #Check if all cities have negative temperatures
    return all(map(lambda x: x['temp'] < 0, w))
acntQ(w) # False
#Or
def acntQo(w):  #Check if all cities have negative temperatures using product with a sequence
    def prod(x, y):
        return x * y # need to use reduce because we have no function equivalent to 'all' but with products
    return reduce(prod, map(lambda x: 1 if x['temp'] < 0 else 0, w)) == 1  # Uses prod function on a list v == (map(lambda x: 1 if x['temp'] < 0 else 0, w))
acntQo(w) # False

def minimum(w): # minimum temperatur of all cities
    def menor(x, y):
        if x['temp'] < y['temp']:
            return x
        else:
            return y
    return reduce(menor, w)['temp']
minimum(w) # -5
#Or
def minimumo(w): # Option for previous function
    z = map(lambda x: x['temp'], w)
    return min(z)
minimumo(w) # -5