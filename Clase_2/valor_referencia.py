def normalizacion(lista):
    for idx, nombre in enumerate(lista):
        nombre = nombre.strip().title()
        lista[idx] = nombre

def cambio(a,b,c):
    a = 300
    b = 400
    c = 500
    

nombres = ["ana perez", "    JOSE PEREZ", "Juan RODRIGUEZ"]
normalizacion(nombres)

print(nombres)

x = 1
y = 2
z = 3

cambio(x,z,y)
print(f"Variables x,y,z : {x} {y} {z}")
