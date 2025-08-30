def cuadrados(x):
    return x**2

def cubos(x):
    return x**3


lista = [2,4,6,8]

print( tuple(map(cuadrados, lista)) ) # Devuelve un objeto map (iterador)