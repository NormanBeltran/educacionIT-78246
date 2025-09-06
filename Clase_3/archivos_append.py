# Ejemplo de escritura en un archivo de texto con append

with open("juegos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("The Legend of Zelda: Breath of the Wild\n")
    archivo.write("Super Mario Odyssey\n")
    archivo.write("Dark Souls III\n")
    archivo.write("The Witcher 3: Wild Hunt\n")
    archivo.write("DOOM Eternal\n")

with open("juegos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Uno\n")
    archivo.write("Ajedrez\n")
    archivo.write("TEG\n")
    archivo.write("Monopoly\n")
    archivo.write("Damas Chinas\n")
