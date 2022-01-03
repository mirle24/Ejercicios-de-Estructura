# Dado un (1) número, imprimir 0 si es par y 1 si es impar

print ("Ingresa un numero")
numero = int(input())
resto = numero % 2
resultado= resto
if resto ==0:
    print(" Es:", resultado, "por lo tanto es par")
else:
    print(" Es:", resultado, " por lo tanto es impar")