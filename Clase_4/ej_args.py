import sys


print("mostrar args", sys.argv, type(sys.argv))

for i in sys.argv[1:]:
    print(f"Hola {i}")