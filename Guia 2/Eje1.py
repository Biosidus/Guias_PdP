"""Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas."""

"""Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas."""

# Variables
cant_ciclistas = 0
nombre = ""
mejor_nombre = ""
posicion = 0
mejor_tiempo = 0.0  # Inicializamos mejor_tiempo con un valor infinito para asegurarnos de que se actualice en la primera iteración
tiempo_prom = 0.0
tiempo_acum = 0.0

# Proceso
print("Bienvenido al sistema de clasificación de carga de tiempos")

while cant_ciclistas < 1:
    cant_ciclistas = int(input("¿Cuántos ciclistas hubo?: "))
    if cant_ciclistas < 1:
        print("La cantidad de ciclistas debe ser al menos 1. Inténtelo nuevamente.")

for i in range(cant_ciclistas):
    nombre = input("Ingrese el nombre del ciclista " + str(i + 1) + ": ")
    tiempo = float(input("Ingrese el tiempo de carrera para " + nombre + ": "))
    posicion = int(input("Ingrese la posición del participante: "))
    if posicion == 1:
        mejor_tiempo = tiempo
        mejor_nombre = nombre

    tiempo_acum += tiempo

tiempo_prom = tiempo_acum / cant_ciclistas

print("La carrera terminó con", mejor_nombre, "con el mejor tiempo de:", str(mejor_tiempo))
print("El promedio general de tiempo fue de:", tiempo_prom)
