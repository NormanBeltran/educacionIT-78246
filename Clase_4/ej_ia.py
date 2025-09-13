import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de pandas
try:
    df = pd.read_csv("ventas.csv")
except FileNotFoundError:
    print("Error: El archivo 'ventas.csv' no se encuentra.")
    exit()

# Agrupar los datos por juego y calcular la suma del importe
ventas_por_juego = df.groupby("nombre_de_juego")["importe_total"].sum()

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))  # Ajustar el tamaño del gráfico
ventas_por_juego.plot(kind="bar")
plt.title("Importe Total de Ventas por Juego")
plt.xlabel("Juego")
plt.ylabel("Importe Total")
plt.xticks(rotation=45, ha="right")  # Rotar las etiquetas del eje x para mejor legibilidad
plt.tight_layout()  # Ajustar el diseño para evitar que las etiquetas se superpongan
plt.show()