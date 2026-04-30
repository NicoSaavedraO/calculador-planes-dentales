import os
os.system("cls")

PLAN_DENTAL = 80000
RADIOGRAFIA_DENTAL = 12000

try:
    edad = int(input("Ingrese la edad del paciente:\n"))
    while edad < 0:
        edad = int(input("Edad ingresada no válida, ingrese la edad nuevamente:\n"))
    quintil = int(input("Ingrese le quintil al que pertenece (1 - 5):\n"))
    while quintil not in range(1,6):
        quintil = int(input("Quintil inválido, ingreselo nuevamente:\n"))
except:
    print("Valor ingresado no válido")

if edad <= 25 and (quintil == 1 or quintil == 2):
    descuento_plan = 0.18
elif edad <= 25 and (quintil == 3 or quintil == 4):
    descuento_plan = 0.12
elif edad >= 26 and edad <= 45 and (quintil == 1 or quintil == 2):
    descuento_plan = 0.12
elif edad >= 26 and edad <= 45 and (quintil == 3 or quintil == 4):
    descuento_plan = 0.08
elif edad > 45:
    descuento_plan = 0

if quintil == 1 or quintil == 2 or quintil == 3:
    descuento_radio = 0.1
else:
    descuento_radio = 0
if edad <= 40:
    desc_adi = 0.05
else:
    desc_adi = 0

provi_plan = PLAN_DENTAL * descuento_plan
provi_radio = (RADIOGRAFIA_DENTAL * descuento_radio) + (RADIOGRAFIA_DENTAL * desc_adi)
total_plan = PLAN_DENTAL - provi_plan
total_radio = RADIOGRAFIA_DENTAL - provi_radio
print(f"Edad del usuario:\n{edad}")
print(f"Quintil del usuario:\n{quintil}")
print(f"El valor del plan es:\n{total_plan}")
print(f"El valor de la radiografía es:\n{total_radio}")