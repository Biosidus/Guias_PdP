#Menores y promedio Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:
#Determinar el menor de los numeros genera dos en forma aleatoria.Calcular el valor promedio de los números menores a 10.000.
import random

#Variables
numero_Min=0
numero_Aleatorio=0
promedio=0.0
cont_promedio=0
suma=0
total_Numeros=5000

#Proceso
for x in range(total_Numeros):
    numero_Aleatorio=random.randint(0,100000)
    if numero_Min > numero_Aleatorio:
        numero_Min=numero_Aleatorio
    if numero_Aleatorio < 10000:
        suma+=numero_Aleatorio
        cont_promedio+=1
        
promedio=suma/cont_promedio
print(f"El menor número de los {total_Numeros} generados es {numero_Min}.")
print(f"El promedio de los {cont_promedio} números menores a 10.000 es {promedio}.")