#Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el numero hexadecimal.
import random

#Variables
n = 101

#Proceso
for _ in range(n):
    numero_decimal = random.randint(5000, 450000)
    numero_hexadecimal = hex(numero_decimal)
    print(f"Número decimal: {numero_decimal}, Número hexadecimal: {numero_hexadecimal}")