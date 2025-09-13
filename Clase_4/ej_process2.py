import subprocess as sp
p = sp.run(["ipconfig", "/all"], capture_output=True, text=True, encoding="cp850")

print(p.stdout)