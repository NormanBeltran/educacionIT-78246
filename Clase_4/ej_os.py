import os

os.system("cls")  # on Windows use 'cls', on Linux/Unix use 'clear'

print (os.listdir())
print(os.getcwd())

if os.path.exists(r"C:\EducacionIT\Python Programming\78246"):
    print("El directorio existe")

os.system("dir ej*")  # on Windows use 'calc', on Linux/Unix use 'gnome-calculator'

print("Fin de Programa")