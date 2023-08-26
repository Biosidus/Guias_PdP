#Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

#Variables
suma_acum=0;
num_a=0;
num_b=0;
num_c=0;
resultado=0.0;

#Proceso
print("Bienvenido a continuacion ingrese los numeros");

num_a=int(input("Ingrese el primer número:"));
num_b=int(input("Ingrese el segundo número:"));
num_c=int(input("Ingrese el tercer número:"));

suma_acum=num_a+num_b+num_c;

if suma_acum>10:
    resultado=suma_acum/2;
    print("El resultado final es: ",int(resultado));
else:
    resultado=suma_acum**3;
    print("El resultado final es: ",resultado);
