# class Nodo:
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None

# class Conjunto:
#     def __init__(self, elemento = None):
#         self.cabeza = None
#         self.tamaño = 0

#         if elemento:
#             for e in elemento:
#                 self.agregar(e)

#     def esta_vacia(self):
#         return self.cabeza is None
    
#     def cardinalidad(self):
#         return self.tamaño
    
#     def pertenece(self, x):
#         actual = self.cabeza
#         while actual:
#             if actual.dato == x:
#                 return True
#             actual = actual.siguiente
#         return False
    
#     def agregar(self, x):
#         if self.pertenece(x):
#             return False
        
#         nuevo = Nodo(x)
#         nuevo.siguiente = self.cabeza
#         self.cabeza = nuevo
#         self.tamaño += 1
#         return True
    
#     def eliminar(self, x):
#         if self.esta_vacia():
#             return False
#         if self.cabeza.dato == x:
#             self.cabeza = self.cabeza.siguiente
#             self.tamaño -= 1
#             return True

#         actual = self.cabeza
#         while actual.siguiente:
#             if actual.siguiente.dato == x:
#                 actual.siguiente = actual.siguiente.siguiente
#                 self.tamaño -= 1
#                 return True
#             actual = actual.siguiente

#         return False

#     def vaciar(self):
#         self.cabeza = None
#         self.tamaño = 0

#     def union(self, otro):
#         resultado = Conjunto()
        
#         actual = self.cabeza
#         while actual:
#             resultado.agregar(actual.dato)
#             actual = actual.siguiente

#         actual = otro.cabeza
#         while actual:
#             resultado.agregar(actual.dato)
#             actual = actual.siguiente

#         return resultado
    
#     def interseccion(self, otro):
#         resultado = Conjunto()
#         actual = self.cabeza
#         while actual:
#             if otro.pertenece(actual.dato):
#                 resultado.agregar(actual.dato)
#             actual = actual.siguiente
#         return resultado
    
#     def diferencia(self, otro):
#         resultado = Conjunto()
#         actual = self.cabeza
#         while actual:
#             if not otro.pertenece(actual.dato):
#                 resultado.agregar(actual.dato)
#             actual = actual.siguiente
#         return resultado
    
#     def diferencia_simetrica(self, otro):
#         return self.diferencia(otro).union(otro.diferencia(self))
    
#     def a_lista(self):
#         resultado = []
#         actual = self.cabeza
#         while actual:
#             resultado.append(actual.dato)
#             actual = actual.siguiente
#         return resultado
    
#     def __str__(self):
#         return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    

# # A = Conjunto(["A", "B", "C"])
# # B = Conjunto(["c", "D", "E"])
# # C = A.union(B)
# # print(C)

# algoritmos = {"Ana", "Carlos", "Diana", "Eduardo", "Fernando", "Gabriel", "Helena", "Ivan"}
# base_datos = {"Juan", "Carlos", "Diana", "Karen", "Luis", "Gabriel", "Maria"}
# redes = {"Diana", "Eduardo", "Gabriel", "Karen", "Natalia", "Oscar", "Ivan"}

# catalogo = {
#     "Inception": {"Ciencia Ficción", "Acción", "Thriller", "Drama"},
#     "The Matrix": {"Ciencia Ficción", "Acción", "Thriller"},
#     "Interstellar": {"Ciencia Ficción", "Drama", "Aventura"},
#     "Titanic": {"Drama", "Romance", "Histórica"},
#     "The Notebook": {"Drama", "Romance"},
#     "Avengers": {"Acción", "Aventura", "Ciencia Ficción"},
#     "John Wick": {"Acción", "Thriller", "Crimen"},
#     "The Godfather": {"Crimen", "Drama", "Thriller"},
#     "Toy Story": {"Animación", "Aventura", "Comedia"},
#     "Shrek": {"Animación", "Comedia", "Aventura"}
# }

# peliculas_con_generos_en_comun = []
# pelicula = list(catalogo.keys())
# for i in range(len(pelicula)):
#     for j in range(i + 1, len(pelicula)):
#         p1, p2 = pelicula[i], pelicula[j]
#         comunes = catalogo[p1] & catalogo[p2]
#         if len(comunes) >= 2:
#             peliculas_con_generos_en_comun.append((p1, p2, comunes))

# print(peliculas_con_generos_en_comun)

# generos_totales = [] 

# for generos_pelicula in catalogo.values():
#     for g in generos_pelicula:
#         if g not in generos_totales:
#             generos_totales.append(g)

# generos_totales.sort()

# print(generos_totales)

def calcular_indice(p1, p2):
    # Definición de STOPWORDS (palabras que no aportan significado)
    STOPWORDS = {
        "el", "la", "los", "las", "un", "una", "unos", "unas",
        "de", "del", "al", "a", "en", "con", "por", "para",
        "y", "o", "que", "es", "son", "se", "su", "sus",
        "como", "pero", "más", "este", "esta", "estos", "estas"
    }

    # 1. Convertir a conjuntos y pasar a minúsculas
    # 2. Filtrar las STOPWORDS usando 'set comprehension'
    palabras1 = {w.lower() for w in p1.split() if w.lower() not in STOPWORDS}
    palabras2 = {w.lower() for w in p2.split() if w.lower() not in STOPWORDS}

    # 3. Calcular Intersección (palabras en ambos) y Unión (todas las palabras únicas)
    interseccion = len(palabras1.intersection(palabras2))
    union = len(palabras1.union(palabras2))

    # Manejo de error si ambos textos están vacíos
    if union == 0:
        return 0

    return interseccion / union

# --- PRUEBA DEL EJERCICIO ---
texto_a = "Un perro puede ladrar"
texto_b = "Un gato puede maullar"

indice = calcular_indice(texto_a, texto_b)

print(f"Índice de similitud: {indice:.2f}")

if indice > 0.6:
    print("Resultado: Se copiaron")
else:
    print("Resultado: Son originales")