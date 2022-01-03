#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.
# Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás

numero1= int(input("  Escriba un número: "))
digito1= numero1 // 10000
digito2= (numero1 // 1000 ) % 10
digito3= (numero1 // 100) % 10
digito4= (numero1 //10) % 10
digito5= (numero1 %10)
if digito1 == digito5 and digito2 == digito4:
     print(" El número " ,(numero1 ) ," es capicual")
else:
     print(" El número " ,(numero1 ) ,"  no es capicual")