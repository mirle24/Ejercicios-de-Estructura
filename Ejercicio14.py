# Para un valor entero positivo que representa una cantidad en segundos, indicar
# su equivalente en minutos, horas y días.
            
segundos= int(input(" Escriba la cantidad de segundos "))
dias = segundos // ( 24 * 60 * 60 )
segundos = segundos % (24 * 60 *60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos= segundos // 60
segundos= segundos // 60
print("Días: {} = Horas {} = Minutos {}".format(dias,horas,minutos))