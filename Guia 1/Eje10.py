#Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto.

#Variables
num_a=0.0;
num_b=0.0;
resto=0.0;
cociente=0.0;
division=0.0;

#Proceso
num_a=float(input("Ingrese el primer número:"));
num_b=float(input("Ingrese el segundo número:"));

division=num_a/num_b;
cociente=num_a//num_b;
resto=num_a%num_b;

print("División: ",division);
print("Cociente: ",cociente);
print("Resto: ",resto);
