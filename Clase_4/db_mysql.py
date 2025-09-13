# pip install pymysql

import pymysql

#_________________________________ Funciones
def conexion():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='EducacionIT',
            db='movies'
        )
        print("Conexión correcta")
        return conn
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)


def crear_peliculas(conn):
    try:
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            insertar = "INSERT INTO peliculas (titulo, anio) VALUES (%s, %s);"
            cursor.execute(insertar, ("Titanic", 1997))
            cursor.execute(insertar, ("Avatar", 2009))
            cursor.execute(insertar, ("El Padrino", 1972))
            cursor.execute(insertar, ("Pulp Fiction", 1994))
            cursor.execute(insertar, ("Forrest Gump", 1994))
            cursor.execute(insertar, ("El Señor de los Anillos: El retorno del Rey", 2003))
            cursor.execute(insertar, ("Matrix", 1999))
            cursor.execute(insertar, ("Interestelar", 2014))
            cursor.execute(insertar, ("Gladiador", 2000))
            cursor.execute(insertar, ("La La Land", 2016))
            cursor.execute(insertar, ("El Rey León", 1994))
            cursor.execute(insertar, ("El Silencio de los Corderos", 1991))
            cursor.execute(insertar, ("El Club de la Pelea", 1999))
            cursor.execute(insertar, ("Jurassic Park", 1993))
            cursor.execute(insertar, ("Avatar: El Camino del Agua", 2022))
            cursor.execute(insertar, ("La Lista de Schindler", 1993))

        conn.commit()
        
    except pymysql.MySQLError as e:
        print("Ocurrió un error al insertar en la tabla: ", e)


def crear_una_pelicula(conn, titulo, anio):
    try:
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            insertar = "INSERT INTO peliculas (titulo, anio) VALUES (%s, %s);"
            cursor.execute(insertar, (titulo, anio))
        conn.commit()
    except pymysql.MySQLError as e:
        print("Ocurrió un error al insertar en la tabla: ", e)

def consultar_peliculas(conn):
    try:
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM peliculas")
            peliculas = cursor.fetchall()
            for pelicula in peliculas:
                print(pelicula)
    except pymysql.MySQLError as e:
        print("Ocurrió un error al consultar en la tabla: ", e)    

def consultar_una_pelicula(conn, id):
    try:
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM peliculas WHERE id = %s", (id,))
            pelicula = cursor.fetchone()
            if pelicula:
                print(pelicula)
            else:
                print(f"No se encontró la película con id {id}")
    except pymysql.MySQLError as e:
        print("Ocurrió un error al consultar en la tabla: ", e)  

def consultar_peliculas_like(conn, titulo): 
    try:
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM peliculas WHERE titulo LIKE %s", (f"%{titulo}%",))
            peliculas = cursor.fetchall()
            for pelicula in peliculas:
                print(pelicula)
    except pymysql.MySQLError as e:
        print("Ocurrió un error al consultar en la tabla: ", e)   

def actualizar_anio(conn, id, anio):
    try:
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            actualizar = "UPDATE peliculas SET anio = %s WHERE id = %s"
            cursor.execute(actualizar, (anio, id))
        conn.commit()
    except pymysql.MySQLError as e:
        print("Ocurrió un error al actualizar en la tabla: ", e)                       

def eliminar_pelicula(conn, id):
    try:
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            eliminar = "DELETE FROM peliculas WHERE id = %s"
            cursor.execute(eliminar, (id, ))
        conn.commit()
    except pymysql.MySQLError as e:
        print("Ocurrió un error al eliminar en la tabla: ", e)

#_________________________________ Conexión a la base de datos

conn = conexion()

#crear_peliculas(conn)
#crear_una_pelicula(conn, "The Game", 1997)
#crear_una_pelicula(conn, "Mente Indomable", 1997)
#crear_una_pelicula(conn, "Alien", 1982)
#crear_una_pelicula(conn, "Kingsman", 2017)
#crear_una_pelicula(conn, "Old boy", 2003)   
#crear_una_pelicula(conn, "La pistola desnuda", 1988)   

#consultar_peliculas(conn)
#consultar_una_pelicula(conn,  33)
#consultar_peliculas_like(conn, "eñ")

#actualizar_anio(conn, 19, 1985)
eliminar_pelicula(conn, 19)

consultar_peliculas(conn)

conn.close()