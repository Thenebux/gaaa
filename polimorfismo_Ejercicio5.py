#Polimorfismo con Clases Abstractas (abc)
#Se utiliza el módulo abc para definir una clase abstracta EmpleadoBase,
#que obliga a las subclases (Empleado, Jefe, Director) a implementar sus propios métodos.
from abc import ABC, abstractmethod
# Clase abstracta
class EmpleadoBase(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @abstractmethod
    def calcular_bono(self):
        """Método obligatorio en las subclases"""
        pass

    @abstractmethod
    def trabajar(self):
        """Método obligatorio en las subclases"""
        pass

# Subclase 1 ----------------------------------------
class Empleado(EmpleadoBase):
    def calcular_bono(self):
        return self.salario * 0.05  # 5% de bono

    def trabajar(self):
        return f" {self.nombre} realiza labores operativas."

# Subclase 2 -----------------------------------------
class Jefe(EmpleadoBase):
    def calcular_bono(self):
        return self.salario * 0.10  # 10% de bono

    def trabajar(self):
        return f" {self.nombre} supervisa a su equipo y organiza tareas."

# Subclase 3 ------------------------------------------
class Director(EmpleadoBase):
    def calcular_bono(self):
        return self.salario * 0.20  # 20% de bono

    def trabajar(self):
        return f" {self.nombre} lidera la empresa y toma decisiones estratégicas."

#Programa Principal -----------------------------------
# Lista polimórfica
personal = [
    Empleado("Luis", 3000),
    Jefe("Claudia", 5000),
    Director("Roberto", 10000)
]
for persona in personal:
    print(f"{persona.trabajar()} Bono: ${persona.calcular_bono():.2f}")