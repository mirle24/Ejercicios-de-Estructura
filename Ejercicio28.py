#Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla del 1 hasta la del 10.

numero = int (input("Digite un nùmero entero: "))

for i in range(1,11):
    print(f"{numero} x {i} = {i * numero}  ")
    {}