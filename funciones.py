
def hola(nombre):
    print(f"Hola {nombre}")


def sumar(num1, num2):
    resultado = num1 + num2
    #mucha logica :)

    return resultado

suma1 = sumar(78,14)
suma2 = sumar(50,10)
suma3 = suma1 + suma2

def suma(*x):
    total = 0
    for valor in x:
        valor = int(valor)
        total = total + valor
    print(total)

def menu():
    print("Menu de opciones...")
    print("1 - Sumar")
    print("2 - Saludar")

    opcion = int(input("Escribe tu eleccion...\n"))

    match opcion:
        case 1:
            num = input("Ingresa numeros para sumar separados con una coma \n")
            nums = num.split(",")
            suma(*nums)
        case 2:
            nombre = input("Ingresa un nombre: ")
            hola(nombre)

def main():
    menu()


if __name__ == '__main__':
    main()