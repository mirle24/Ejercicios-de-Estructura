# Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho número.

mes=int(input("INGRESE UN VALOR DEL 1 AL 12 \n "))
if mes==1:
   print(" Enero ")
elif mes ==2:
   print(" Febrero ")
elif mes ==3:
    print("Marzo")
elif mes ==4:
    print("Abril")
elif mes ==5:
    print("Mayo")
elif mes ==6:
    print("Junio")
elif mes ==7:
    print("Julio")
elif mes ==8:
    print("Agosto")
elif mes ==9:
    print("Septiembre")
elif mes ==10:
    print("Octubre")
elif mes ==11:
    print("Noviembre")
elif mes ==12:
    print("Diciembre")
elif mes > 12:
    print("Numero del mes incorrecto")
    