#Escriba un programa que transforme todas las letras de una palabra en mayúsculas, minúsculas y la primera con minúsculas(capitalización).

#Variables
palabra="";
Mayus="";
minus="";
capitalizada="";

#Proceso
print("Bienvenido, a continuacion podra convertir las palabras:");
palabra=str(input("Ingrese la palabra a modificar:"));

    #Mayusculas
Mayus=palabra.upper();
print("Su palabra en Mayúsculas: "+Mayus);

    #Minusculas
minus=palabra.lower();
print("Su palabra en Minúsculas: "+minus);

    #Capitalizada(con la primera letra mayúscula)
capitalizada=palabra.capitalize();
print("Su palabra capitalizada: "+capitalizada);