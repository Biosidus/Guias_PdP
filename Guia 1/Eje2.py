#Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.

#Variable y Constantes
nombre="";

#Proceso
print("Bienvenido");
print("Para saber si su nombre es par o impar");
nombre=str(input("Ingrese su nombre:"));

cant_letras=len(nombre);

#Salida por pantalla
if(cant_letras%2==0):
    print("Su nombre es par y tiene "+str(cant_letras)+" letras.");
else:
    print("Su nombre es impar y tiene "+str(cant_letras)+" letras.");
