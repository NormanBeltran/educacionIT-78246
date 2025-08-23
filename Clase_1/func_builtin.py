amigos = ['Juan', 'Pedro', 'Maria', 'Luis', 'Pedro', 'Juan', 'Ana', 'Carlos', "Juan"]
apellido = ["Perez", "Gomez", "Lopez", "Diaz", "Martinez", "Sanchez", "Torres", "Ramirez", "Hernandez"]

for idx, amigo in enumerate(amigos):
    print(idx, amigo, apellido[idx])


for nombre, apellido in zip(amigos, apellido):
    print(nombre, apellido)
