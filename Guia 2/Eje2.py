#Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente.


#Variables
num_1=0
num_2=0

#Proceso

print("A continuación deberá ingresar los 2 números:");
num_1=int(input("Ingrese el primer número: "))
num_2=int(input("Ingrese el segundo número: "))

print("Números impares en forma ascendente:")
for i in range(num_1, num_2 + 1):
    if i % 2 != 0:
        print(i, end=" ")

print("\nNúmeros impares en forma descendente:")
for i in range(num_2, num_1 - 1, -1):
    if i % 2 != 0:
        print(i, end=" ")