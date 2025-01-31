#Crea una función que reciba una lista de números y calcule la suma y el promedio de los números.
# Ejemplo:
# Entrada: 10, 20, 30
# Salida: Suma: 60, Promedio: 20.0
def suma_promedio():
    numeros=[1,2,3,4,5]
    suma=0
    for i in numeros:
        suma+=i
    promedio=suma/len(numeros)
    print(f'Suma: {suma}, Promedio: {promedio}')
suma_promedio()