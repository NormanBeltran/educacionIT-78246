"""
Dada una lista de ausentes del mes, RH solicitad un diccionario, donde la clave sea el nombre del ausente y 
el valor sea la cantidad de veces que estuvo ausente.


ausentes = ["Juan", "Pedro", "Ana", "Maria", Ricardo", "Matias", "Pedro", "Ana", 
             "Maria", "Pedro", "Ana", "Maria", "Matias" ]

Ejemplo: {"Juan": 1, "Pedro": 3, "Ana": 3, "Maria": 3, "Ricardo": 1, "Matias": 2}

Resolver con un diccionario por comprension

dic = {clave: expresion  for ....    if  }

"""
"""
ausentes = ["Juan", "Pedro", "Ana", "Maria", "Ricardo", "Matias", "Pedro", "Ana", "Maria", "Pedro", "Ana", "Maria", "Matias"]
## Creación de un diccionario
diccionario = {}
## Recorrer cada ausente
for nombre in ausentes:
    if nombre in diccionario:
        ## Si ya existe, le incremento su contador de ausencias
        diccionario[nombre] += 1
    else:
        ## Si no existe, lo agrego con contador en 1
        diccionario[nombre] = 1
print("Listado de ausencias:", diccionario)
"""

# Grupo con Martina, Gaston y Joshua:
# Resolver por un diccionario por compresion para contar los ausentes
ausentes = ["Juan", "Pedro", "Ana", "Maria", "Ricardo", "Matias", "Pedro", "Ana", "Maria", "Pedro", "Ana", "Maria", "Matias"]
dicc = {nombre: ausentes.count(nombre) for nombre in set(ausentes)}
print(dicc)
# Fin grupo con Martina, Gaston y Joshua