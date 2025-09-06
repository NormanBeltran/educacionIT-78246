
# Para archivos de texto de menor tamaño

with open("unificar.txt", "w", encoding="utf-8") as unificar:
    with open("argentina.txt", "r", encoding="utf-8") as archivo1:
        contenido1 = archivo1.read()
        unificar.write(contenido1)
        unificar.write("\n")
    with open("usa.txt", "r", encoding="utf-8") as archivo2:
        contenido2 = archivo2.read()
        unificar.write(contenido2)
        unificar.write("\n")
