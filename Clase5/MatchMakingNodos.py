class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def enqueue(self, valor):
        nuevo = Nodo(valor)

        if self.esta_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        valor = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        return valor

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        return self.frente.dato
    
class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel

class Matchmaking:

    def __init__(self):
        self.cola = Cola()

    def entrar_cola(self, jugador):

        if self.cola.esta_vacia():
            self.cola.enqueue(jugador)
            return

        anterior = None
        actual = self.cola.frente

        while actual:

            otro = actual.dato

            if abs(otro.nivel - jugador.nivel) <= 150:

                print(f"Match: {jugador.id} vs {otro.id}")

                # eliminar nodo de la cola
                if anterior is None:
                    self.cola.frente = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                if actual == self.cola.final:
                    self.cola.final = anterior

                return

            anterior = actual
            actual = actual.siguiente

        # si no encontró pareja
        self.cola.enqueue(jugador)


matchMaking = Matchmaking()

matchMaking.entrar_cola(Jugador("A",1200))
matchMaking.entrar_cola(Jugador("B",2000))
matchMaking.entrar_cola(Jugador("C",1300))
matchMaking.entrar_cola(Jugador("D",1180))