#Gestión de empleados con NumPy - vamos a suponer que queremos manejar la 
#información de varios empleados: ID, Edad y  Sueldo y calcular 
#estadísticas básicas usando solo NumPy.
import numpy as np
# Crear datos iniciales **********************************
# IDs de empleados
ids = np.array([101, 102, 103, 104, 105])
# Edades de empleados
edades = np.array([25, 32, 40, 29, 50])
# Sueldos (en dólares)
sueldos = np.array([2500, 3200, 4000, 2900, 5000])
# Mostrar la información completa ************************
print("---- LISTADO DE EMPLEADOS ----")
for i in range(len(ids)):
    print(f"ID: {ids[i]} | Edad: {edades[i]} anios | Sueldo: ${sueldos[i]}")

#Calcular estadísticas con NumPy **************************
print("\n---- ESTADISTICAS ----")
print(f"Edad promedio: {np.mean(edades):.2f} anios")
print(f"Sueldo promedio: ${np.mean(sueldos):.2f}")
print(f"Sueldo maximo: ${np.max(sueldos)}")
print(f"Sueldo minimo: ${np.min(sueldos)}")

# Aplicar operaciones vectorizadas (sin bucles)
# Aumentar los sueldos un 10%
sueldos_actualizados = sueldos * 1.10
print("\n---- SUELDOS ACTUALIZADOS (10% aumento)----")
for i in range(len(ids)):
    print(f"ID: {ids[i]} | Nuevo sueldo: ${sueldos_actualizados[i]:.2f}")


# Filtrar empleados mayores de 30 años
mayores_30 = edades > 30 # condicion
print("\n---- EMPLEADOS MAYORES DE 30 ----")
print("IDs:", ids[mayores_30])
print("Edades:", edades[mayores_30])
print("Sueldos:", sueldos[mayores_30])

# Ordenar empleados por sueldo
indice_orden = np.argsort(sueldos)
print(indice_orden)
print("\n---- EMPLEADOS ORDENADOS POR SUELDO -----")
for i in indice_orden:
    print(f"ID: {ids[i]} | Sueldo: ${sueldos[i]}")

