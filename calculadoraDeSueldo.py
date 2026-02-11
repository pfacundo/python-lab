#quiero hacer un programa que calcule cuanto seria el sueldo por hora dado
#un monto mensual y las horas trabajadas a la semana en distintos puestos
#de trabajo.

def calcular_sueldo_por_hora(sueldo_mensual, horas_semanales):
    semanas_por_mes = 4  # Promedio de semanas en un mes
    horas_mensuales = horas_semanales * semanas_por_mes
    if horas_mensuales == 0:
        return 0
    sueldo_por_hora = sueldo_mensual / horas_mensuales
    return sueldo_por_hora
# Ejemplo de uso
#cabe destacar que en mare se paga un bono semanal de 200 pesos, lo que hace que
# el sueldo mensual 

sueldo_mensual = 9500 + 200*4 # Monto mensual
horas_semanales = 52  # Horas trabajadas por semana
mare = calcular_sueldo_por_hora(sueldo_mensual, horas_semanales)
print(f"Sueldo por hora en mare: ${mare:.2f}\n\
      horas semanales: {horas_semanales}")
sueldo_mensual2 = 10000
horas_semanales2 = 42
vika = calcular_sueldo_por_hora(sueldo_mensual2, horas_semanales2)
print(f"Sueldo por hora en vika: ${vika:.2f}\n\
      horas semanales: {horas_semanales2}")
#