#En un almacén se hace un 20% de descuento a los clientes cuya compra superelos Bs 1000, 
# se desea que realice un algoritmo el cual tome por entrada el monto a
# pagar por el cliente y arroje como salida el monto aplicando el descuento de ser necesario.

valor= float(input("INGRESE EL VALOR DE SU COMPRA "))
if valor >=1000:
    descuento= valor * .20
    print("EL MONTO A PAGAR APLICANDOLE DESCUENTO ES: $ ",valor - descuento) 
else:
    descuento = 0
    print(" EL VALOR A PAGAR ES: $ ", str(valor) )
    print("NO APLICA DESCUENTO")