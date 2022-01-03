
    # Todos los años que se dividen exactamente entre 400, o que son divisibles
    # exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
    # Usando estas premisas crea un algoritmo que lea una fecha como un número
    # entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
    # el mismo es un año bisiesto o no.
año=int(input("INGRESE AÑO "))
if año%4==0:
       print("EL AÑO QUE INGRESO " + str(año) + " ES BISIESTO")
else:
       print("EL AÑO QUE INGRESO " + str(año) + " NO ES BISIESTO")                                                                                                                                                                                                                                                                                  

