#Conversión de medidas. Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas pulgadas cenơmetros metros Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro = 1000

#Variables y constantes
pies=0;
PULGADAS=12;
medida_pulgadas=0.0;
YARDA=0.3;
medida_yardas=0.0;
CENTIMETROS=PULGADAS*2.54;
medida_centimetro=0.0;
METROS=CENTIMETROS/100;
medida_metros=0.0;

#Proceso
pies=float(input("ingrese la medida en pies a convertir:"));
medida_yardas=pies*YARDA;
medida_centimetro=pies*CENTIMETROS;
medida_pulgadas=pies*PULGADAS;
medida_metros=pies*METROS;

print("El equivalente en yardas: ",medida_yardas);
print("El equivalente en centímetros: ",medida_centimetro);
print("El equivalente en pulgadas: ",medida_pulgadas);
print("El equivalente en metros: ",medida_metros);