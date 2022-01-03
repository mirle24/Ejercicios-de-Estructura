# Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
# decenas, centenas y unidades de mil.
#Entrada:
#1234
#Salida:
#Unidades: 4
#Decenas: 3
#Centenas: 2
#Unidades de mil: 1

num = int(input("Ingresa 4 dígitos:  \n"))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
n= str(num)
print("Separando numero.......... ".format(num))
print("Unidades:{}". format(u))
print("Decenas:{}". format(d))
print("Centenas:{}". format(c))  
print("Unidades de mil:{}". format(m)) 

