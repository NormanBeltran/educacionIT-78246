def orden(sublista):
    mul =  1
    for x in sublista:
        mul *= x
    return mul

lista = [88,44,33,99,100,1,5]

lista2 = [2.34, "Ana", 5, "Pedro"] # No es valido su ordenamiento por ser diferentes tipos de datos

print(sorted(lista)) # Ordena de menor a mayor

lst = ["a", "aba", "asd", "sdsds", "asdadkjfh", "asasa", "b"]

print(sorted(lst, key=len)) # Ordena por la longitud de los strings

matriz = [[20,1], [1,2,3,4,5,6,7], [10,2,2]]

print(sorted(matriz, key=orden)) # Ordena por la suma de los elementos de cada sublista