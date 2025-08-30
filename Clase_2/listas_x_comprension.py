"""
mul7 = []

for i in range(1, 101):
    mul7.append(i * 7)

print(mul7)    
"""

mul7 = [i * 7  for i in range(1, 101)] # Listas por comprension

mul7y5 = [i * 7  for i in range(1, 101) if (i*7) % 5 == 0]

print(mul7y5)