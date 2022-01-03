#Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que la serie termina al leer un 0.
  
contador=0
suma=0
numero=1
while numero !=0:
             numero =int(input("DIGITE UN NUMERO ENTERO POSITIVO (0 PARA FINALIZAR....) \n"  )) 
             
             suma += numero
             contador +=1
if contador ==0:
             print("NO DIGITO NINGUN NUMERO ")
else:
             promedio= suma/contador
             print ("EL PROMEDIO DE LOS {} NUMEROS ES IGUAL A : ".format(contador, promedio )      )            

