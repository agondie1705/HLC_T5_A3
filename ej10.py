# Ejemplo:
# Entrada: [1, 2, 3, 4, 5, 6]
# Salida: [1, 3, 5]
#p=input("dime los numeros")
p=[1,2,3,4,5,6]
for i in p:
    if i%2 == 0:
        p.remove(i)
print(p)