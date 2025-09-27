import tkinter as tk
from tkinter import ttk

#______________________________________ Funciones

def calcular():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    resultado = num1 + num2
    etiqueta_resultado.config(text=f"{resultado}")

#______________________________________Programa


ventana = tk.Tk()
ventana.title("Mi primera ventana") 
ventana.config(width=400, height=300)

etiqueta1 = ttk.Label(ventana, text="Calculadora (SUMA)")
etiqueta1.place(x=150, y=10)


etiqueta2 = ttk.Label(ventana, text="Número 1:")
etiqueta2.place(x=50, y=50)

entrada1 = ttk.Entry(ventana)
entrada1.place(x=150, y=50)

etiqueta3 = ttk.Label(ventana, text="Número 2:")
etiqueta3.place(x=50, y=90)

entrada2 = ttk.Entry(ventana)
entrada2.place(x=150, y=90)

boton1 = ttk.Button(ventana, text="Calcular", command=calcular)
boton1.place(x=150, y=130)

etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.place(x=150, y=190)
etiqueta_resultado.config(font=("Arial", 20), foreground="yellow", background="black", width=10)

ventana.mainloop()