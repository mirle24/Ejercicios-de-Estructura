#El IMC resulta de la división de la masa del individuo (en kilogramos)entre el
    # cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
    # del peso de una persona en relación con su altura.
    # Clasificación del IMC de acuerdo con la OMS de la ONU:
    # a. Menor a 16: Criterio de ingreso.
    # b. 16 a 16.9: infra peso.
    # c. 17 a 18.4: bajo peso.
    # d. 18.5 a 24.9: peso normal.
    # e. 25 a 29.9: sobrepeso.
    # f. 30 a 34.9: obesidad pre-mórbida.
    # g. 40 a 45: obesidad mórbida.
    # h. Mayor a 45: obesidad híper-mórbida.
    # Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en
    # centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
    # de IMC de la persona y la categoría en la cual fue clasificado.
    
masa=int(input("Escriba su peso en libras "))
estatura=int(input("Escriba su estatura en centímetros "))
peso = masa * 0.453591
imc = peso /estatura
if imc > 45 :
      print("SU IMC ES ",(imc), "Por lo tanto usted sufre de Obesidad Hiper- Morbida")
elif imc <=45 and (imc>=40):
      print("SU IMC ES " ,(imc), " Por lo tanto usted tiene Obesidad - Morbida ")
elif imc <= 35 and imc >= 30:
      print("SU IMC ES " ,(imc), "Por lo tanto usted tiene Pre- Morbida " )
elif imc <=29 and imc >=25:
      print("SU IMC ES " ,(imc), "Por lo tanto usted tiene Sobrepeso ")
elif imc <=25 and imc >=18:
      print("SU IMC ES " ,(imc), "Por lo tanto usted tiene Peso Normal ")
elif imc == 17:
      print("SU IMC ES " ,(imc),"Por lo tanto usted tiene Peso Bajo ")
elif imc ==19:
      print("SU IMC ES " ,(imc), "Por lo tanto usted tiene Infra Peso ")