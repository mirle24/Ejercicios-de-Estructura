#Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
#peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
#base en dicha secuencia se desea realizar un estudio a fin de conocer:
# Edad promedio de todas las personas en la muestra.
# Peso promedio de todas las personas en la muestra.
# Estatura promedio de todas las personas en la muestra.
# Cuántas personas hay con edad entre los 18 y 25 años.
# Cuántas personas son mayores a 36 años.


def ejercicio24(self):
            ed=[18,24,25,30,35,36]
            pe=[40,50,60,70,80]
            esta=[1.40,1.45,1.50,1.55,1.60,1.70]
            p_edad=(sum())/len()
            p_peso=(sum(pe))/len(pe)
            p_estatura=(sum(pe))/len(esta)
            c=0
            x=0
            while c<8:
                x+=(p_edad.count(18+c))
                c+=1  
            c=1
            mayores_36=0  
            while c<150:
                mayores_36+=(p_edad.count(36+c))
                c+=1
            c=0
            santos=0
            while c<36:
                santos=[i for i,x in enumerate(p_edad) if x>=18 and x<=35]
                c+=1
            suma=0
            c=0
            while c<len(santos):
                suma+=pe[santos[0+c]]
                c+=1
            print(santos)
            print("promedio edad :", p_edad)
            print("promedioa de peso : ", p_peso)
            print("promedio estatura : " ,p_estatura)
            print("un rango entrese 18 y 25 : ", x)
            print("personas mayores : " , mayores_36)
            print("promedio de pesos de todas las personas : " , suma/len(santos))