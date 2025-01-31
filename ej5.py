# Ejemplo:
# Entrada: hola mundo hola
# Salida: {'hola': 2, 'mundo': 1}
def frecuencia_palabras(d):
    ps = d.split()
    f = {}

    for p in ps:
        if p in f:
            f[p] += 1
        else:
            f[p] = 1

    return f
print(frecuencia_palabras('hola mundo hola'))