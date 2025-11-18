import numpy as np
lista = [25, 12, 15, 66, 12.5, 25.5]
vector = np.array(lista)
#Metodos del numpy
print(f"- Suma de todos los elementos: {np.sum(vector)}\n")
print(f"- Promedio de todos los elementos: {np.mean(vector)}\n")
print(f"- El mayor de todos los elementos: {np.max(vector)}\n")
print(f"- El menor de todos los elementos: {np.min(vector)}\n")
#cambiando de forma a la matriz
matriz = vector.reshape(3, 2)
print(f"- Cambiando la forma del vector a una matriz 3x2\n{matriz}")
