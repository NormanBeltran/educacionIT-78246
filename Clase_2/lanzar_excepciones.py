def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Se requieren dos numeros.")
    return a + b

try:
    sumar(2, "A")
except Exception as e:
    print("Error:", e, e.__class__)