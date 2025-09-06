"""
r - read - leer
w - write - escribir (si el archivo existe, lo sobreescribe)
a - append - agregar (si el archivo existe, agrega al final)

"""

# Para archivos de texto de menor tamaño

with open("peliculas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)


# Para archivos de texto de mayor tamaño
# lee línea por línea
with open("peliculas.txt", "r", encoding="utf-8") as archivo:
    contador = 1
    for linea in archivo:
        print(f"{contador}: {linea}", end="")
        contador += 1