#Secuencia numérica. Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar
#a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
#b) Determinar la cantidad de números que son el cuadrado del número anterior
#c) Determinar la posición del mayor elemento impar de la secuencia

#Variables
cuadrados_del_anterior = 0
contDivTres=0
mayor_impar = None
posicion_mayor_impar = 0
posicion_actual = 1

#Proceso
while True:
    num=int(input("Ingrese un número(0 si quiere salir):"))
    while not num.isdigit():
        print("Error")
        num=int(input("Ingrese un número, no una letra:"))

    if num==0:
        break
    elif num%3 ==0:
        contDivTres+=1
    elif  posicion_actual > 1 and num == anterior ** 2:
        cuadrados_del_anterior += 1
    elif num % 2 != 0:
        if mayor_impar is None or num > mayor_impar:
            mayor_impar = num
            posicion_mayor_impar = posicion_actual
    anterior = num
    posicion_actual += 1


total_numeros = posicion_actual - 1
if total_numeros > 0:
    porcDivTres = (contDivTres / total_numeros) * 100
else:
    porcDivTres = 0

# Mostrar los resultados
print(f"Porcentaje de números divisibles por 3 en la secuencia: {porcDivTres:.2f}%")
print(f"Cantidad de números que son cuadrados del número anterior: {cuadrados_del_anterior}")
if mayor_impar is not None:
    print(f"Mayor elemento impar en la secuencia: {mayor_impar}")
    print(f"Posición del mayor elemento impar en la secuencia: {posicion_mayor_impar}")
else:
    print("No se encontraron números impares en la secuencia.")
