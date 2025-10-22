"""Escribir un programa que le pida al usuario que ingrese un número por teclado, lo eleve al
cubo y muestre el resultado por pantalla. El programa deberá seguir funcionando hasta
que el usuario ingrese el número cero."""


def main():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            if num == 0:
                print("Saliendo del programa...")
                break

            num = num ** 3
            print(num)
        except ValueError:
            print("Eso no es un numero. Escribe solo numeros")

if __name__ == '__main__':
    main()