""""
John E. Vargas A.
ahorcado
version: 1.0.0
creado: 12/05/23
ultima vez modificado: 12/05/23
"""
import random

# creamos el banco de palabras
lista = ("luna", "python", "arbol", "perico", "guitarra", "bajo", "botella")

# Elejimos una palabra random.
random_index = random.randint(0, 7)
palabra_random = lista[random_index]

# printeamos la cantidad de letras de la palabra
print(f"La palabra tiene {len(palabra_random)} letras:")
car = []
palabra = []
for i in palabra_random:
    car.append("_")
print(*car)
for i in palabra_random:
    palabra.append(i)

# Creamos un loop con 8 intenos max
intentos = 0
contador = 0
usados = []
while car != palabra and intentos < 8:
    letra = input("Digite una letra: ")
    if letra not in palabra_random:
        print("La letra no esta en la palabra, intentalo de nuevo.")
        intentos += 1
        usados.append(letra)
        print(f"las letras usadas son: {usados}")
        print(*car)
    elif letra in usados:
        print("Ya intentaste esta letra")
        pass
    elif letra in car:
        print("Ya esta en la palabra")
        pass
    else:
        i = 0
        lon = len(palabra)
        while i < lon:
            if letra == palabra[i]:
                car[i] = letra
                contador += 1
                print(*car)
            i += 1

if intentos < 8:
    print(f"Ganaste en tan solo {intentos + contador} intentos!")
    print(f"con tan solo {intentos} malas!")
else:
    print(f"Perdiste! la palabra era: {palabra_random}")
