import sqlite3

#_____________________________________________ Funciones _____________________________________________#

def crear_tabla():

    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        salario REAL,
                        depto TEXT,
                        posicion TEXT,
                        fecha_ingreso TEXT NOT NULL,
                        edad INTEGER NOT NULL
                   )
                   ''')
    conn.commit()


def insertar():
    personas = (("Jose",     50000, "Finanzas",     "Jefe", "2010-01-01", 30),
                ("Antonia", 100000, "RRHH",         "Empleado", "2012-01-01", 10),
                ("Pedro",   150000, "Sistemas",     "Supervisor", "2015-01-01", 40),
                ("Mariana",  75000, "Legales",      "Analista", "2013-01-01", 25),
                ("Marina",  200000, "Contabilidad", "Director", "2011-01-01", 45),
                ("Lucas",   125000, "Presidencia",  "Secretaria", "2012-01-01", 21))
    
    for nombre, salario, depto, posicion, fecha_ingreso, edad in personas:
        cursor.execute("INSERT INTO empleados (nombre, salario, depto, posicion, fecha_ingreso, edad) VALUES (?, ?, ?, ?, ?, ?)", \
                       (nombre, salario, depto, posicion, fecha_ingreso, edad))
    conn.commit()


def insertar_uno(nombre, salario, depto, posicion, fecha_ingreso, edad):
    cursor.execute("INSERT INTO empleados (nombre, salario, depto, posicion, fecha_ingreso, edad) VALUES (?, ?, ?, ?, ?, ?)", \
                   (nombre, salario, depto, posicion, fecha_ingreso, edad))
    conn.commit()


def consultar():
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)

def consultar_uno(id):
    cursor.execute("SELECT * FROM empleados WHERE id = ?", (id,))
    empleado = cursor.fetchone()
    if empleado:
        print(empleado)
    else:
        print(f"No se encontro empleado con id {id}")

def consultar_like(nombre):
    cursor.execute("SELECT * FROM empleados WHERE nombre LIKE ?", (f"%{nombre}%",)  )
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)        

def actualizar_salario(id, nuevo_salario):
    cursor.execute("UPDATE empleados SET salario = ? WHERE id = ?", (nuevo_salario, id))
    conn.commit()

def borrar_uno(id):
    cursor.execute("DELETE FROM empleados WHERE id = ?", (id,))
    conn.commit()    
    
#_____________________________________________ Programa Principal _____________________________________________#

conn = sqlite3.connect("empleados.db")
cursor = conn.cursor()

crear_tabla()

#insertar()
#insertar_uno("Juan", 60000, "Marketing", "Coordinador", "2025-09-13", 28)
#insertar_uno("Ana", 50000, "IT", "Soporte Tecnico", "2025-09-13", 25)

#consultar()
#consultar_uno(15)
#consultar_like("n")

#actualizar_salario(4, 100000)
borrar_uno(3)

consultar()

conn.close()