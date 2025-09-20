import requests


nombres = ["Pedro", "Juan", "Maria", "Luis"]
emails = ["pedro@gmail.com", "juan@gmail.com", "maria@gmail.com", "luis@gmail.com"]
mensajes = ["Hola", "Chau", "Buenos dias", "Buenas tardes"]

"""
datos = {
     "name": "PEDRO PICAPIEDRA",
    "email": "pp@gmail.com",
    "message": "Hola, esto es un mensaje de prueba"
}
"""

for n, e, m in zip(nombres, emails, mensajes):
    datos = {
        "name": n,
        "email": e,
        "message": m
    }

    r = requests.post("http://localhost:8880/form", data=datos)

    if "Mensaje enviado" in r.content.decode("utf-8"):
        print(f"SC: {r.status_code} Formulario enviado correctamente")
    else:
        print(f"SC: {r.status_code} Error al enviar el formulario")