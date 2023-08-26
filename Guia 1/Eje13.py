#Crear un conversor de pies y pulgadas a centímetros.

#Variables
CM_PIE=30.4;
CM_PULGADA=2.54;
cant_a_conv=0.0;
cm_convertidos=0.0;
opcion=0;

#Proceso
print("Bienvenido al conversor de longitud");

print("Tiene 2 opciones de conversión:");
print("1. Convertir PIE a Centímetros");
print("2. Convertir PULGADAS a Centímetros");
opcion = int(input("Seleccione una opción (1 o 2): "));

if opcion==1:
    cant_a_conv=float(input("Ingrese la cantidad de PIES a convertir:"));
    cm_convertidos=cant_a_conv*CM_PIE;
if opcion==2:
    cant_a_conv=float(input("Ingrese la cantidad de Pulgadas a convertir:"));
    cm_convertidos=cant_a_conv*CM_PULGADA;


if opcion!=1 and opcion!=2:
    print("No ingreso una opción válida");    

