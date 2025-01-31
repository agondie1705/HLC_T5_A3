# Ejemplo:
# Entrada: gato perro elefante
# Salida: {'gato': 4, 'perro': 5, 'elefante': 8}
#p=input("dime las palabras deseadas")
p=("gato perro elefante")
p=p.split()
d={}
for i in p:
    d[i]=len(i)
print(d)