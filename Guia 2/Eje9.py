#
import random

#Variables
suma=0
total_Numeros=1000
promedio=0.0

#Proceso
for x in range(total_Numeros):
    numero_aleatorio=random.randint(0,100000)
    suma+=numero_aleatorio
#Promedio
promedio= suma/total_Numeros

# Imprimir el resultado
print(f"El promedio de los 1000 números aleatorios es: {promedio}")
