#Dado un número, determine si es capicúa.
#Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás


numero= int(input("INGRESE UN NUMERO POSITIVO "))
if numero  >=0:
    if str(numero)==str(numero)[ :: -1]:
        print("%i es capicua" % numero)
    else:
        print("%i no es capicua" % numero)
else:
    print("El numero debe ser positivo") 
