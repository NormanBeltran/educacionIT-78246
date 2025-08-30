def sumar(*args):
    print(args)
    return sum(args)


def imprimir(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"Clave : {k} - Valor : {v}")

print(sumar(1,2,3,4,5,6,7,8))
print(sumar(1000, 2000))

imprimir(nombre="Ana", apellido="Perez", edad=28)