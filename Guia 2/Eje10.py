#Búsqueda de mayor Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de[0,100.000].
import random
#Variables
numero_aleatorio=0
maximo_num=0
total_Numeros=10000

#Proceso
for x in range(total_Numeros):
    numero_aleatorio=random.randint(0,100000)
    if maximo_num<numero_aleatorio:
        maximo_num=numero_aleatorio

#Salidas
print(f"El número máximo del programa es {maximo_num}")


