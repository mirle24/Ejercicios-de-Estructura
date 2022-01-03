# Dado un (1) número binario de cuatro (4) dígitos imprimir su valor

def BinDec(n):
    S=0
    i=0
    print("El binario de :", n, end= " ")
    while(n>=1):
        d=n%10;
        n=int(n/10);
        S=S+d*pow(2,i);
        i=i+1
    print("Corresponde al número: ", S)
numero = int(input('Ingrese 4 digitos: '))
print (BinDec(numero))
        
        

    
    
    
    

