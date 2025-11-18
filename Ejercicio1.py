import numpy as np #Creas una variable tipo numpy -> np
print("\nVersion del numpy")
print(np.__version__)#muestra la version numpy
#manejo de la informacion a traves del objeto numpy np
arrayUnidimensional = np.array([1,2,-1,4.9])
#imprimiendo la arrays
print("\nImprimiendo Array Completo - Directo")
print(arrayUnidimensional) #impresion de manera directa
#imprimiendo los elementos unop a uno
print("\nImprimiendo Array - Cada Objeto")
for i in arrayUnidimensional:
    print(i)

print("\nCreando un Arrays Unidimensional - Generado(Random)")
ArrayUnid_Aleatorio = np.random.rand(8)
print(ArrayUnid_Aleatorio)

print("\nCreando un Arrays Unidimensional - Generado(Random) - Rango")
ArrayUnid_Aleatorio_Entero = np.random.randint(5,20,size= 5)
print(ArrayUnid_Aleatorio_Entero)   