def suma(*x):
    total = 0
    for valor in x:
        valor = int(valor)
        total = total + valor
    print(total)

def hola(nombre):
    print(f"Hola {nombre}")