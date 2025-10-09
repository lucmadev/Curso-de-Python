# Pedir al usuario un número entero. Mostrar por pantalla la
# tabla de multiplicar de ese número desde el 1 hasta el 10.


def tabla(num):
    print("\n---------------------\n")
    for i in range(1,11): # 3
        valor = num * i # 30
        print(f"{valor} ")
    print("\n---------------------\n")
    
def main():
    num = int(input("Ingrese la tabla  a visualizar... \n"))
    tabla(num) # 10



if __name__ == '__main__':
    main()