"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN C
                    Sistema de Cola de Atención al Cliente
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Un banco necesita un sistema para gestionar la cola de clientes en espera.
Los clientes tienen diferentes tipos de atención (preferencial, normal) y
se debe poder atender, consultar y gestionar la cola.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Cliente) con los atributos necesarios
2. Diseñar la clase Lista (Cola) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos
6. Calificación: 0.0 a 5.0

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Cliente):
   - Debe almacenar: nombre, tipo de atención (preferencial/normal), 
     tiempo estimado de atención en minutos
   - Debe poder enlazarse con otro cliente

b) Clase LISTA (Cola):
   - Los clientes preferenciales van al INICIO
   - Los clientes normales van al FINAL


PUNTO 2 (1.0): AGREGAR CLIENTE - RECURSIVO
------------------------------------------
Implementa un método para agregar un cliente.
- Si es preferencial: insertar al inicio de los preferenciales
- Si es normal: insertar al final de la cola
- OBLIGATORIO usar recursividad para encontrar la posición


PUNTO 3 (1.0): TIEMPO DE ESPERA - RECURSIVO
-------------------------------------------
Implementa un método que calcule el tiempo de espera de un cliente
dado su nombre (suma de tiempos de todos los que están antes).
- OBLIGATORIO usar recursividad
- Retorna -1 si el cliente no está en la cola


PUNTO 4 (1.0): ATENDER SIGUIENTE
--------------------------------
Implementa un método que retire y retorne el primer cliente de la cola.
- Retorna None si la cola está vacía


PUNTO 5 (1.0): CONTAR POR TIPO - RECURSIVO
------------------------------------------
Implementa un método que cuente cuántos clientes hay de cada tipo.
- OBLIGATORIO usar recursividad
- Retorna una tupla (preferenciales, normales)

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Cliente)
class Cliente:
    def __init__(self, nombre, atencion, tiempo):
        self.nombre = nombre
        self.atencion = atencion
        self.tiempo = tiempo
        self.siguiente = None




# PUNTO 1b: Clase Lista (Cola)

class Cola:
   def __init__(self):
      self.cabeza = None

   def agregar(self, nombre, atencion, tiempo):

      self.cabeza = self._agregar_recursivo(self.cabeza, nombre, atencion, tiempo)
    
   def _agregar_recursivo(self, actual, nombre, atencion, tiempo):

      

      if actual is None or actual.atencion == "normal": 
         nuevo = Cliente(nombre, atencion, tiempo)
         nuevo.siguiente = actual
         return nuevo


      

      actual.siguiente = self._agregar_recursivo(actual.siguiente, nombre, atencion, tiempo)
      return actual
   
   def mostrar(self):
      self._mostrar_recursivo(self.cabeza)
      print("None")

   def _mostrar_recursivo(self, nodo):
        if nodo:
            print(f"{nodo.nombre} → ", end="")
            self._mostrar_recursivo(nodo.siguiente)

#terminado punto 3
   def tiempo_espera(self,nombre, total = 0):
      actual = self.cabeza
      
      return self._tiempo_espera_recursivo(self.cabeza,nombre,total)
     

   def _tiempo_espera_recursivo(self, nodo,nombre,total):
      
      if nombre != nodo.nombre: #este es el cambio (creo) cambio hecho jiji         
 
         total += nodo.tiempo #¿como saco esto de la funcion????
         return self._tiempo_espera_recursivo(nodo.siguiente,nombre,total)  
      else:
         return total 


   #terminado punto 4
   def atender(self):        
        if self.cabeza is None:
            return None
        dato = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return dato

   def contar_por_tipo(self, normal = 0, preferencial = 0):
      return self._contar_por_tipo_recursivo(self.cabeza, normal, preferencial)
     

   def _contar_por_tipo_recursivo(self, nodo, normal, preferencial):
         
         if nodo:
           
            if nodo.atencion == "normal":
                normal +=1
                
            if nodo.atencion == "preferencial":
                preferencial +=1
               
            return self._contar_por_tipo_recursivo(nodo.siguiente,normal,preferencial)   
         else:
            # Contar por tipo: (2 preferenciales, 2 normales)      

            return preferencial , " preferenciales , ",normal," normales"
            

      



       

   '''
   def tiempo_espera(self,nombre):
      self._tiempo_espera_recursivo(self.cabeza,nombre)
      print("None")

   def _tiempo_espera_recursivo(self, nodo,nombre):
      if nombre != nodo.nombre: #este es el cambio (creo)
         print(f"{nodo.nombre} → ", end="")
         self._tiempo_espera_recursivo(nodo.siguiente,nombre)   

   '''


    

# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════


if __name__ == "__main__":
    cola = Cola()
    
    # Agregar clientes
    cola.agregar("Juan", "normal", 10)
    cola.agregar("María", "preferencial", 5)
    cola.agregar("Pedro", "normal", 15)
    cola.agregar("Antonio", "normal", 3)
    cola.agregar("Ana", "preferencial", 8)

    print("Por tipo:", cola.contar_por_tipo())
    
    # Orden esperado: María, Ana, Juan, Pedro (preferenciales primero)
    cola.mostrar()

    print("Espera de Pedro:", cola.tiempo_espera("Pedro"))

    # Atender siguiente (María)
    atendido = cola.atender()
    print("Atendido:", atendido.nombre)

    atendido = cola.atender()
    print("Atendido:", atendido.nombre)

    
    

"""
    # Tiempo de espera de Pedro: 5 + 8 + 10 = 23 minutos
    print("Espera de Pedro:", cola.tiempo_espera("Pedro"))
    
    # Contar por tipo: (2 preferenciales, 2 normales)
    print("Por tipo:", cola.contar_por_tipo())
    
    # Atender siguiente (María)
    atendido = cola.atender()
    print("Atendido:", atendido.nombre)
"""