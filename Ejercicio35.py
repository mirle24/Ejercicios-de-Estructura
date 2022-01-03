
#Escriba una acción (MillasAKilometros) que convierta una distancia en millas a
#kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre
#de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre
#ellas y debe retornar la distancia entre las ciudades en kilómetros.
#Desarrolle además una acción principal en donde utilice a la acción
#MillasAKilometros para convertir e informar la distancia en kilómetros entre 4 pares
#de ciudades suministradas por el usuario.
#Entrada:
#Cuidad A
#Ciudad B
#332
#Salida:
#Entre la Ciudad A y la Ciudad B hay 534.30 Km
from Ejercicio31 import Ejercicios

Calculo = Ejercicios()
diccionario_palabras = ["primer","segundo","tercer","cuarto"]
contador = 0
while contador < 5:
            ciudad_o = input("Ingrese el {} par de Ciudad:\n1. ".format(diccionario_palabras[contador]))
            ciudad_d = input("2. ")
            distancia = int(input("Ingrese la distancia entre la ciudad {} y {}: ".format(ciudad_o,ciudad_d)))
            convercion = Calculo.Calmikm(distancia)
            print("Entre la ciudad de {} y la de {} hay {} Km".format(ciudad_o,ciudad_d,round(convercion,2)))
            contador+=1

def Calmikm(self,c):    
    milla_kilometros = 1.60935
    respuesta = c * milla_kilometros
    return respuesta
