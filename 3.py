'''
Elabore un programa para la facultad de Ingeniería que pida 400 números e indique si ese número es par o impar; 
me muestre un listado y me indique cuantos son pares y cuantos son impares.
'''
def es_par(num):
    return num % 2 == 0

# Inicializar contadores
contador_pares = 0
contador_impares = 0


resultados = []

print("Ingrese 400 números:")

for i in range(10):
    while True:
        try:
            numero = int(input(f"Número {i+1}: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    if es_par(numero):
        resultado = f"{numero} es par"
        contador_pares += 1
    else:
        resultado = f"{numero} es impar"
        contador_impares += 1

    resultados.append(resultado)

print("\nListado de resultados:")
for resultado in resultados:
    print(resultado)

print(f"\nCantidad de números pares: {contador_pares}")
print(f"Cantidad de números impares: {contador_impares}")
