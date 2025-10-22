"""Ejercicio 5
Escribir un programa que permita el ingreso por teclado de palabras, tantas como el
usuario desee. Para finalizar el ingreso, el usuario deberá ingresar la siguiente frase: “Fin
del ingreso”.
Una vez finalizado el ingreso, mostrar por pantalla, la cantidad de letras ingresadas en total y la cantidad de cada vocal.
"""

"""Error: cuando le doy play, le pide al usuario un numero en ves de palabras"""

def main():
    carga = True
    palabras = ''
    cantidadA = 0
    cantidadE = 0
    cantidadI = 0
    cantidadO = 0
    cantidadU = 0
    cantidadLetra = 0

    while carga == True:
        palabra = input("Ingrese la palabra que necesite contar sus letras y vocales: ").lower()
        if palabra == "fin del ingreso":
            break
        palabras = palabras + palabra

    for letra in palabras:
        cantidadLetra += 1
        if letra == "a":
            cantidadA += 1
        elif letra == "e":
            cantidadE += 1
        elif letra == "i":
            cantidadI += 1
        elif letra == "o":
            cantidadO += 1
        elif letra == "u":
            cantidadU += 1

    print(cantidadA)
    print(cantidadE)
    print(cantidadI)
    print(cantidadO)
    print(cantidadU)
    print(cantidadLetra)


if __name__ == '__main__':
    main()