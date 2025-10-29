import sqlite3

# Crear base de datos

# db = sqlite3.connect("icq.db")

# cursor = db.cursor()

# cursor.execute('create table if not exists alumnos (nombre varchar(100), apellido varchar(100))')

# db.close()

# Insertando datos en la Base de datos (XD)

db = sqlite3.connect("icq.db")

cursor = db.cursor()

alumno1 = ("Javier", "Aguirre")

alumno2 = ("Evelyn","Morel")

cursor.execute(f'insert into alumnos values {alumno1}, {alumno2}')

db.commit()

db.close()


def insertar(alumno):
    
    cursor.execute(f'insert into alumnos values {alumno}')

    db.commit()