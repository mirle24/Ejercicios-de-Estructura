    # #Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
    #resultado su equivalente en segundos.
    
horas= int(input("Escriba la cantidad de horas: " ))
minutos= int(input("Escriba la cantidad de minutos: " ))
if minutos <=59:
     h1= horas * 60
     m1= minutos * 60
     suma= h1 + m1
     segundos= suma * 60
     print(" El resultado equivalente en segundos es: ",(segundos))
else:
     print("Escriba el valor de los minutos: ")