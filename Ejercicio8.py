#Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. 
# El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.

print ("Ingresa un numero")
def binarizar(decimal):
 binario = ''
 while decimal // 2 != 0:
  binario = str(decimal % 2) + binario
  decimal = decimal // 2 
 return str(decimal) + binario

def bits(decimal):
    result = 0
    if decimal:
     result ^=  decimal and 1
     decimal  >>= 1
    print(" Es:", result, "por lo tanto es impar")
    print(" Es:", result, " por lo tanto es par")
    return result


