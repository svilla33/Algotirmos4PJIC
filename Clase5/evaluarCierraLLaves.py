def cierreLLaves2 (expresion,llaves):
    # 1.evaluar si la pila esta vacia}
    pila = []
    for letra in expresion:
        if letra == "{" or letra == "(" or letra == "[":
            pila.append(letra)
        else:
            if pila[-1] == llaves[letra]:
                pila.pop()
            else:
                return "Expresion Incorrecta"

    return "expresion correcta"

def cierreLLaves (expresion):
    # 1.evaluar si la pila esta vacia}
    pila = []
    for letra in expresion:
        if letra == "{" or letra == "(" or letra == "[":
            pila.append(letra)
        else:
            match letra:
                case "]":
                    if pila[-1] == "[":
                        pila.pop()
                    else:
                        return "Expresion Incorrecta"
                case ")":
                    if pila[-1] == "(":
                        pila.pop()
                    else:
                        return "Expresion Incorrecta"
                case "}":
                    if pila[-1] == "{":
                        pila.pop()
                    else:
                        return "Expresion Incorrecta"

    return "expresion correcta"

llaves = {
    ")": "(",
    "]": "[",
    "}": "{"
}

expresion = "((([{{[()][( )]}}[]])))"

print(cierreLLaves2(expresion,llaves))

print(cierreLLaves(expresion))


'''

dic = {
    "a": 1,
    "b": 2,
    "c": 3
}

codigo de apoyo:

lista.pop(1)

def peek(pila):
    if pila:
        return pila[-1]
    return None


def peek(pila):
    if pila:
        return pila[-1]
    return None

match letra:
    case 'a':
        print("Es a")
    case 'b':
        print("Es b")
    case 'c':
        print("Es c")
    case _:
        print("Otro valor")

texto = "abc"

pila = []

for letra in texto:
    pila.append(letra)

print(pila)

texto = "abc"

for letra in texto:
    if letra == 'a':
        print("Encontré una a")

letra = 'b'

'''


