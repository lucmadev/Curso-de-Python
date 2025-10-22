num = 5


cuadrado = lambda num: num * num

hola = lambda nombre: print(f"Hola {nombre}")


estoEsUnEntero = lambda num: print("es un numero entero") if type(num) is int else print("no es un numero entero")


print(estoEsUnEntero(5))