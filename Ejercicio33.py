#Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la
#suma de los lados del polígono)

from Ejercicio31 import Ejercicios


lados = int(input("Ingrese el lado del polígono: "))
perimetro = Ejercicios()
resultado = perimetro.PerPenta(lados)
print("El perímetro del pentágono es: {}".format(resultado))

def PerPenta(self,lados):
        resultado = lados*5
        return resultado