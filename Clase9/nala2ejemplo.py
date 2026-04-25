def tiene_diplicados(lista)
    n = len(lista)
    for i in range(n):
        for j in range(i+1, n):
            if lista[i] == lista[j]:
                return True
    return False
