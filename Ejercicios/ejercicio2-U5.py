"""
Crear y llenar una lista con los números enteros del 50 al 200. [x]
Declarar una función lambda [x]
que usando MAP, cargue en otra lista el cuadrado de cada uno de los elementos de la primera lista. []
"""

listaOriginal = []

listaCuadrada = []

cuadrado = lambda num: num ** 2 


def main():

    for numero in range(50, 201):
        listaOriginal.append(numero)

    print(listaOriginal)

    print("-------------------------------------------------")

    listaCuadrada = list(map(cuadrado, listaOriginal))

    print(listaCuadrada)

if __name__ == '__main__':
    main()