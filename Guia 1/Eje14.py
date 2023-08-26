#Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:

#Variables
nombre="";
apellido="";
dominio="";
primeras_letras="";
direccion_correo="";

#Proceso
print("Bienvenido al generador de direcciones de correo");

nombre = str(input("Ingrese su nombre: "));
apellido = str(input("Ingrese su apellido: "));
dominio = str(input("Ingrese el dominio: "));

primeras_letras = nombre[0].lower() + apellido[0].lower();

if nombre[0].lower() == apellido[0].lower():
    direccion_correo=nombre,".",apellido,dominio;
else:
    direccion_correo=primeras_letras[0],apellido,dominio;

print("La dirección de correo es:", direccion_correo);
