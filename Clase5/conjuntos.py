class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None

    def push(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")

        valor = self.tope.dato
        self.tope = self.tope.siguiente
        return valor

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")

        return self.tope.dato

#el profe usa una llamada usando pythontutor.com esta buena

def validar_balanceo(expresion):

    pila = Pila();

    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }                
    aperturas = set(pares.values())
    cierres = set(pares.keys())

    for token in expresion:
        if token in aperturas:
            pila.push(token)
            print(f"Agregando '{token}' a la pila. Pila actual: {pila}")
        elif token in cierres:
            if pila.esta_vacia() or pila.pop() != pares[token]:
                