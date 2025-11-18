import numpy as np
#Inicializando los vectores
vector1 = np.random.randint(1,9,size=9)
vector2 = np.random.randint(1,9,size=9)

print("\nImpresion de los vectores")
print("Impresion del Vector 1: ",vector1)
print("Impresion del Vector 2: ",vector2)

print("\nOperaciones Aritmeticas")
print("Suma de los Vectores: ",vector1 + vector2)
print("Resta de los Vectores: ",vector1 - vector2)
print("Multiplicacion de los Vectores: ",vector1 * vector2)
print("Division de los Vectores: ",vector1 / vector2)

print("\nImpresion del Vector accediendo a cada valores del vector")
for i in range(0, len(vector1)):
    print("Posicion ",i," = ",vector1[i])

vector3 = vector1 * vector2
vector = vector1 + vector3
matriz = vector.reshape(3, 3)
print(f"- Cambiando la forma del vector a una matriz 3x3\n{matriz}")


