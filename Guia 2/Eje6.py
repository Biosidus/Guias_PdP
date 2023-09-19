#Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).

#Variables
num_ingresado=-1
cont=0
promedio=0.0

#Proceso

while num_ingresado !=0:
    print("Para continuar en el búcle ingrese un número distinto a 0.")
    num_ingresado=int(input("Ingrese el número:"))
    if num_ingresado !=0:
        cont+=1
        promedio=(promedio+num_ingresado)/cont
        print("El promedio actual es de: ",promedio)

print("El promedio final es:", promedio)
print("Gracias por usar el prgrama!")