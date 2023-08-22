#Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo.

#Variables
num_a=0.0;
num_b=0.0;
cuadrado_bin=0.0;

#Proceso
print("Ingrese los valores para sacar el cuadrado del binomio.");

num_a=float(input("Ingrese el valor a:"));
num_b=float(input("Ingrese el valor b:"));
cuadrado_bin=num_a*num_a+2*num_a*num_b+num_b*num_b;

"""print(f"({num_a} + {num_b})^2 = {num_a**2} + 2*{num_a}*{num_b} + {num_b**2}")"""
print("El cuadrado del binomio de ("+str(num_a)+"*"+str(num_b)+")^2 es igual a :"+str(cuadrado_bin));