#Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
#   a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
#   b) Determinar en qué mes recibió el sueldo más bajo del período.
#   c) Informar el sueldo promedio del semestre.

#Variables
sueldo=0.0
sueldo_prom=0.0
sueldo_acum=0.0
aguinaldo=0.0
mes=""
num_mes=0
mayor_sueldo=0.0
menor_sueldo=0.0

#Proceso

for i in range(6):
    print("A continuación deberá ingresar el sueldo del mes N°",i+1,":")
    sueldo=float(input("Ingrese el sueldo:"))
    if mayor_sueldo < sueldo:
        mayor_sueldo = sueldo
    if menor_sueldo > sueldo:
        menor_sueldo = sueldo
        num_mes=i
    sueldo_acum+=sueldo

sueldo_prom=sueldo_acum/6
aguinaldo=mayor_sueldo/2

if num_mes == 0:
    mes = "Enero"
elif num_mes == 1:
    mes = "Febrero"
elif num_mes == 2:
    mes = "Marzo"
elif num_mes == 3:
    mes = "Abril"
elif num_mes == 4:
    mes = "Mayo"
elif num_mes == 5:
    mes = "Junio"

print("\nResultados:")
print("a) El aguinaldo es:", aguinaldo)
print("b) El sueldo más bajo se recibió en el mes de ",mes)
print("c) El sueldo promedio del semestre es:", sueldo_prom)