#------------------------------------------------------------------------------------------
#1
#------------------------------------------------------------------------------------------


import re

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.
    """
    patron = r'^[A-Z]{3}-?\d{3}$'
    return bool(re.match(patron, placa))


def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    """
    patron = r'#\w+'
    return re.findall(patron, texto)


#------------------------------------------------------------------------------------------
#2
#------------------------------------------------------------------------------------------

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print(" Sin pedidos")
            return
        while actual:
            print(f" {actual}")
            actual = actual.siguiente

    def agregar(self, cliente, direccion, valor):
        nuevo = Pedido(cliente, direccion, valor)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self._agregar_rec(self.cabeza, nuevo)

    def _agregar_rec(self, nodo, nuevo):
        if nodo.siguiente is None:
            nodo.siguiente = nuevo
        else:
            self._agregar_rec(nodo.siguiente, nuevo)

    def valor_pendiente(self):
        return self._valor_pendiente_rec(self.cabeza)

    def _valor_pendiente_rec(self, nodo):
        if nodo is None:
            return 0
        if not nodo.entregado:
            return nodo.valor + self._valor_pendiente_rec(nodo.siguiente)
        return self._valor_pendiente_rec(nodo.siguiente)

    def eliminar_entregados(self):
        self.cabeza = self._eliminar_rec(self.cabeza)

    def _eliminar_rec(self, nodo):
        if nodo is None:
            return None
        if nodo.entregado:
            return self._eliminar_rec(nodo.siguiente)
        nodo.siguiente = self._eliminar_rec(nodo.siguiente)
        return nodo
    
#------------------------------------------------------------------------------------------
#3
#------------------------------------------------------------------------------------------

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


def estudiantes_en_todos():
    return club_ciencias & club_deportes & club_arte


def solo_un_club():
    solo_ciencias = club_ciencias - club_deportes - club_arte
    solo_deportes = club_deportes - club_ciencias - club_arte
    solo_arte = club_arte - club_ciencias - club_deportes

    return solo_ciencias | solo_deportes | solo_arte


def clubes_de_estudiante(nombre):
    clubes = []

    if nombre in club_ciencias:
        clubes.append("Ciencias")
    if nombre in club_deportes:
        clubes.append("Deportes")
    if nombre in club_arte:
        clubes.append("Arte")

    return clubes


#------------------------------------------------------------------------------------------
#4
#------------------------------------------------------------------------------------------

def escalones_sin_memo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return escalones_sin_memo(n-1) + escalones_sin_memo(n-2)


def escalones_con_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    if n == 1:
        return 1

    memo[n] = escalones_con_memo(n-1, memo) + escalones_con_memo(n-2, memo)
    return memo[n]
