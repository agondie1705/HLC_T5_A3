# Ejemplo:
# Entrada: hola mundo
# Salida: {'vocales': 4, 'consonantes': 5}
#p=input("dime las palabras deseadas")
p=("hola mundo")
p=p.split()
d={}
vocales=0
consonantes=0
for i in p:
    for j in i:
        if j in "aeiou":
            vocales+=1
        else:
            consonantes+=1
d["vocales"]=vocales
d["consonantes"]=consonantes
print(d)