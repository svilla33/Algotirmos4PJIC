class Nodo:
    def __init__(self, dato):
        self.dato = dato          # lo que guarda el nodo (número, nombre, objeto...)
        self.siguiente = None     # flecha hacia adelante
        self.anterior = None      # ← flecha hacia atrás (¡esto es lo nuevo!)

class ListaDoble:
    def __init__(self):
        self.cabeza = None   # primer nodo
        self.cola = None     # último nodo (¡nos facilita mucho la vida!)

    def esta_vacia(self):
        return self.cabeza is None

    # 3.1 Insertar al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            return
        nuevo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo
        self.cabeza = nuevo

    # 3.2 Insertar al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            return
        nuevo.anterior = self.cola
        self.cola.siguiente = nuevo
        self.cola = nuevo

    # 3.3 Imprimir hacia adelante (iterativo)
    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    # 3.4 Imprimir hacia atrás (iterativo)
    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")
        
    def imprimir_recursivo_adelante(self):
        self._imprimir_adelanteR(self.cabeza)   # método "privado" helper

    def _imprimir_adelanteR(self, nodo): #version recursiva
        if nodo is None:
            print("None")
            return
        print(nodo.dato, end=" <-> ")
        self._imprimir_adelante(nodo.siguiente)