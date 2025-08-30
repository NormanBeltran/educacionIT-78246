def calcular_iva(precio, detalle):
    iva = 0.21
    return f"{detalle} {precio * iva}"


def potencia(base, exponente):
    return base ** exponente

def normalizacion(lista):
    for nombre in lista:
        print(nombre.strip().title())

def ecuacion(x, y, z=2): # Ejemplo de valor por default z=2
    return (x + y) * z

print(calcular_iva(100, "El IVA calculado es :"))

print(potencia(exponente=3, base=2))

nombres = ["ana perez", "    JOSE PEREZ", "Juan RODRIGUEZ"]
retorno = normalizacion(nombres)

print(retorno)

print(ecuacion(4, 6, 4))