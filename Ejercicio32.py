#Construya una función “Eleva” Que reciba como parámetros una base y un
#exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese su exponente: "))
resultado = "Ejercicios"()
calculo = resultado.Eleva(base,exponente)
print("El resultado de elevar {} a la {} es {}".format(base,exponente,calculo))

def Eleva(self,base,exponente):
    calculo = base**exponente
    return calculo