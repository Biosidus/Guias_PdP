#Números pares e impares Se pide desarrollar un programa que permita leer una serie de números. La nalización de carga de datos se presenta cuando el usuario ingrese un número negativo. Los requerimientos funcionales del programa son: La sumatoria de solo los números que estén comprendidos entre 50 y 100. Cantidad de valores pares ingresados. Cantidad de valores impares ingresados. Informar si en la carga de números se ingreso al menos un número 0. Informar si la serie contiene solo números pares e impares alternados.

#Variables
suma_entre_50_y_100 = 0
cantidad_pares = 0
cantidad_impares = 0
hay_numero_cero = False
alternados = True
ultimo_numero = None

# Proceso
while True:
    numero = int(input("Ingrese un número (ingrese un número negativo para finalizar): "))
    
    if numero < 0:
        break
    
    if numero == 0:
        hay_numero_cero = True
    
    if 50 <= numero <= 100:
        suma_entre_50_y_100 += numero
    
    if numero % 2 == 0:
        cantidad_pares += 1
        if ultimo_numero is not None and ultimo_numero % 2 == 0:
            alternados = False
    else:
        cantidad_impares += 1
        if ultimo_numero is not None and ultimo_numero % 2 != 0:
            alternados = False
    
    ultimo_numero = numero

# Salidas
print(f"La sumatoria de los números entre 50 y 100 es: {suma_entre_50_y_100}")
print(f"Cantidad de números pares ingresados: {cantidad_pares}")
print(f"Cantidad de números impares ingresados: {cantidad_impares}")

if hay_numero_cero:
    print("Se ingresó al menos un número 0.")
else:
    print("No se ingresó ningún número 0.")

if alternados:
    print("La serie contiene solo números pares e impares alternados.")
else:
    print("La serie no contiene solo números pares e impares alternados.")
