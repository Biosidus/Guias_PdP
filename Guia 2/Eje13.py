#Desarrollar un programa que permita procesar los datos del último censo de un apequeña población.Por cada habitantes e ingresa:sexo(M/F)y edad. La carga de datos analiza al ingresar cualquier otro valor para sexo. El programa debe informar:Aqué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.

# Variables
edad = 0
sexo = ""
cont_femenino = 0
cont_masculino = 0
mayor_cantidad_sexo = ""
cont_mujeres_escolar=0
# Proceso

while True:
    sexo = input("Ingrese el sexo del censado (f/m) o 'q' para finalizar:").lower()

    if sexo == 'q':
        break

    while sexo not in ("f", "m"):
        print("No ingresaste una opción válida.")
        sexo = input("Ingrese el sexo del censado (f/m) o 'q' para finalizar:").lower()

    edad = int(input("Ingrese la edad del censado:"))

    if sexo == 'f':
        cont_femenino += 1
        if 4 <= edad <= 18:
            cont_mujeres_escolar += 1
    elif sexo == 'm' and edad > 80:
        masculino_mayor_80 = True

if cont_femenino > cont_masculino:
    mayor_cantidad_sexo = "Femenino"
elif cont_femenino < cont_masculino:
    mayor_cantidad_sexo = "Masculino"
else:
    mayor_cantidad_sexo = "Igual cantidad de Femenino y Masculino"

print(f"El sexo con la mayor cantidad de habitantes es: {mayor_cantidad_sexo}")
print(f"Cantidad de mujeres en edad escolar: {cont_mujeres_escolar}")

if masculino_mayor_80:
    print("Hay al menos un varón que supera los 80 años de edad.")
else:
    print("No hay varones que superen los 80 años de edad.")
