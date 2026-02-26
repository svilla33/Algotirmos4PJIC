#le pasamos unas denominaciones de monedas y un numero
# nesesito saber la cantidad minima de monedas
# complejidad factorial

monedas = [1,5,10,25]

def monedas_minimas(cantidad ,monedas, memo={}):
     
    #caso base 
    if cantidad == 0:
        return 0;

    if cantidad < 0:
        return float('inf')
    
    minimo = float('inf')
    for moneda in monedas:
        resultado = monedas_minimas(cantidad - moneda, monedas)
        minimo = min(minimo, resultado + 1)

    return minimo


monedas = [1,5,10,25]

def monedas_minimas_memo(cantidad ,monedas, memo={}): #añado diccionario
     
    if cantidad in memo:  #cosa del diccionario
        return memo[cantidad]
    #caso base 
    if cantidad == 0:
        return 0;

    if cantidad < 0:
        return float('inf')
    
    minimo = float('inf')
    for moneda in monedas:
        resultado = monedas_minimas_memo(cantidad - moneda, monedas, memo)
        minimo = min(minimo, resultado + 1)

    memo[cantidad] = minimo
    return minimo


monedas = [100,200,500,1000]
memo = {}

print(monedas_minimas_memo(150500, monedas, memo))
