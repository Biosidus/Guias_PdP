# Variables
total_Ventas = 0
rango_Inferior = 0
rango_A = 0
rango_B = 0

# Proceso
print("Bienvenido al sistema de carga de ventas")

while True:
    ventas_Ingresadas = int(input("¿Cuántas ventas se ingresaran? (Ingrese un número negativo para salir): "))
    
    if ventas_Ingresadas < 0:
        print("Gracias por usar el programa!")
        break

    total_Ventas += 1

    # Cálculo de los rangos
    if 100 < ventas_Ingresadas < 300:
        rango_A += 1
    elif ventas_Ingresadas in (400, 500, 600):
        rango_B += 1
    elif ventas_Ingresadas < 50:
        rango_Inferior += 1

# Salidas
print(f"Se realizaron un total de {total_Ventas} ventas.")
print(f"Se realizaron un total de {rango_Inferior} ventas, con una cantidad de unidades menor a 50.")
print(f"Se realizaron un total de {rango_A} ventas, con una cantidad de unidades entre 100 y 300.")
print(f"Se realizaron un total de {rango_B} ventas, con una cantidad de unidades 400, 500 y 600.")

