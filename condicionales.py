# si alumnoNota es igual o mayor a 7 -> aprueba sino -> desaprueba

alumno = ["Ceci", 9, None]

"""
 == es igual
 > es mayor
 < es menor
 >= es mayor o igual
 <= es menor o igual
 != o es desigual
"""


if alumno[1] >= 7:
    alumno[2] = True
else:
    alumno[2] = False

print(f"Alumno: {alumno[0]} esta aprobado? {alumno[2]}")




