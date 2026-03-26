import re

# santiagovilla333@gmail.com
# santiago_banol82242@elpoli.edu.co
# test234@22-ss.au

# malo67@-22-ss.au
# malo1273@22-ss-.au

while True:
    correo = input("Ingresa un correo")

    if re.fullmatch(r"^([\w]+)@(A-Za-z0-9)([A-Za-z0-9-])+(A-Za-z0-9)\.(A-Za-z0-9)$", correo):
        break

    print("Correo ingresado no valido")

print("Correo agregado exitosamente")


while True:
    contrasenia = input("Ingresa una contreseña segura, debe tener ")

    if re.fullmatch(r"\d+", contrasenia):
        break

    print("Numero ingresado no valido")

print("Numero agregado exitosamente")

'''
 def validar_regex_input(regex, valor):
    while True:
        texto = input("Ingresa un", valor)
        
        if re.fullmatch(regex, texto):
            return texto
        print(valor, "ingresado no valido")
    print("Correo agregado exitosamente")
    
 '''
