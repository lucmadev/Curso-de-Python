#Pedir al usuario que ingrese una palabra. Contar cuántas
#vocales tiene y mostrar el resultado.

def contarVocales(palabra):
    total = 0
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            total += 1
    return total

def main():
    palabra = input("Ingrese la palabra a contar... \n")
    valor = contarVocales(palabra.lower())
    print(f"La palabra: {palabra} tiene {valor} vocales")



if __name__ == '__main__':
    main()