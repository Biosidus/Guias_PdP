#Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.

#Variables
TURNO_DIURNO=35.5;
TURNO_NOCTURNO=40.6;
opcion=0;
cant_horas=0.0;
salario=0.0;

#Proceso
print("Bienvenido al calculador de pagos");

print("Tiene 2 opciones de turnos:");
print("1. Turno DIURNO");
print("2. Turno NOCTURNO");
opcion = int(input("Seleccione una opción (1 o 2): "));
cant_horas = float(input("Ingrese la cantidad de horas a facturar:"));

if opcion == 1:
    salario=cant_horas*TURNO_DIURNO;
    print("Se debe abonar al operario $",salario);

if opcion == 2:
    salario=cant_horas*TURNO_NOCTURNO;
    print("Se debe abonar al operario $",salario);

if opcion!=1 and opcion!=2:
    print("No ingreso una opción válida");
