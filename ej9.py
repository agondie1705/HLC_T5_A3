# Ejemplo:
# Entrada: {'Juan': 7, 'Ana': 9, 'Pedro': 6}
# Salida: Promedio: 7.33, Mejor estudiante: Ana con 9
p={"Juan":7,"Ana":9,"Pedro":6}
suma=0
mejor=0
mejor_nombre=""
for i in p:
    suma+=p[i]
    if p[i]>mejor:
        mejor=p[i]
        mejor_nombre=i
promedio=suma/len(p)
print("Promedio:",promedio,", Mejor estudiante:",mejor_nombre,"con",mejor)
