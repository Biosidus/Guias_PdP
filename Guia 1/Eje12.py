#Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.

#Variables
sueldo=0.0;
ahorrado=0.0;
PORC_DE_AHORRO=0.1;

#Proceso
print("Bienvenido al calculador de ahorro mensual");

sueldo=float(input("Ingrese su sueldo de Enero:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Febrero:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Marzo:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Abril:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Mayo:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Junio:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Julio:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Agosto:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Septiembre:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Octubre:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Noviembre:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

sueldo=float(input("Ingrese su sueldo de Diciembre:"));
ahorrado=ahorrado+(sueldo*PORC_DE_AHORRO);

print("En total a ahorrado: $",ahorrado);