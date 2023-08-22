#Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.

#Variables
numero=0;
resultado=0;

#Proceso
numero=int(input("ingrese el número:"));
for i in range(1,11):
    resultado=numero*i;
    print(numero,"x",i,"=",resultado);
