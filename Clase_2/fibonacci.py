def fib_acum(n):
    if n <= 2:
        return('El numero debe ser mayor a 2')
    elementos = [0,1]
    while len(elementos) < n:
        elementos.append(elementos[-1] + elementos[-2])
    return elementos

n = int(input('Introduzca el numero con el cual desea hacer la serie de fibonacci: '))

print(fib_acum(n))