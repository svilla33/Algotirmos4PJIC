import time

class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel
        self.tiempo = time.time()

class Matchmaking:

    def __init__(self):
        self.cola = []

    def entrar_cola(self, jugador):

        candidato = None

        for j in self.cola:
            if abs(j.nivel - jugador.nivel) <= 150:
                if candidato is None or j.tiempo < candidato.tiempo:
                    candidato = j

        if candidato:
            self.cola.remove(candidato)
            print(f"Match: {jugador.id} vs {candidato.id}")
        else:
            self.cola.append(jugador)

mm = Matchmaking()

mm.entrar_cola(Jugador("A", 1200))
mm.entrar_cola(Jugador("B", 2000))
mm.entrar_cola(Jugador("C", 1300))