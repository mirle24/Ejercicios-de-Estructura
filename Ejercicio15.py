 # # Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
    # mayor? y ¿cuál es el segundo mayor
n1= float(input("Ingrese el primer número:  "))
n2=float(input("Ingrese el segundo número:  "))
n3= float(input("Ingrese el tercer número:  "))
if n2 < n1 > n3:
      print(" El número mayor es el primer número.:" ,n1)
elif n1 < n2 > n3 :
      print(" El numero mayor es el segundo número.:",n2)
elif n1 < n3 > n2 :
      print("El número mayor es el tercer número.:",n3)
else:
      print( " TODOS LOS NUMEROS SON IGUALES. ")