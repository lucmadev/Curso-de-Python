# # Escrituura

# txt = open('datos.txt', 'w') # w == Escritura

# lista = ["Fer", "Ceci", "Fran", 3456]

# for item in lista:
#     txt.write(str(item) + '\n')

# txt.close()


# Lectura

# txt = open('datos.txt', 'r') # r == Lectura

# archivo = []

# numeros = []

# linea = txt.readline()

# while linea != '':
#     print(linea, end='')
#     # for caracter in linea:
#     #     if caracter in '1234567890':
#     #         numeros.append(caracter)
            
#     # if type(numeros).__name__ == 'int' :
#     #     linea = numeros
#     archivo.append(linea.replace('\n', ''))

#     linea = txt.readline()

# txt.close()

# print(archivo)

#Solucion proporcionada por Francisco

txt = open('datos.txt', 'r') # r == Lectura

archivo = []

linea = txt.readline()

while linea != '':
    print(linea, end='')
    for caracter in linea:
        if caracter.isdigit():
            numeros = int(caracter)
            print(numeros)
            archivo.append(numeros)
    archivo.append(linea.replace('\n', ''))


    linea = txt.readline()

txt.close()

print(archivo)