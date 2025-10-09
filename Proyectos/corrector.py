
def calcularPuntaje(hechos,totalEjercicios):
    nota = (hechos / totalEjercicios) * 100 if totalEjercicios > 0 else 0
    return nota


def main():

    hechos = float(input("Ingrese los ejercicios hechos\n"))
    totalEjercicios = int(input("Ingrese la cantidad de ejercicios que tiene el TP\n"))

    while hechos != 0:
        nota = calcularPuntaje(hechos, totalEjercicios)
        print(f"{nota:.2f}")
        hechos = float(input("Ingrese los ejercicios hechos\n"))

    opcion = input("Vas a corregir otro tp? N / S").lower()

    if opcion == "S":
        main()
    else:
        pass


if __name__ == '__main__':
    main()