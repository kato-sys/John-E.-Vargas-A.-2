"""
John E. Vargas A.
Modulo de funciones para el editor
version: 1.0.0
creado el 17/05/23
ulima fecha modificado: 17/05/23
"""
# Se guarda la ruta del folder
rute = "proyecto_john/Editor de textos/"

# creamos variables necesarias para despues.
lines = []

# creamos las funciones necesarias.


def ver_texto():
    with open(rute + 'john', 'r') as file:
        for line in file:
            print(line)


def crear_titulo():
    with open(rute + 'john', 'a+') as file:
        titulo = input("que titulo desea darle a su texto?: ")
        formato1 = titulo.center(50, " ")
        formato2 = formato1.title()
        formato3 = formato2 + '\n'
        file.write(formato3)


def escribir():
    with open(rute + 'john', 'a+'):
        txt = input("Que desea escribir?: ")
        return txt


def alinear():
    with open(rute + 'john', 'a+') as file:
        align = input("ingrese 'l' para izquierda y 'r' para derecha: ")
        if align == "l":
            txt = escribir()
            txt_aligned = txt.ljust(25, " ")
            file.write(txt_aligned)
        elif align == "r":
            txt = escribir()
            txt_aligned = txt.rjust(25, " ")
            file.write(txt_aligned)
        else:
            print("Favor elegir una opcion valida")


def read_txt():
    with open(rute + 'john', 'r') as file:
        lines = file.read().splitlines()
        print(lines)


def cortar():
    with open(rute + 'john', 'r') as file:
        words = file.read()
    print("estas son sus palabras:")
    print(words)
    eleccion = input("que palabra desea borrar?: ")
    ntxt = words.replace(eleccion, "")
    with open(rute + 'john', 'w') as file:
        file.write(ntxt)


def mayusculas_todo():
    with open(rute + 'john', 'r') as file:
        words = file.read()
        text = str(words.upper())
    with (open(rute + 'john', "w")) as file:
        file.write(text)


def minuscula_todo():
    with open(rute + 'john', 'r') as file:
        words = file.read()
        text = str(words.lower())
    with (open(rute + 'john', "w")) as file:
        file.write(text)


def pegar():
    text = input("Que desea pegar?: ")
    line = int(input("En qué linea desea pegarlo?: "))

    with (open(rute + 'john', "r")) as file:
        lineas = file.readlines()
    lineas.insert(line - 1, text + '\n')

    with (open(rute + 'john', "w")) as file:
        file.writelines(lineas)


def eliminar_text():
    with open(rute + 'john', 'w'):
        return None
