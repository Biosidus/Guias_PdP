#Comisión de vendedores. Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores, para ello les solicita un sistemita que le permita calcular dichos montos. Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores(1 a 4).Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta(el proceso termina cuando se ingrese una categoría igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:
#Categoría1:cobra una comisión de 10%
#Categoría2: cobra una comisión de 25%
#Categoría3:cobra una comisión de 30%
#Categoría4:cobra una comisión de 40%
#Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedor es que en el la empresa junto con el total general.

#Variables
totalVenta=0.0
total_General=0.0
cantComision=0.0
categoriaVendedor=""
acumCatUno=0.0
acumCatDos=0.0
acumCatTres=0.0
acumCatCuatro=0.0

#Porcentaje de las categorias
CAT_UNO=0.1
CAT_DOS=0.25
CAT_TRES=0.3
CAT_CUATRO=0.4


#Proceso

print("Bienvenido al calculador de Comisiones")

while True:
    print("Puede ingresar las siguientes categorías: 1, 2, 3 y 4, si desea salir presione 0")
    categoriaVendedor=int(input("Ingrese la categoria del vendedor:"))

    while not categoriaVendedor.isdigit():
        print("Pruebe ingresar las siguientes categorías: 1, 2, 3, 4 o 0 para salir.")
        categoriaVendedor=int(input("Ingrese una categoría válida:"))
    
    print("Ahora ingresará el valor de la venta, recuerde que debe ser positivo.")
    totalVenta=float(input("Ingrese el total de la venta:"))
    while  totalVenta < 0:
        print("Error, ingresó un número negativo.")
        totalVenta=float(input("Ingrese un valor positivo:"))
    if categoriaVendedor == 1:
        cantComision=totalVenta*CAT_UNO
        acumCatUno+=cantComision
    elif categoriaVendedor == 2:
        cantComision=totalVenta*CAT_DOS
        acumCatDos+=cantComision
    elif categoriaVendedor == 3:
        cantComision=totalVenta*CAT_TRES
        acumCatTres+=cantComision
    elif categoriaVendedor == 4:
        cantComision=totalVenta*CAT_CUATRO
        acumCatCuatro+=cantComision
    elif categoriaVendedor == 0:
        break
    
    #Reinicio de variables
    totalVenta=0.0
    categoriaVendedor=0

total_General=acumCatUno+acumCatDos+acumCatTres+acumCatCuatro
print(f"El total a pagar de las comisiones a pagar de la Categoría 1 es: ${acumCatUno}")
print(f"El total a pagar de las comisiones a pagar de la Categoría 2 es: ${acumCatDos}")
print(f"El total a pagar de las comisiones a pagar de la Categoría 3 es: ${acumCatTres}")
print(f"El total a pagar de las comisiones a pagar de la Categoría 4 es: ${acumCatCuatro}")
print(f"El total general a pagar es de: ${total_General}")
