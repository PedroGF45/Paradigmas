#Conditional Programming (missing classes)

w = [{'cidade': 'Lisboa', 'temp': 25}, {'cidade': 'Porto', 'temp': -5}, {'cidade': 'Funchal', 'temp': 20}, {'cidade': 'Braga', 'temp': -2}]

a = list(filter( lambda x: x['temp'] < 0, w)) # list of cities which temperature is below 0
def numberNegativeCities(w):
    return len(w) 
numberNegativeCities(a) # 2