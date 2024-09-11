"""Elabore un programa para la Universidad de Florida que calcule los primeros 100 números de la siguiente
    serie 5, 8, 13, 21, ... sin mostrar el 13, y muestre la lista del resultado de los números.
"""

#Declaramos las variabes con los primeros numeros de la serie
num1, num2 = 5, 8
resultado = []

# 100 PRIMEROS NUMEROS DE LA SERIE GENERADOS
for _ in range(100):
    #Excluimos al 13
    if num1 != 13:   
        resultado.append(num1)
    num1, num2 = num2, num1 + num2


print("Los primeros 100 numeros de la serie (sin el 13):")
print(resultado)
