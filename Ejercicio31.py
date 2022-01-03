#Construya una función que solicite edades al usuario y determine el promedio de
#las edades mayores a 18 años. El usuario indicará cuando desea dejar de
#suministrar datos de entrada. En la Acción Principal se informará el promedio calculado.

bandera = input("Desea ingresar datos? sí (y) o no (n) ")

def Ejercicios():
    promedio = Ejercicios()
    return promedio

if bandera.lower() == "y":
            print("Si desea salir, ingrese una 'x'")
            promedio = Ejercicios()
            pro_final = promedio.SoliUser(bandera)
            if pro_final != 0:
                print("El promedio de las edades mayores a 18 años es: ",pro_final)
            elif pro_final == 0:
                print("No hay edades mayores a 18 años.")
            else:
                print("Dado que no ha dado valores, no hay promedio.")
else:
            print("Ha salido!")


def SoliUser(self,bandera):
        lista = []

        while bandera.lower() != "x":
            edad = input("Ingrese edad: ")
            if edad == "x":
                bandera = "x"
            elif edad != "x" and int(edad) <= 0:
                print("Ingrese un valor acorde por favor, o 'x' para dejar de ingrear datos")
            elif int(edad) > 18:
                lista.append(int(edad))


        if len(lista) > 0:
            promedio = (sum(lista))/len(lista)
        else:
            promedio = 0
        return promedio