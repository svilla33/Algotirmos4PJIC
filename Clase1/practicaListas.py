

class Nodo:
    def __init__(self, documento, nombre):#supongamos que son pacientes de un hospital
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None
        self.cola = None
        
#lista ligada simple
class Lista_Ligada_Simple:
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

    #else mal optimizado, tiene que recorrer todo el nodo

        ''' 
        else:
            actual = self.cabeza
            while actual.siguiente != None: #tambien puede ser simplemente "actual.siguiente:"
                actual = actual.siguiente
            actual.siguiente = nodo
        '''
  
class Lista_Ligada_Simple_Circular:
    def __init__(self):
        self.cabeza=None

    def AgregarAlFinal():



    
        








