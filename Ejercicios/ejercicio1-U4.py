# Escribir un programa que consulte al usuario su edad y determinar si es mayor o menor de
# edad.

def main():

    edad = int(input("Ingrese su edad: \n"))

    # Validar el tipo de dato y que sea mayor a 0 osea que no sea negativo

    if edad >= 18:
        print("Es mayor")
    else:
        print("Es menor")

if __name__ == "__main__":
    main()