class Nodo:
    def __init__(self, documento, nombre):#supongamos que son pacientes de un hospital
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None
        self.cola = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def AgregarAlFinal(self, documento, nombre):
        nodo = Nodo(documento,nombre)

        if self.cabeza == None:
            self.cabeza =nodo
            self.cola = nodo
        else:
            self.cola.siguiente = nodo
            self.cola = nodo

    def MostrarPacientes(self):
        actual = self.cabeza
        print(actual.nombre, actual.documento)

        while actual.siguiente != None: #tambien puede ser simplemente "actual.siguiente:"
            actual = actual.siguiente
            print(actual.nombre, actual.documento)
            

        


pacientes = Lista()

pacientes.AgregarAlFinal(123,"carlos")
pacientes.AgregarAlFinal(999,"fernanda")

pacientes.MostrarPacientes()


            

    
        








