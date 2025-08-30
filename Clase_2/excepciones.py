a = 10
b = int(input("Ingrese un numero: "))
lista = [1,2,3,4,5,6,7,8,9,10]

"""
try:
    print(a/b)
    print(lista[20])

except ZeroDivisionError:
    print("Error: División por cero no permitida.")

except IndexError:
    print("Error: Índice fuera de rango.")

"""
"""
try:
    print(a/b)
    print(lista[20])

except (ZeroDivisionError, IndexError):
    print("Se produjo un error: División o Index Error.")

"""
a = 100

try:
    print(a/b)
    #int(a)
    #print(lista[20])
except Exception as e:
    print("Se produjo un error: ", e.__class__)
    print("Cause              : ", e)
    b = 1
else:
    print("No se produjo ninguna excepción.")    
finally:    
    pass    

c = a/b
print("Fin de programa")    
