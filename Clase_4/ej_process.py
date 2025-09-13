import subprocess

p = subprocess.run(["python", "-W"], shell=True, capture_output=True, text=True)


input("Presione una tecla para continuar...")

print("Estandar Output",p.stdout) #  captura la salida estandar
print("Estandar Error",p.stderr) #  captura la salida de error
print("Codigo de Retorno",p.returncode) #  captura el codigo de retorno

if p.returncode != 0:
    print("Error en la ejecucion")