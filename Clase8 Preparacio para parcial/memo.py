# =========================
# 🍰 EJEMPLO 1: FIBONACCI (ESCALONES)
# =========================

def sin_memo(n):
    # Caso base: si n es 0 o 1, solo hay 1 forma
    if n == 0 or n == 1:
        return 1
    
    # ❌ PROBLEMA:
    # Aquí se repiten MUCHOS cálculos
    # Ej: sin_memo(5) calcula sin_memo(3) varias veces
    return sin_memo(n-1) + sin_memo(n-2)


def con_memo(n, memo=None):
    # Creamos el diccionario la primera vez
    if memo is None:
        memo = {}
    
    # 🔥 Si ya lo calculamos antes, lo devolvemos
    # 👉 Aquí está la magia de la memorización
    if n in memo:
        return memo[n]
    
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # Calculamos el resultado UNA sola vez
    resultado = con_memo(n-1, memo) + con_memo(n-2, memo)
    
    # 🧠 Guardamos el resultado para el futuro
    memo[n] = resultado
    
    return resultado


# =========================
# 🍰 EJEMPLO 2: SUMA DE 1 A N
# =========================

def suma_sin_memo(n):
    # Caso base
    if n == 0:
        return 0
    
    # ❌ Aquí no es tan grave, pero igual repite trabajo si se usa muchas veces
    return n + suma_sin_memo(n-1)


def suma_con_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    # 🔥 Si ya sabemos cuánto suma hasta n, lo usamos
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    
    resultado = n + suma_con_memo(n-1, memo)
    
    # Guardamos el resultado
    memo[n] = resultado
    
    return resultado


# =========================
# 🍰 EJEMPLO 3: FACTORIAL
# =========================

def factorial_sin_memo(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # ❌ Se recalcula si se llama muchas veces con los mismos valores
    return n * factorial_sin_memo(n-1)


def factorial_con_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    # 🔥 Revisamos si ya existe
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    resultado = n * factorial_con_memo(n-1, memo)
    
    # Guardamos
    memo[n] = resultado
    
    return resultado