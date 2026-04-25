"""
═══════════════════════════════════════════════════════════════════════════════
        TALLER: ANÁLISIS DE ALGORITMOS
        Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES GENERALES:
------------------------
- Entregar archivo .py con todas las secciones resueltas
- El código debe ejecutar sin errores

DISTRIBUCIÓN:
- Sección A: Análisis teórico (1.0)         
- Sección B: Investigación (0.5)             
- Sección C: Resolver y optimizar (2.0)      
- Sección D: Proponer y justificar (1.5)     

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN A: ANÁLISIS TEÓRICO (1.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO A.1 (0.4): Clasificar complejidad

Para cada función, escribe:
  - La complejidad Big-O
  - UNA línea explicando por qué

Escribe tus respuestas como comentarios debajo de cada función.
"""


def alpha(lista):
    total = 0
    for x in lista:
        total += x
    promedio = total / len(lista)
    return promedio

# Complejidad: O(n)
# Porque: Un for que depende del parametro dado

def beta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                return True
    return False

# Complejidad: O(n²)
# Porque: un doble for aninado que depende de la entrada


def gamma(n):
    if n <= 1:
        return 1
    return gamma(n // 2) + 1

# Complejidad: O(Log n)
# Porque: es solo un if, las lineas solo se ejecutan 1 vez


def delta(lista):
    resultado = set()
    for x in lista:
        resultado.add(x)
    return resultado

# Complejidad: O(n)
# Porque: es un conversor a SET que se ejecuta n veces y n demende de la entrada


def epsilon(lista):
    for x in lista:
        if x in lista:
            pass

# Complejidad: O(n²)
# Porque: n in lista cuesta n y hay dos n in lista asi que n * n
# PISTA: ¿cuánto cuesta `x in lista`?


def zeta(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 3

# Complejidad: O(n Log n)
# Porque: la funcion se ejecuta n veces pero cada vez que se ejecuta, dentro se ejecuta log n veces


def eta(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = eta(lista[:medio])
    der = eta(lista[medio:])
    return izq + der

# Complejidad: O(n Log n)
# Porque: el n log n sale de la linea que haya medio, aun asi, como izq y der llaman a la misma 
# funcion y retorna izq + der se ejecuta n veces  
# PISTA: ¿cuánto cuesta lista[:medio]?


def theta(n):
    i = 1
    while i * i <= n:
        i += 1
    return i

# Complejidad: O(raiz de n)
# Porque: es por i * i, digamos que no escala logaritmicamente, sino exponencialmente
# la solucuon 


"""
PUNTO A.2 (0.3): Ordenar de menor a mayor complejidad

Ordena las siguientes complejidades de la MÁS RÁPIDA a la MÁS LENTA:

O(n!), O(1), O(n log n), O(2^n), O(n²), O(log n), O(n), O(n³), O(√n)

Tu respuesta (de más rápida a más lenta):
1. O(1)
2. O(log n)
3. O(Raiz n)
4. O(n)
5. O(n log n)
6. O(n²)
7. O(n³)
8. O(2^n)
9. O(n!)
"""


"""
PUNTO A.3 (0.3): Verdadero o Falso

Escribe V o F y justifica brevemente las falsas.

1. F O(2n) es más lento que O(n)
   Justificación: Si nos referimosa clasificacion de complejidad, con equivalentes

2. V Un algoritmo O(n²) siempre es más lento que uno O(n log n)
   Justificación: Siempre va a ser mas lenta, la complejidad es una combinacion de log y lineal,
   funciones mucho mas eicientes que exponencial

3. F Si un algoritmo tiene un for de n y dentro un for de 5,
       su complejidad es O(n²)
   Justificación: Falso, solo un for anidado depende de la entrada, el otro es lineal

4. F `x in set` tiene la misma complejidad que `x in list`
   Justificación: set es constante list es lineal

5. F Un algoritmo recursivo que se llama a sí mismo 2 veces
       siempre es O(2^n)
   Justificación: si no es anidado no aplic por ejemplo

6. F O(n) + O(n²) = O(n³)
   Justificación: no se suman los big O

7. V La complejidad espacial de un algoritmo in-place es O(1)
   Justificación: Un algoritmo in- place no usa espacio adicional significativo

8. V Memoización mejora la complejidad temporal pero empeora la espacial
   Justificación: nos ayuda en la temporal pero empeora la espacial
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN B: INVESTIGACIÓN (0.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO B.1 (0.25): Complejidad de operaciones de Python

Investiga y completa la tabla con la complejidad de cada operación.
Agrega una justificación de por qué es la complejidad.
Puedes consultar: https://wiki.python.org/moin/TimeComplexity

┌──────────────────────────────┬──────────────┬──────────────┐
│ Operación                    │ Lista []     │ Set/Dict {}  │
├──────────────────────────────┼──────────────┼──────────────┤
│ Acceder por índice [i]       │ O(1)         │ N/A          │
│ Buscar elemento (x in ...)   │ O(n)         │ O(?)         │
│ Agregar al final (.append)   │ O(?)         │ O(?)  (.add) │
│ Insertar al inicio           │ O(?)         │ N/A          │
│ Eliminar por valor (.remove) │ O(?)         │ O(?)         │
│ Obtener longitud (len)       │ O(?)         │ O(?)         │
│ Ordenar (.sort / sorted)     │ O(?)         │ N/A          │
│ Copiar (.copy / [:])         │ O(?)         │ O(?)         │
└──────────────────────────────┴──────────────┴──────────────┘
"""


"""
PUNTO B.2 (0.25): Caso real

Investiga y responde:

1. ¿Qué algoritmo de ordenamiento usa Python internamente (sorted/list.sort)?
   Respuesta: ___

2. ¿Cuál es su complejidad en el mejor, peor y caso promedio?
   Mejor: ___
   Peor: ___
   Promedio: ___

3. ¿Por qué Python eligió ese algoritmo y no Quick Sort?
   Respuesta: ___
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN C: RESOLVER Y OPTIMIZAR (2.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
En cada problema:
1. Analiza la versión LENTA y escribe su complejidad
2. Implementa la versión RÁPIDA
3. Escribe la complejidad de tu versión
4. Ejecuta las pruebas para verificar que funciona
"""


# ─── PROBLEMA C.1 (0.4): Elementos únicos ────────────────────────────────────

def unicos_lento(lista):
    """
    Retorna lista sin duplicados manteniendo el orden.
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    """
    Misma funcionalidad pero más eficiente.
    USA un set auxiliar para búsqueda O(1).

    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    pass


# ─── PROBLEMA C.2 (0.4): Frecuencia del más común ────────────────────────────

def mas_comun_lento(lista):
    """
    Retorna el elemento que más se repite y cuántas veces.
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    max_elem = None
    max_count = 0
    for x in lista:
        count = 0
        for y in lista:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


def mas_comun_rapido(lista):
    """
    Misma funcionalidad usando diccionario contador.

    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    pass


# ─── PROBLEMA C.3 (0.4): Pares que suman K ───────────────────────────────────

def pares_suma_lento(lista, k):
    """
    Retorna todos los pares (i, j) donde lista[i] + lista[j] == k.
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


def pares_suma_rapido(lista, k):
    """
    Misma funcionalidad usando set para buscar complementos.

    Estrategia:
    - Para cada x, el complemento es k - x
    - Si el complemento ya está en un set de "vistos", es un par

    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    pass


# ─── PROBLEMA C.4 (0.4): Anagramas ───────────────────────────────────────────

def son_anagramas_lento(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (mismas letras, diferente orden).
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


def son_anagramas_rapido(palabra1, palabra2):
    """
    Misma funcionalidad sin ordenar.

    Estrategia: contar frecuencia de cada letra con diccionario.

    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    pass


# ─── PROBLEMA C.5 (0.4): Subarray de suma máxima ─────────────────────────────

def max_subarray_lento(lista):
    """
    Encuentra la suma máxima de un subarray contiguo.
    Ejemplo: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])

    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    n = len(lista)
    max_suma = lista[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += lista[k]
            max_suma = max(max_suma, suma)
    return max_suma


def max_subarray_rapido(lista):
    """
    Algoritmo de Kadane: un solo recorrido.

    Idea: mantener la suma actual. Si se vuelve negativa, reiniciar.
    - suma_actual = max(x, suma_actual + x)
    - max_suma = max(max_suma, suma_actual)

    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    pass


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN D: PROPONER Y JUSTIFICAR (1.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO D.1 (0.5): Diseñar un algoritmo

PROBLEMA: Sistema de autocompletado
Un buscador tiene una lista de 1 millón de palabras. Cuando el usuario
escribe las primeras letras, debe mostrar las 5 palabras que empiezan
con ese prefijo.

Ejemplo:
  palabras = ["python", "programar", "programa", "prueba", "pizza", ...]
  autocompletar("pro") → ["programar", "programa"]

Propón DOS soluciones con diferente complejidad:

SOLUCIÓN 1 (fuerza bruta):
  Descripción: ___
  Complejidad: O(?)
  Código:
"""


def autocompletar_v1(palabras, prefijo):
    """
    Versión fuerza bruta.
    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    pass


"""
SOLUCIÓN 2 (optimizada):
  Descripción: ___
  Complejidad: O(?)
  ¿Qué estructura de datos usarías? ___
  Código:
"""


def autocompletar_v2(palabras_ordenadas, prefijo):
    """
    Versión optimizada.
    PISTA: Si las palabras están ordenadas, puedes usar búsqueda binaria
    para encontrar dónde empiezan las que tienen el prefijo.

    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    pass


"""
PUNTO D.2 (0.5): Analizar un sistema real

ESCENARIO: Red social con 10 millones de usuarios.
Cada usuario tiene una lista de amigos (promedio 200 amigos).

Analiza la complejidad de estas operaciones y propón la mejor
estructura de datos para cada una:

1. Verificar si dos usuarios son amigos
   - Con lista de amigos: O(?)
   - Con set de amigos: O(?)
   - ¿Cuál elegirías? ___

2. Encontrar amigos en común entre dos usuarios
   - Con listas: O(?)
   - Con sets: O(?)
   - ¿Cuál elegirías? ___

3. Sugerir "personas que quizás conozcas" (amigos de amigos que no son tus amigos)
   - Describe tu algoritmo: ___
   - Complejidad estimada: O(?)
   - ¿Es viable para 10M de usuarios? ___

4. Si cada usuario tiene en promedio 200 amigos y hay 10M de usuarios:
   - ¿Cuánta memoria ocupa almacenar TODAS las relaciones de amistad?
   - Con lista: ___ bytes aproximadamente
   - Con set: ___ bytes aproximadamente
"""


"""
PUNTO D.3 (0.5): Reflexión y comparación

Escribe un párrafo (mínimo 5 líneas) respondiendo:

¿Por qué es importante analizar la complejidad de un algoritmo
ANTES de implementarlo? Da un ejemplo concreto de un caso donde
elegir el algoritmo incorrecto podría causar problemas reales
(tiempo de espera, costos de servidor, mala experiencia de usuario, etc.)

Tu respuesta:
___
___
___
___
___
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                         CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def medir(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    return resultado, time.time() - inicio


if __name__ == "__main__":
    print("=" * 70)
    print("     TALLER: ANÁLISIS DE ALGORITMOS - PRUEBAS SECCIÓN C")
    print("=" * 70)

    # ── C.1: Únicos ──────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.1: ELEMENTOS ÚNICOS")
    print("─" * 70)

    for n in [1000, 5000, 10000]:
        lista = [random.randint(1, n // 2) for _ in range(n)]

        r1, t1 = medir(unicos_lento, lista)
        r2, t2 = medir(unicos_rapido, lista) if unicos_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓ correcto" if r1 == r2 else f"  ✗ DIFERENTE")
        else:
            print("  (sin implementar)")

    # ── C.2: Más común ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.2: ELEMENTO MÁS COMÚN")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 20) for _ in range(n)]

        r1, t1 = medir(mas_comun_lento, lista)
        r2, t2 = medir(mas_comun_rapido, lista) if mas_comun_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓" if r1 == r2 else f"  resultado: {r1} vs {r2}")
        else:
            print("  (sin implementar)")

    # ── C.3: Pares que suman K ───────────────────────────────────
    print("\n" + "─" * 70)
    print("C.3: PARES QUE SUMAN K")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 100) for _ in range(n)]
        k = 50

        r1, t1 = medir(pares_suma_lento, lista, k)
        r2, t2 = medir(pares_suma_rapido, lista, k) if pares_suma_rapido(lista, k) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  pares encontrados: {len(r1)} vs {len(r2)}")
        else:
            print("  (sin implementar)")

    # ── C.4: Anagramas ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.4: ANAGRAMAS")
    print("─" * 70)

    casos_anagramas = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("python", "typhon", True),
        ("abc", "abcd", False),
    ]

    for p1, p2, esperado in casos_anagramas:
        r_lento = son_anagramas_lento(p1, p2)
        r_rapido = son_anagramas_rapido(p1, p2) if son_anagramas_rapido(p1, p2) is not None else "N/A"
        marca = "✓" if r_rapido == esperado else "✗"
        print(f"  {marca} '{p1}' vs '{p2}': lento={r_lento}, rápido={r_rapido}, esperado={esperado}")

    # ── C.5: Subarray máximo ─────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.5: SUBARRAY DE SUMA MÁXIMA")
    print("─" * 70)

    casos_subarray = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5, -9, 6, -2, 3],
    ]

    for lista in casos_subarray:
        r_lento = max_subarray_lento(lista)
        r_rapido = max_subarray_rapido(lista)
        marca = "✓" if r_rapido == r_lento else "✗"
        print(f"  {marca} {lista} → lento={r_lento}, rápido={r_rapido}")

    for n in [500, 2000, 5000]:
        lista = [random.randint(-50, 50) for _ in range(n)]
        r1, t1 = medir(max_subarray_lento, lista)
        r2, t2 = medir(max_subarray_rapido, lista) if max_subarray_rapido(lista) is not None else (None, 0)
        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s")

    # ── D.1: Autocompletar ───────────────────────────────────────
    print("\n" + "─" * 70)
    print("D.1: AUTOCOMPLETAR")
    print("─" * 70)

    palabras = [f"palabra_{random.randint(1000, 9999)}" for _ in range(50000)]
    palabras.extend(["python", "programar", "programa", "prueba", "pizza",
                      "proyecto", "profesor", "promedio", "proceso", "producir"])
    random.shuffle(palabras)
    palabras_ord = sorted(palabras)

    for prefijo in ["pro", "pyt", "piz", "xyz"]:
        r1, t1 = medir(autocompletar_v1, palabras, prefijo) if autocompletar_v1(palabras, prefijo) is not None else (None, 0)
        r2, t2 = medir(autocompletar_v2, palabras_ord, prefijo) if autocompletar_v2(palabras_ord, prefijo) is not None else (None, 0)

        print(f"  Prefijo '{prefijo}': v1={t1:.4f}s  v2={t2:.4f}s", end="")
        if r1:
            print(f"  → {len(r1)} resultados")
        else:
            print("  (sin implementar)")
