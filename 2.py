'''Elabore un programa para el Éxito que determine el salario de los 1897 empleados de su compañía, 
teniendo en cuenta las comisiones y la seguridad social que debe pagar, e imprima el listado de la información.
'''
print("---------- ÉXITO S.A.S ----------")
num_empleados = 18
#Libreria random para sacar numeros aleatorios
import random

empleados = []
for i in range(num_empleados):
    # Salario base aleatorio entre 2000 y 5000
    salarioBase = random.uniform(2000, 5000)  
    # Comisión aleatoria entre 100 y 1000
    comision = random.uniform(100, 1000)  
    empleados.append({
        'empleado_id': i + 1,
        'salario_base': salarioBase,
        'comision': comision
    })

# Calcular el salario neto y mostrar la información
def calcular_salario_neto(salario_base, comision):
    salario_bruto = salario_base + comision
    seguridad_social = 0.04 * salario_bruto
    salario_neto = salario_bruto - seguridad_social
    return salario_neto

# Imprimir el listado de información
print(f"{'ID':<10} {'Salario Base':<15} {'Comisión':<10} {'Salario Neto':<15}")
print("-" * 50)
for empleado in empleados:
    salario_neto = calcular_salario_neto(empleado['salario_base'], empleado['comision'])
    print(f"{empleado['empleado_id']:<10} {empleado['salario_base']:<15.2f} {empleado['comision']:<10.2f} {salario_neto:<15.2f}")









