#Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras.

#Constante y Variables
LIBRAS= 2.2;
kilogramos=0.0;

#Proceso
kilogramos = float(input("Ingrese los kilogramos a convertir: "));
peso_conv = kilogramos * LIBRAS;

#Salida por pantallas
print("Usted convirtió", kilogramos, "Kgs a", peso_conv, "Libras");