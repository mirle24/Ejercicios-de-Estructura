#Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene dicho número.

user_input = int(input("Ingrese un numero"))
user_input = abs(user_input)
print("Numero original es: {}".format(user_input))
count=1
user_input //=10
while user_input > 0:
    user_input //=10
    count += 1
    print("El numero de digitos de dicho numero es:{}".format(count))
