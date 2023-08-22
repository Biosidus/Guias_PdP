#Área de un triángulo. Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.

#Variables
base=0.0;
area=0.0;
altura=0.0;

#Proceso
print("Bienvenido");
base=float(input("Ingrese el valor de la base:"));

altura=base*base;
area=(base*altura)/2;

print("El área del triángulo es de: "+str(area)+"U cuadradas.");