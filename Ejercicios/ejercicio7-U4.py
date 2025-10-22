"""
Crea una función llamada modificar() que a partir de una lista de números realice las
siguientes tareas sin modificar la original:

- Borrar los elementos duplicados.
- Ordenar la lista de mayor a menor.
- Eliminar todos los números impares.
- Realizar una suma de todos los números que quedan.
- Añadir como primer elemento de la lista la suma realizada.
- Devolver la lista modificada.

Una vez escrita la función, utilizarla y verificar que el primer elemento de dicha lista,
coincide con la suma de los demás elementos.
"""

def modificar(nums):
    numsPares = []
    numsInstancia = sorted(list(set(nums)), reverse=True)

    for num in numsInstancia:
        if num % 2 == 0:
            numsPares.append(num)

    suma = sum(numsPares)
    numsPares.insert(0, suma)

    return numsPares


def main():
    numsOriginal = [1,8,9,3,4,5,2,1,9,8,2,5,7,3,9]

    numsModificados = modificar(numsOriginal)

    if numsModificados[0] == (sum(numsModificados[1:])):
        print("Suma verificada :)")

    print(numsModificados)

if __name__ == "__main__":
    main()