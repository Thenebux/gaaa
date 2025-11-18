
import numpy as np
filas = 3
columna = 3
#lista vacia
lista=[]
print("Ingreso de Valores de la Matriz 3*3")
for f in range(filas):
    for c in range(columna):
        frase = "Ingrese Valor Mat["+str(f) + ","+str(c)+"]: "
        valor=int(input(frase))
        lista.append(valor)

#convirtiendo la lista a matriz
print("\nConvirtiendo una Lista a una Matriz")
matriz = np.array(lista).reshape((filas,columna))
print(matriz)