class Estudiante:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

estudiente1 = Estudiante("Juan", 111)

print(estudiente1.nombre,estudiente1.documento)