import numpy as np
print("Creacion de una Lista")
my_list = [1,2,3] #lista en python
print(my_list)
print("Conversion de Lista a una Arrays ")
np.array(my_list) #conversion de una lista a arreglo mediante el método 'array'
a = np.array(my_list) #se puede asignar a una variable
print(a)

print("\nTipo de dato del Arrays")
print(type(a)) #tipo de dato
print("\nTipos de Datos de los Objetos del Arrays")
print(a.dtype)  #tipo de datos que estan en el arreglo

print("Trabajando con una Matriz")
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
print("Conversion de Lista a una Arrays ")
b= np.array(my_matrix) # conversion de una lista de listas a Matriz)
print(b)
