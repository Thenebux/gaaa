-- ejemplo 1
class Empleado:
    # __nombre y __salario, son atributos privados protegidos contra acceso directo
    def __init__(self,nombre,salario):
        self.__nombre = nombre #atributo privado
        self.__salario = salario #atributo privado
    
    # Getter para el atributo nombre --------------
    @property
    def nombre(self):
        return self.__nombre

    #Setter para el atributo nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if nuevo_nombre.strip()!="":
            self.__nombre = nuevo_nombre
        else:
            print("El Nombre no puede estar vacio!!!!")

    # Getter para el atributo salario --------------
    @property #convierte el metodo en una propiedad de solo lectura getter, permite acceder como si fuera un atributo
    def salario(self):
        return self.__salario

    #Setter para el atributo salario
    @salario.setter
    def salario(self,nuevo_salario):
        if nuevo_salario >=0:
            self.__salario = nuevo_salario
        else:
            print("El Salario no puede ser Negativo!!!!")
    
    # Metodo para mostrar la informacion del empleado
    def mostrar_info(self):
        print(f"Empleado: {self.__nombre}, Salario: {self.__salario}")

#Programa Principal ----------------------------
emp1  = Empleado("Cristian",3500)
emp1.mostrar_info()
#Acceso controlado mediante propiedades
emp1.nombre = "Ariana" #usara el setter
emp1.salario = 3230 #usara el setter
#mostrar
print("Nombre: ",emp1.nombre) #usara el getter
print("Salario: ",emp1.salario) #usara el getter
#Valores Invalidados
emp1.nombre = ""
emp1.salario = -1200
-----------------------------------------------------------------------------------
-- ejemplo 2
class Estudiante:
       #Atributo de clase(compartido para todos los estudiantes)
       institucion = "Universidad Peruana de Ciencias Aplicadas"

       #Contructor se define los atributos de instancia
       def __init__(self,nombre,carrera, promedio):
           self.nombre = nombre
           self.carrera = carrera
           self.promedio = promedio

       #metodo de instancia:uso los atributos del objeto
       def mostrar_info(self):
           print(f"Estudiante: {self.nombre} | Carrera: {self.carrera} | Promedio: {self.promedio}")

       #metodo de clase: permite modificar el atributo de clase
       @classmethod
       def cambiar_institucion(cls,nueva_institucion):
           cls.institucion = nueva_institucion
           print(f"La institucion ahora se llama: {cls.institucion}")
       
#Programa Principal
est1 = Estudiante("Ariana Rodriguez","Ingenieria de Software",15.8)
est2 = Estudiante("Sharon Valeriano","Ingenieria de Sistemas",16.7)
#Mostrar informacion inicial
est1.mostrar_info()
est2.mostrar_info()
         
#cambiar un atributo de clase(afecta a todos los estudiantes)
Estudiante.cambiar_institucion("UPC-PERU")

#Mostrar informacion despues del cambio
est1.mostrar_info()
est2.mostrar_info()

#cambiar atributos de instancia(solo afecta a ese estudiante)
est1.promedio = 19.5
print("Despues de Actualizar el promedio de Ariana")
est1.mostrar_info()
est2.mostrar_info()

------------------------------------------------------------------------------------------- ejemplo 3
class Estudiante:
    intitucion ="Univesidad peruana de Ciencias Aplicadas"

    def __init__ (self,nombre,promedio):
        self.nombre = nombre
        self.promedio = promedio

    def mostrar_info(self):
        print(f"{self.nombre} | promedio: {self.promedio} | {Estudiante.intitucion}")

    #metodo estatico
    @staticmethod 
    def calcular_promedio_general(notas):
        #calcula el promedio general de una lista de notas
        if len(notas) ==0:
            return 0
        return sum(notas)/ len(notas)

#programa principal
e1 = Estudiante("Iliana", 18.7)
e1.mostrar_info()

promedio_curso = Estudiante.calcular_promedio_general([18,15,17,19])
print("promedio General del curso: ",promedio_curso)
-------------------------------------------------------------
-- Ejemplo 4
#Ejemplo Asociación
-------------------------------------------------------------
from pickle import OBJ


class Alumno:
 def __init__(self,codigo,nombre):
  self.__codigo=codigo
  self.__nombre=nombre
  self.__profesor=None
  print(f"Se ha creado el alumno {self.__nombre}")

 def get_nombre(self):
  return self.__nombre
 
 def get_codigo(self):
   return self.__codigo
 
 def get_profesor(self):
  return self.__profesor
 
 def set_nombre(self,nv_nombre): 
        if nv_nombre !=self.__nombre: 
            self.__nombre = nv_nombre
        else: 
            print("El nombre no se debe repetir!!!!")
   
 def set_codigo(self,nv_codigo): 
        if nv_codigo!=0: 
            self.__codigo = nv_codigo
        else: 
            print("El codigo debe ser un numero positivo!!!!")

 def set_profesor(self,profe):
   if isinstance(profe,Profesor):
    self.__profesor=profe
   else:
    raise ValueError("El elemento debe ser de tipo Profesor.")
   
 def mostr_datos(self):
    if self.__profesor:
     print(f"Alumno: {self.__nombre} \t Codigo: {self.__codigo} \t Profesor: {self.__profesor.get_pnombre()}")


class Profesor:
 def __init__(self,codigo,nombre,curso):
  self.__pcodigo=codigo
  self.__pnombre=nombre
  self.__curso=curso
  self.__estudiantes=[]
  print(f"Se ha creado el profesor {self.__pnombre}")

 def get_pnombre(self):
   return self.__pnombre
 
 def get_pcodigo(self):
   return self.__pcodigo
  
 def get_curso(self):
   return self.__curso
  
 def set_pnombre(self,nv_nombre): 
        if nv_nombre !=self.__pnombre: 
            self.__pnombre = nv_nombre
        else: 
            print("El nombre no se debe repetir!!!!")
   
 def set_pcodigo(self,nv_codigo): 
        if nv_codigo!=0: 
            self.__pcodigo = nv_codigo
        else: 
            print("El codigo debe ser un numero positivo!!!!")
 
 def set_curso(self,nv_curso): 
        if nv_curso !=self.__curso: 
            self.__curso = nv_curso
        else: 
            print("El curso no se puede repetir!!!!")

 def add_estudiante(self,estudiante):
     if isinstance(estudiante,Alumno):
        self.__estudiantes.append(estudiante)
     else:
        raise ValueError("El elemento debe ser tipo Alumno.")
  
 def listar_estudiantes(self):
     print(f"Lista de estudiantes del(la) profesor(a) {self.__pnombre}")
     if(len(self.__estudiantes)==0):
        print("No hay estudiantes registrados.")
     else:
        for estudiante in self.__estudiantes:
           print(estudiante.get_nombre())

 def mostr_datos(self):
     print(f"Profesor: {self.__pnombre} \t Codigo: {self.__pcodigo} \t Curso: {self.__curso}")

#programa principal
p1=Profesor("P001","Mario Montes", "Matematica")
p2=Profesor("P002","Julia Villanueva","Comunicacion")

print("------------------------------------------")

p1.mostr_datos()
p2.mostr_datos()

print("------------------------------------------")

p1.set_pcodigo("P003")
p2.set_pnombre("Julia Venegas")
p2.set_curso("Biologia")

p1.mostr_datos()
p2.mostr_datos()

print("------------------------------------------")

a1=Alumno("A001","Ana Gutierrez")
a2=Alumno("A002","Julio Gonzales")
a3=Alumno("A003","Alexander Pena")
a4=Alumno("A004","Rubi Hernandez")

print("------------------------------------------")
a1.set_profesor(p1)
a2.set_profesor(p1)
a3.set_profesor(p2)
a4.set_profesor(p1)

a1.mostr_datos()
a2.mostr_datos()
a3.mostr_datos()
a4.mostr_datos()

print("------------------------------------------")

a1.set_codigo("A011")
a1.set_nombre("Ana Guevara")

a1.set_profesor(p1)
a2.set_profesor(p1)
a3.set_profesor(p2)
a4.set_profesor(p1)

a1.mostr_datos()
a2.mostr_datos()
a3.mostr_datos()
a4.mostr_datos()

print("------------------------------------------")

p1.add_estudiante(a1)
p1.add_estudiante(a2)
p2.add_estudiante(a3)
p1.add_estudiante(a4)

p1.listar_estudiantes()
print("------------------------------------------")
p2.listar_estudiantes()

--------------------------------------------------------
-- Ejemplo de Dependencia
--------------------------------------------------------
class Impresora:
  def __init__(self, marca,modelo):
    self.__marca=marca
    self.__modelo=modelo

  def print_documento(self, documento):
    return f" La Impresora de marca {self.__marca} de modelo {self.__modelo} esta imprimiendo: {documento.get_contenido()}"

class DocumentoPDF:
  def get_contenido(self):
    return "Contenido del documento PDF"

class DocumentoWord:
  def get_contenido(self):
    return "Contenido del documento Word"

#===PROGRAMA PRINCIPAL===
# Usando la dependencia
Impresora = Impresora("Canon","G3110")
pdf = DocumentoPDF()
word = DocumentoWord()
print(Impresora.print_documento(pdf))  
# Va a mostrar: La Impresora de marca Canon de modelo G3110 esta imprimiendo: Contenido del documento PDF
print(Impresora.print_documento(word)) 

# Va a mostrar: La Impresora de marca Canon de modelo G3110 esta imprimiendo: Contenido del documento Word


-------------------------------------------------------------------------------
EJEMPLO DE RELACION DE ASOCIACION
-------------------------------------------------------------------------------
#Relación de Asociación: Es un vínculo estructural que implica una conexión permanente (mucho más que la dependencia) entre dos o más clases permitiendo que los objetos(instancias) de estas mismas interactuen entre sí estando conectados de manera unidireccional(Solo una clase conoce a la otra y puede interactuar con ella) o bidireccional (Ambas clases se conocen mutuamente y pueden comunicarse entre sí)

#Unidireccional
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def enseñar(self, estudiante):
        print(f"{self.nombre} está enseñando a {estudiante.nombre}")


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
#Instancia de los objetos de cada clase
profesor_1=Profesor("Cristhian Sanchez")
estudiante_1=Estudiante("Juan Flores")
profesor_1.enseñar(estudiante_1)

#Bidireccional
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.profesor = self  # el estudiante también conoce al profesor


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesor = None  # referencia al profesor
#Instancia de los objetos de cada clase
profesor_1=Profesor("Aaron Villa")
estudiante_1=Estudiante("Anderson Zaid")
estudiante_2=Estudiante("Juan Gabriel")
profesor_1.agregar_estudiante(estudiante_1)
profesor_1.agregar_estudiante(estudiante_2)
profesor_2=Profesor("Cristhian Sanchez")
estudiante_3=Estudiante("Alfredo Bryce")
profesor_2.agregar_estudiante(estudiante_3)
print(f"El estudiante {estudiante_1.nombre} tiene como profesor a {estudiante_1.profesor.nombre}")
print(f"El estudiante {estudiante_2.nombre} tiene como profesor a {estudiante_2.profesor.nombre}")
print(f"El estudiante {estudiante_3.nombre} tiene como profesor a {estudiante_3.profesor.nombre}")

-------------------------------------------------------------------------------
EJEMPLO DE RELACION DE ASOCIACION 2
-------------------------------------------------------------------------------

#Características de la relacion de asociación

#1.CARDINALIDAD: 
# Define la cantidad de objetos de una clase que están relacionados con objetos de otra clase. Cada asociación tiene dos cardinalidades o  multiplicidades (Cuántos objetos de la primera clase pueden relacionarse con un objeto de la segunda clase y Cuántos objetos de la segunda clase pueden relacionarse con un objeto de la primera clase) 

#1.2.SINMBOLOGÍA:
# 1 -> 1 y solo 1
# 0..1 -> 0 ó 1 (Asociación opcional)
# N..M -> Un valor entre N y M
# * -> varios
# 0..* -> 0 o muchos(ilimitado)
# 1..* -> 1 ó muchos
# 2..4 -> Rango específico
# 2,4..6,8 -> Múltiple, Rangos disjuntos

#2.ROLES:
#Son una herramienta que clarifica la participación de los objetos instanciados en una relación asignando roles, definiendo la interacción y función que desempeña cada uno en la misma.

print("=========================================================")

#Ejemplo que evidencia la presencia de asociación (cardinalidad y roles) con respecto a un profesor y sus alumnos
# Clase Estudiante: rol de "alumno"
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesor = None  # cada estudiante tiene 1 profesor (1..1)

    def asignar_profesor(self, profesor):
        self.profesor = profesor  # se vincula con un profesor
        print(f"El estudiante {self.nombre} ahora tiene como profesor a {profesor.nombre}.")


# Clase Profesor: rol de "docente"
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # puede tener uno o muchos estudiantes (1..*)

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.asignar_profesor(self)  # se establece la relación bidireccional

    def mostrar_estudiantes(self):
        print(f"El profesor {self.nombre} enseña a:")
        for e in self.estudiantes:
            print(f"   - {e.nombre}")

# Creación de objetos (instancias)
profesor1 = Profesor("Carlos Ruiz")

# Se crean estudiantes (cardinalidad 1..*)
est1 = Estudiante("Ana López")
est2 = Estudiante("Pedro Torres")
est3 = Estudiante("Lucía Ramos")

# Se asocian los objetos (1 profesor <--> muchos estudiantes)
profesor1.agregar_estudiante(est1)
profesor1.agregar_estudiante(est2)
profesor1.agregar_estudiante(est3)

# Mostrar las asociaciones desde ambos roles
print("\n--- Relación vista desde el Profesor ---")
profesor1.mostrar_estudiantes()

print("\n--- Relación vista desde el Estudiante ---")
print(f"{est1.nombre} tiene como profesor a {est1.profesor.nombre}")
print(f"{est2.nombre} tiene como profesor a {est2.profesor.nombre}")
print(f"{est3.nombre} tiene como profesor a {est3.profesor.nombre}")



