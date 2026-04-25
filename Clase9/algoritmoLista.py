lista = [3,8,8,8,8,8,5,2,1,3,5,5,6,7,8]
lista2 = [3, -1, -2, 5, 8]


def contar_elemento_mayor(lista):
    guardador = 0
    

    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista)):
            if  lista[i] == lista[j]:
                contador += 1 
                print('Contador: ',contador)
        
        if guardador < contador:
            guardador = contador
            numeroMayor = lista[i]
        print('Fin Contador:', lista[i],'Numero Mayor:' ,numeroMayor)
    return numeroMayor



#Optimizando con diccionario
def contar_elemento_mayor_memo(lista):
    frecuencias = {}

    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1

    maxElemento = None
    maxConteo = 0

    for elemento, conteo in frecuencias.items():
        if conteo > maxConteo:
            maxConteo = conteo
            maxElemento = elemento

    return maxElemento, maxConteo

def tres_suman_cero(lista):
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lista[i] + lista[j] + lista[k] == 0:
                    return True, (lista[i], lista[j], lista[k])

    return False, None



resultado = tres_suman_cero(lista2)

print(contar_elemento_mayor_memo(lista))

print(resultado)

