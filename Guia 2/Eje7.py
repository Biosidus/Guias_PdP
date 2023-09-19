#Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines.
#Por cada función se conoce:cantidad de espectadoretermina cuando la cantidad de espectads y descuento(S/N).
#La carga ores sea igual a 0(cero).
#El programa deberá:Calcular la recaudación total del complejo,considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.
#Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones

#Variables
cant_espectadores=-1
ENTRADA_DESCUENTO=50
ENTRADA_NORMAL=75
recaudacion_total=0.0
recaudacion_actual=0.0
acum_desc=0.0
cont_func_desc=0
cont_func=0
continuar=0
opc_desc=""

#Proceso

while cant_espectadores !=0:
    while cant_espectadores < 0:
        cant_espectadores=int(input("Ingrese la cantidad de espectadores:"))
        if cant_espectadores < 0:
            print("No ingresó una cantidad válida, vuelva a intentarlo.")
        if cant_espectadores==0:
            break
    while opc_desc !="S" and opc_desc !="N":
        opc_desc=str(input("¿Es un día de descuento? (S/N)").upper())
        if opc_desc !="S" and opc_desc !="N":
            print("No, ingresó una opción válida,")
    if opc_desc == "S":
        recaudacion_actual=ENTRADA_DESCUENTO*cant_espectadores
        cont_func_desc+=1
    else:
        recaudacion_actual=ENTRADA_NORMAL*cant_espectadores
    cont_func+=1
    recaudacion_total+=recaudacion_actual
#Reinicio de variables
    if cant_espectadores !=0:
        cant_espectadores=-1
    else:
        cant_espectadores=0
    opc_desc=""





print("La recaudación total del complejo es de $", recaudacion_total)
print("Cantidad de funciones con descuento:", cont_func_desc)
print("Porcentaje de funciones con descuento sobre el total:", (cont_func_desc / cont_func) * 100, "%")

print("afuera")
