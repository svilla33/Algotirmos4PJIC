# =========================
# 🍰 EJEMPLO 1: SUMAR NODOS DE UNA LISTA ENLAZADA
# =========================

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Lista:
    def __init__(self):
        self.cabeza = None

    def sumar(self):
        # 👉 llamamos a la función recursiva pasando la cabeza
        return self._sumar(self.cabeza)

    def _sumar(self, nodo):
        # 🧠 CASO BASE:
        # si el nodo es None, no hay nada más que sumar
        if nodo is None:
            return 0
        
        # 🔁 CASO RECURSIVO:
        # sumo el valor actual + lo que sigue
        return nodo.valor + self._sumar(nodo.siguiente)


# =========================
# 🍰 EJEMPLO 2: CONTAR NODOS
# =========================

class ListaContar:
    def __init__(self):
        self.cabeza = None

    def contar(self):
        return self._contar(self.cabeza)

    def _contar(self, nodo):
        # 🧠 CASO BASE:
        if nodo is None:
            return 0
        
        # 🔁 CASO RECURSIVO:
        # cuento este nodo (1) + los siguientes
        return 1 + self._contar(nodo.siguiente)


# =========================
# 🍰 EJEMPLO 3: BUSCAR UN VALOR
# =========================

class ListaBuscar:
    def __init__(self):
        self.cabeza = None

    def buscar(self, valor):
        return self._buscar(self.cabeza, valor)

    def _buscar(self, nodo, valor):
        # 🧠 CASO BASE 1:
        # si llego al final, no está
        if nodo is None:
            return False
        
        # 🧠 CASO BASE 2:
        # si lo encuentro, paro
        if nodo.valor == valor:
            return True
        
        # 🔁 CASO RECURSIVO:
        # sigo buscando en el siguiente nodo
        return self._buscar(nodo.siguiente, valor)


# =========================
# 🍰 EJEMPLO 4: ELIMINAR NODOS (MUY PARECIDO AL PARCIAL)
# =========================

class ListaEliminar:
    def __init__(self):
        self.cabeza = None

    def eliminar_pares(self):
        # 👉 actualizamos la cabeza con lo que devuelva la recursión
        self.cabeza = self._eliminar(self.cabeza)

    def _eliminar(self, nodo):
        # 🧠 CASO BASE:
        if nodo is None:
            return None
        
        # 🔁 CASO RECURSIVO:
        # primero proceso el resto de la lista
        nodo.siguiente = self._eliminar(nodo.siguiente)
        
        # 👉 luego decido si me quedo con este nodo o no
        if nodo.valor % 2 == 0:
            return nodo.siguiente  # lo elimino
        
        return nodo  # lo conservo