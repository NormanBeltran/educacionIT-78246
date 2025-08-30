def cuadrados(x):
    return x**2

def cubos(x):
    return x**3


def aplicar_funcion(funcion, lista):    # Funcion de Orden Superior (pq recibe una funcion como parametro)
    return [funcion(x) for x in lista]


lista = [2,4,6]
print(aplicar_funcion(cubos, lista))

