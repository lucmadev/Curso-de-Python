# Convertir USD a ARS

opcion = -1

menuInicio = """
    Calculadora de Moneda

    1 - Iniciar     2- Salir
            """


def interfaz():
    opcion = int(input(menuInicio))
    while opcion == 1 or opcion == 2:
        if opcion == 1:
            calcular()
            return
        elif opcion == 2:
            return
    print("Es una opcion invalida, abortando programa.")

def calcular():
    valor = float(input("Ingrese el valor de USD actual: "))
    cantidad = float(input("Ingrese la cantidad de USD que tenes: "))
    total = valor * cantidad
    print(f"Tenes {total} de ARS")


def main():
    interfaz()

if __name__ == '__main__':
    main()
