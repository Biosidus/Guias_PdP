#Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.

#Variables
precio_dol=0.0;
cantidad=0.0;
opcion=0;
conversion=0.0;

#Proceso
print("Bienvenido al conversor de moneda");
precio_dol=float(input("Ingrése el valor del dólar:"));
print("Tiene 2 opciones de conversión:");
print("1. Convertir de dólares a pesos");
print("2. Convertir de pesos a dólares");
opcion = int(input("Seleccione una opción (1 o 2): "));


if opcion==1:
    cantidad=float(input("Ingrese la cantidad de pesos a convertir en dólares:"));
    conversion=cantidad/precio_dol;
if opcion==2:
    cantidad=float(input("Ingrese la cantidad de dólares a convertir en pesos:"));
    conversion=cantidad*precio_dol;
if opcion!=1 and opcion!=2:
    print("No ingreso una opción válida");    

print("Usted acaba de comprar $",conversion);