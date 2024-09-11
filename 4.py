'''
Elabore un programa para un Hospital que determine, y muestre el nivel de Leucemia de 803 pacientes clasificando su puntaje si esta inferior a 10 no tiene Leucemia;
si esta entre 11 y 40, nivel bajo de Leucemia; si esta entre 40 y 69, nivel moderado de Leucemia, si esta entre 70 y 100, nivel grave de Leucemia.
'''

import random

# Generar puntajes aleatorios entre 1 y 100 para 803 pacientes
puntajes = [random.randint(1, 100) for _ in range(803)]

# Contadores para cada categoría de leucemia
cont_no_leucemia = 0
cont_bajo = 0
cont_moderado = 0
cont_grave = 0

resultados = []

# Clasificar el nivel de leucemia según el puntaje y contar
for puntaje in puntajes:
    if puntaje < 10:
        nivel = "No tiene Leucemia"
        cont_no_leucemia += 1
    elif 11 <= puntaje <= 40:
        nivel = "Nivel bajo de Leucemia"
        cont_bajo += 1
    elif 41 <= puntaje <= 69:
        nivel = "Nivel moderado de Leucemia"
        cont_moderado += 1
    elif 70 <= puntaje <= 100:
        nivel = "Nivel grave de Leucemia"
        cont_grave += 1
    else:
        nivel = "Puntaje no visto"  

    resultados.append((puntaje, nivel))

print("Resultados de niveles de Leucemia:")
for puntaje, nivel in resultados:
    print(f"Puntaje: {puntaje}, Nivel: {nivel}")

# Imprimir los totales por categoría
print(f"\nTotal de pacientes sin Leucemia: {cont_no_leucemia}")
print(f"Total de pacientes con nivel bajo de Leucemia: {cont_bajo}")
print(f"Total de pacientes con nivel moderado de Leucemia: {cont_moderado}")
print(f"Total de pacientes con nivel grave de Leucemia: {cont_grave}")

