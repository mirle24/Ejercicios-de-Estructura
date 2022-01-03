#Construya un programa que dado un valor entero N, haga el cálculo de la función
#factorial utilizando estructuras iterativas.

def factorial(n):
    if (n==0):
        return 1
    else:
        return n* factorial(n-1)
n= int(input("Ingrese un numero : "))
print("El factorial de : " + str(n) + ": es :" + str(factorial(n))) 