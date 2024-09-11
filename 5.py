'''
Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable,
registrando un puntaje que se clasifica de la siguiente forma si tiene 2 puntos está con un funcionamiento defectuoso, 
si tiene 3 puntos el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo.
'''

#Funcion de clasificacion
def clasificar_funcionamiento(puntaje):
    if puntaje == 2:
        return "Defectuoso 😞"
    elif puntaje == 3:
        return "Moderado 🫥"
    elif puntaje == 4:
        return "Óptimo 😊"
    else:
        return "Puntaje inválido"

# Inicializar contadores para cada categoría
contador_defectuoso = 0
contador_moderado = 0
contador_optimo = 0

clasificaciones = []

print("Ingrese los puntajes para 407 cabinas de metro cable:")

for i in range(20):
    while True:
        try:
            puntaje = int(input(f"Puntaje para cabina {i+1}: "))
            if puntaje in [2, 3, 4]:
                break
            else:
                print("Puntaje inválido. Debe ser 2, 3 o 4.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    clasificacion = clasificar_funcionamiento(puntaje)
    clasificaciones.append(f"Cabina {i+1}: {clasificacion}")

    #Reset
    if clasificacion == "Defectuoso 😞":
        contador_defectuoso += 1
    elif clasificacion == "Moderado 🫥":
        contador_moderado += 1
    elif clasificacion == "Óptimo 😊":
        contador_optimo += 1


print("\nListado de clasificaciones:")
for clasificacion in clasificaciones:
    print(clasificacion)

# Mostrar la cantidad de cabinas en cada categoría
print(f"\nCantidad de cabinas defectuosas: {contador_defectuoso}")
print(f"Cantidad de cabinas con funcionamiento moderado: {contador_moderado}")
print(f"Cantidad de cabinas óptimas: {contador_optimo}")
