#Menu de Opciones con secuencias. Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes operaciones: 
#a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados 
#b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales 
#c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares 
#d) Salir

import time
#Variables
n=0 #Se usa en el problema A y C
num=0
cuadradoNum=0
sumaDeCuadrados=0
contPar=0 #Se usa en el problema C
contImpar=0


#Proceso
#hacer los def's
def mostrar_menu():
    print("Menu de OPCIONES:")
    print("a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados")
    print("b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales")
    print("c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares")
    print("d) Salir")

#Def de la opcion A
def calculo_cuadrado():
    print("Bienvenido a la suma de cuadrados")
    n=int(input("Ingrese la cantidad de números a operar"))
    while n<0:
        n=int(input("Ingresó un número < a 0, vuelva a intentarlo:"))
    for n in range(1,n):
        num=int(input(f"Ingrese el {n}° a elevar al cuadrado:"))
        cuadradoNum=num**2
        sumaDeCuadrados+=cuadradoNum
        
#Def de la opcion B
def cantidad_vocales():
    texto = input("Ingrese un texto finalizado por un punto: ")
    palabras = texto.split()
    contador_vocales = 0
    for palabra in palabras:
        palabra = palabra.strip('.!?,;:"')
        if palabra[-1].lower() in 'aeiou':
            contador_vocales += 1

#Def de la opcion C
def par_impra():
        print("Bienvenido a la determinacion de series de números")
        while True:
            n=int(input("Ingrese el valor del número a sumar"))
            while not n.isdigit():
                print("Error")
                n=int(input("Ingrese el valor del número a sumar"))
            if n==0:
                break
            elif n%2 == 0:
                contPar+=1
            elif n%2 != 0:
                contImpar+=1
        if contPar > contImpar:
            print("Hay una mayor cantidad de números pares.")
        elif contPar < contImpar:
            print("Hay una mayor cantidad de números impares.")
        else:
            print("Hay la misma cantidad de números pares e impares.")
        
#MENU
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (a, b, c o d): ").lower()
    while not opcion.isalpha():
        print("Error")
        opcion = input("Ingrese una opción correcta (a, b, c o d): ").lower()

    #Punto A
    if opcion == 'a':
        sumaDeCuadrados=calculo_cuadrado()
        print(f"La suma de los cuadrados actual es: {sumaDeCuadrados}")

    #Punto B
    elif opcion == 'b':
            vocales=cantidad_vocales()
            print(f"La cantidad de palabras que terminan con vocales es: {vocales}")

    #Punto C
    elif opcion=='c':
        par_impra()

    #Punto D
    elif opcion == 'd':
        print("Saliendo del programa.")
        time.sleep(3)
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (a, b, c o d).")






