# por cada alumno sumar +1 presente

alumnos = ["Valen", "Ceci", "Francisco", "Jose"]
presentesDeAlumnos = [15, 0, 0, 0]

for i in range(0,4):
    presentesDeAlumnos [i] = presentesDeAlumnos [i] +  1
    print(f"Alumno: {alumnos[i]} presentes: {presentesDeAlumnos[i]}" )



def hola(nombre):
    print(f"Hola {nombre}")

nombre = input("Escribe tu nombre: ")

while nombre != '0':
    hola(nombre)
    nombre = input("Escribe tu nombre: ")
