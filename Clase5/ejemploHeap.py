datos = [5,3,8,1,2,9,4]

import heapq
heapq.heapify(datos)
print("Heap",datos)

heapq.heappush(datos,6)
print("Heap despues de agregar 6:", datos)

minimo = heapq.heappop(datos)
print("Elemento minimo extraido:", minimo)
print("Heap despues de extraer el minimo", datos)

datos2 = [(2, 'Alejandro'),(1, 'Bob'),(3, 'Carlos'),(2, 'Bety')]
heapq.heapify(datos2)
print("Heap con tuplas",datos2)


'''
Programa del hospital
Cada paciente tiene prioridad de 1 a 3, 1 es la mas importante
las personas del hospital deben saber quien es el siguiente en ser atendido
E indicar su nombre y su prioridad
'''
hospital = []

def agregar_paciente(nombre, prioridad):
    # heapq usa el primer valor para ordenar, así que ponemos prioridad primero
    heapq.heappush(hospital, (prioridad, nombre))
    print(f"Paciente {nombre} agregado con prioridad {prioridad}.")

# Función para atender al siguiente paciente
def atender_siguiente():
    if hospital:
        prioridad, nombre = heapq.heappop(hospital)
        print(f"Atendiendo a {nombre} con prioridad {prioridad}.")
    else:
        print("No hay pacientes para atender.")

# Agregamos algunos pacientes
agregar_paciente("Ana", 2)
agregar_paciente("Carlos", 1)
agregar_paciente("Beatriz", 3)
agregar_paciente("David", 1)

# Atendemos a todos los pacientes
while hospital:
    atender_siguiente()

'''
Un programa que ermita programamr tareas y me diga
cual es la siguiente tarea a realizar segun calendario
'''
import datetime

tareas = []

def tiempo_tarea(anio,mes,dia,hora):
    # Fecha de la tarea: año, mes, día, hora, minuto, segundo
    fecha_tarea = datetime(anio, mes, dia, hora, 0, 0)

    # Fecha actual
    ahora = datetime.now()

    # Calculamos cuánto falta
    tiempo_restante = fecha_tarea - ahora  # Esto es un timedelta

    # Convertimos a segundos
    return tiempo_restante.total_seconds()


def agregar_tarea(nombre, tiempo):
    # heapq usa el primer valor para ordenar, así que ponemos prioridad primero
    heapq.heappush(tareas, (tiempo, nombre))
    print(f"Tarea {nombre} agregada")


flag = "Y"
while flag != "N":
    nombre = input("Ingrese el nombre de la tarea")
    anio = input("Ingrese el año de entrega")
    mes = input("Ingrese el mes de entrega")
    dia = input("Ingrese el dia de entrega")
    hora = input("Ingrese el hora de entrega")

    tiempo = tiempo_tarea(anio,mes,dia,hora)
    agregar_tarea(nombre, tiempo)

    input("Si desea ingresar una nueva tarea ingrese Y, de lo contrario ingrese N")

print (tareas)