# Ejemplo:
# Salida: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def diccionario():
    d={n:n**2 for n in range(1,6)}
    return d

print(diccionario())
   