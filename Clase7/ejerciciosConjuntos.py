# =========================================
# EJERCICIOS DE CONJUNTOS EN PYTHON
# =========================================
# Este archivo contiene 5 ejercicios resueltos usando conjuntos en Python.
# Está pensado como si fuera tu primera vez aplicando conjuntos,
# pero ya conoces los conjuntos matemáticos.
#
# Recuerda:
# Unión (A ∪ B) -> A | B
# Intersección (A ∩ B) -> A & B
# Diferencia (A - B)
# Diferencia simétrica -> A ^ B
#
# =========================================


# -----------------------------------------
# EJERCICIO 1
# -----------------------------------------
# Dados dos grupos de estudiantes, encuentra:
# 1) Quiénes están en ambos cursos
# 2) Quiénes están solo en el primero

curso_python = {"Ana", "Carlos", "Diana", "Eduardo"}
curso_java = {"Carlos", "Diana", "Fernando", "Gabriel"}

print("=== EJERCICIO 1 ===")

# Intersección
ambos = curso_python & curso_java
print("En ambos cursos:", ambos)

# Diferencia
solo_python = curso_python - curso_java
print("Solo en Python:", solo_python)


# -----------------------------------------
# EJERCICIO 2
# -----------------------------------------
# Une los estudiantes de ambos cursos sin repetir

print("\n=== EJERCICIO 2 ===")

union = curso_python | curso_java
print("Todos los estudiantes:", union)


# -----------------------------------------
# EJERCICIO 3
# -----------------------------------------
# Encuentra estudiantes que están en un curso u otro,
# pero NO en ambos (diferencia simétrica)

print("\n=== EJERCICIO 3 ===")

exclusivos = curso_python ^ curso_java
print("Estudiantes exclusivos:", exclusivos)


# -----------------------------------------
# EJERCICIO 4
# -----------------------------------------
# Dado un catálogo de películas con géneros,
# encuentra cuáles tienen al menos 2 géneros en común

catalogo = {
    "Inception": {"Ciencia Ficción", "Acción", "Thriller"},
    "The Matrix": {"Ciencia Ficción", "Acción", "Thriller"},
    "Titanic": {"Drama", "Romance"},
    "Avengers": {"Acción", "Aventura", "Ciencia Ficción"},
}

print("\n=== EJERCICIO 4 ===")

peliculas = list(catalogo.keys())

for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1 = peliculas[i]
        p2 = peliculas[j]

        comunes = catalogo[p1] & catalogo[p2]

        if len(comunes) >= 2:
            print(f"{p1} y {p2} comparten:", comunes)


# -----------------------------------------
# EJERCICIO 5
# -----------------------------------------
# Índice de similitud (Jaccard)
# Mide qué tan parecidos son dos textos

def calcular_indice(p1, p2):
    STOPWORDS = {
        "el", "la", "los", "las", "un", "una",
        "de", "y", "en", "a"
    }

    palabras1 = {w.lower() for w in p1.split() if w.lower() not in STOPWORDS}
    palabras2 = {w.lower() for w in p2.split() if w.lower() not in STOPWORDS}

    interseccion = len(palabras1 & palabras2)
    union = len(palabras1 | palabras2)

    if union == 0:
        return 0

    return interseccion / union


print("\n=== EJERCICIO 5 ===")

texto1 = "El perro corre en el parque"
texto2 = "Un perro juega en el parque"

indice = calcular_indice(texto1, texto2)

print("Índice de similitud:", round(indice, 2))

if indice > 0.5:
    print("Textos similares")
else:
    print("Textos diferentes")

# =========================================
# FIN DEL ARCHIVO
# =========================================
