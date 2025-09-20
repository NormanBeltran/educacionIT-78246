import requests
import json

#_______________________________________________________________ Funciones

def consultar():
    r = requests.get("http://localhost:7001/student")
    print(f"Status Code: {r.status_code}\nRespuesta:{r.json()}")

def consultar_por_id(id):
    r = requests.get("http://localhost:7001/student/"+str(id))
    print(f"Status Code: {r.status_code}\nRespuesta:{r.json()}")

def crear(name, courses):
    r = requests.post("http://localhost:7001/student", json={"name":name, "courses":courses})
    print(f"Status Code: {r.status_code}\nRespuesta:{r.json()}")

def modificar(id, name, courses):
    r = requests.put("http://localhost:7001/student/"+str(id), json={"name":name, "courses":courses})
    print(f"Status Code: {r.status_code}")

def eliminar(id):
    r = requests.delete("http://localhost:7001/student/"+str(id))
    print(f"Status Code: {r.status_code}")

#_______________________________________________________________ Main

#crear("Maria Perez", 4)
#crear("Juan Gomez", 5)
#crear("Pedro Alvarez", 6)
#crear("Ana Fernandez", 7)
#consultar_por_id(0)
#consultar_por_id(99)
modificar(3, "PEDRO PICAPIEDRA", 77)
eliminar(0)
consultar()