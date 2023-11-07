"""
John E. Vargas A.
Editor de texto
version: 2.0.0
creado: 16/05/23
ultima fecha modificado: 17/05/23
"""
# Importamos las librerias necesarias
import fun_edit as fn
import os
import errno

# creamos el folder
rute = "proyecto_john/Editor de textos/"
try:
    os.makedirs(rute)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# creamos un loop
while True:
    print("titulo = 1 escribir = 2, leer = 3, mayuscula = 4, minuscula = 5")
    print("pegar = 6, cortar = 7, eliminar = 8 y finalizar = 9.")
    opcion = int(input("Que desea hacer?: "))
# Vemos que opcion se eligio y se ejecuta la funcion correspondiente.
    if opcion == 1:
        fn.crear_titulo()
    elif opcion == 2:
        fn.alinear()
    elif opcion == 3:
        fn.ver_texto()
    elif opcion == 4:
        fn.mayusculas_todo()
    elif opcion == 5:
        fn.minuscula_todo()
    elif opcion == 6:
        fn.pegar()
    elif opcion == 7:
        fn.cortar
    elif opcion == 8:
        fn.eliminar_text()
    elif opcion == 9:
        break
print(f"el programa finalizo este es su archivo: {fn.ver_texto()}")

"""
Profe, el resto los intente hacer pero la verdad es que no logre ver como
"""
