# Ejemplo:
# Entrada: 12
# Salida: [1, 2, 3, 4, 6, 12]
#n=int(input("dime el numero"))
n=12
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)