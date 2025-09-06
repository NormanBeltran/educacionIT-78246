# Ejemplo de escritura en un archivo de texto
# Ojo porque si el archivo ya existe, lo sobreescribe

with open("bandas.txt", "w", encoding="utf-8",) as archivo:
    archivo.write("Nirvana\n")
    archivo.write("Metallica\n")
    archivo.write("Queen\n")
    archivo.write("The Beatles\n")
    archivo.write("Pink Floyd\n")

with open("movies.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Inception\n")
    archivo.write("The Dark Knight\n")
    archivo.write("Interstellar\n")
    archivo.write("Pulp Fiction\n")
    archivo.write("The Matrix\n")