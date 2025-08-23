"""
Colecciones

1. Orden (importancia del orden para la coleccion)
2. Mutabilidad (si la coleccion puede ser modificada o no)
3. Repetición de elementos (pueden repetirse elementos en la colección)


- Listas
  - Orden: Las listas mantienen el orden de inserción de los elementos.
  - Mutabilidad: Las listas son mutables, se pueden modificar después de su creación.
  - Repetición: Las listas permiten elementos duplicados.

- Tuplas
  - Orden: Las tuplas mantienen el orden de inserción de los elementos.
  - Mutabilidad: Las tuplas son inmutables, no se pueden modificar después de su creación.
  - Repetición: Las tuplas permiten elementos duplicados.

- Diccionarios
  - Orden: No es importante para los diccionarios
  - Mutabilidad: Los diccionarios son mutables, se pueden modificar después de su creación, se pueden eliminar o agregar elementos.
  - Repetición: Los diccionarios no permiten claves duplicadas, pero los valores pueden repetirse.

- Conjuntos
  - Orden: No es importante para los conjuntos.
  - Mutabilidad: Los conjuntos son mutables, pueden eliminar o agregar elementos.
  - Repetición: Los conjuntos no permiten elementos duplicados.

"""

"""
# Listas

amigos = ['Juan', 'Pedro', 'Maria', 'Luis', 'Pedro', 'Juan', 'Ana', 'Carlos', "Juan"]
print(amigos[1])  # Acceder al segundo elemento (índice 1)

# Agregar elementos en listas
#amigos.append('Raul')
#amigos.insert(2, 'Sofia')  # Insertar en la posición 2

# Modificar elementos en listas
#amigos[0] = 'Matias'

# Eliminar elementos en listas
#amigos.remove('Pedro')
#del amigos[1]

print("Count:", amigos.count('Juan'))  # Contar la cantidad de veces que aparece 'Juan' en la lista)
print("Index:", amigos.index('Ana'))  # Obtener el índice de la primera aparición de 'Ana' en la lista)

print(amigos)
"""

"""
# Tuplas (inmutables)
amigos_tupla = ('Juan', 'Pedro', 'Maria', 'Luis', 'Pedro', 'Juan', 'Ana', 'Carlos', "Juan")

print(amigos_tupla[1])  # Acceder al segundo elemento (índice 1)

print("Count:", amigos_tupla.count('Juan'))  # Contar la cantidad de veces que aparece 'Juan' en la tupla)
print("Index:", amigos_tupla.index('Ana'))  # Obtener el índice de la primera aparición de 'Ana' en la tupla)

print(amigos_tupla)
"""

"""
# Diccionarios

paises = {
    'Argentina': 46,
    'Brasil': 213,
    'Colombia': 45,
    'Ecuador': 17,
    'Peru': 31,
    'Venezuela': 25,
    'Uruguay': 3.3,
    'Paraguay': 10,
    'Bolivia': 12,
    'Chile': 18
}

print(paises["Chile"])

# Mutabilidad

paises["Mexico"] = 100     # Agregar un nuevo país
paises["Argentina"] = 47   # Modificar el valor de un país existente
paises["Ecuador"] = 18     # Modificar el valor de un país existente

del paises["Venezuela"]

# Repeticion de elementos
print(paises)
"""

# Conjuntos

conj_1 = {1,2,3,4,5}
conj_2 = {4,5,6,7,8}

# Operaciones con conjuntos
print("Conjunto 1:", conj_1)
print("Conjunto 2:", conj_2)

# Unión
print("Unión:", conj_1 | conj_2) # conj_1.union(conj_2)

# Intersección
print("Intersección:", conj_1 & conj_2) # conj_1.intersection(conj_2)

# Diferencia
print("Diferencia:", conj_1 - conj_2) # conj_1.difference(conj_2)

# Diferencia simétrica
print("Diferencia simétrica:", conj_1 ^ conj_2) # conj_1.symmetric_difference(conj_2)

conj = {1,2,3,4,5,6,7,8,9,10}

# Mutabilidad

conj.add(11)
conj.remove(1)  # Arroja error si el elemento no existe
conj.discard(12)

print("Conjunto después de agregar 11:", conj)