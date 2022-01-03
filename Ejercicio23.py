#Dado un número N determinar si es un número primo.
#Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo. 

n= int(input("Ingrese un numero: "))
def evaluar_primo(n):
    contador = 0
    resultado= True
    for i in range(1, n+1):
        if (n%i==0):
            contador+=1
        if (contador >2):
                resultado=False
                break
    return resultado
if(evaluar_primo(n)==True):
            print("El numero es primo")
else:
             print("El numero no es primo")