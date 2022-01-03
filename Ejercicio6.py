#Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.

from math import sqrt

AB = float(input("Introducir el Valor de AB: "))
BC = float(input("Introducir el Valor de BC: "))

hipotenusa = sqrt((AB**2) + (BC**2))

print("La Hipotenusa es: ", hipotenusa)