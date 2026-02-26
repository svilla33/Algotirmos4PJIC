class Nodo:
    def __init__(self, dato, prioridad):
        self.dato = dato
        self.prioridad = prioridad
        self.siguiente = None


class ListaLigadaPrioridad:
    def __init__(self):
        self.cabeza = None
    
    # ====================== AGREGAR (recursivo) ======================
    def agregar(self, dato, prioridad):
        """Agrega un elemento manteniendo el orden de prioridad.
        ¡Menor número = MAYOR prioridad! (ej: prioridad 1 > prioridad 5)"""
        self.cabeza = self._agregar_recursivo(self.cabeza, dato, prioridad)
    
    def _agregar_recursivo(self, actual, dato, prioridad):
        # Caso base: llegamos al final o encontramos la posición correcta
        if actual is None or actual.prioridad > prioridad: #el > se puede cambiar para las prioridades
            nuevo = Nodo(dato, prioridad)
            nuevo.siguiente = actual
            return nuevo
        
        # Seguimos avanzando recursivamente
        actual.siguiente = self._agregar_recursivo(actual.siguiente, dato, prioridad)
        return actual

    # ====================== ELIMINAR MAYOR PRIORIDAD ======================
    def eliminar_mayor_prioridad(self):
        """Elimina y devuelve el elemento con mayor prioridad (el de adelante)"""
        if self.cabeza is None:
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        return dato

    # ====================== ELIMINAR POR VALOR (recursivo) ======================
    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato usando recursión"""
        self.cabeza = self._eliminar_recursivo(self.cabeza, dato)
    
    def _eliminar_recursivo(self, actual, dato):
        if actual is None:
            return None
        if actual.dato == dato:
            return actual.siguiente   # saltamos este nodo
        actual.siguiente = self._eliminar_recursivo(actual.siguiente, dato)
        return actual

    # ====================== MOSTRAR (recursivo) ======================
    def mostrar(self):
        self._mostrar_recursivo(self.cabeza)
        print("None")

    def _mostrar_recursivo(self, nodo):
        if nodo:
            print(f"[{nodo.dato}(p{nodo.prioridad})] → ", end="")
            self._mostrar_recursivo(nodo.siguiente)


# ====================== EJEMPLO DE USO ======================
if __name__ == "__main__":
    lista = ListaLigadaPrioridad()

    lista.agregar("Tarea A", 5)
    lista.agregar("Tarea B", 2)
    lista.agregar("Tarea C", 8)
    lista.agregar("Tarea D", 2)   # misma prioridad que B

    print("Lista después de agregar:")
    lista.mostrar()
    # Salida: [Tarea B(p2)] → [Tarea D(p2)] → [Tarea A(p5)] → [Tarea C(p8)] → None

    print("\nEliminado (mayor prioridad):", lista.eliminar_mayor_prioridad())  # elimina B
    lista.mostrar()

    lista.eliminar("Tarea C")   # elimina por valor (recursivo)
    print("\nDespués de eliminar Tarea C:")
    lista.mostrar()