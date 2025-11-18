import numpy as np
# Definición de la clase Empleado
class Empleado:
    def __init__(self, id_empleado, nombre, edad, sueldo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def __str__(self):
        return f"ID: {self.id_empleado} | {self.nombre} | Edad: {self.edad} | Sueldo: ${self.sueldo:.2f}"

    def aplicar_aumento(self, porcentaje):
        #Aumenta el sueldo del empleado en un porcentaje dado
        self.sueldo *= (1 + porcentaje / 100)

# Definición de la clase Empresa
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        #Agrega un empleado a la lista
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print(f"\n---- LISTADO DE EMPLEADOS DE {self.nombre.upper()} ----")
        for e in self.empleados:
            print(e)

    def obtener_sueldos_numpy(self):
        #Devuelve un array NumPy con los sueldos
        return np.array([e.sueldo for e in self.empleados])

    def obtener_edades_numpy(self):
        #Devuelve un array NumPy con las edades
        return np.array([e.edad for e in self.empleados])

    def estadisticas_sueldos(self):
        #Calcula estadísticas usando NumPy
        sueldos = self.obtener_sueldos_numpy()
        print("\n---- ESTADÍSTICAS DE SUELDOS ----")
        print(f"Sueldo promedio: ${np.mean(sueldos):.2f}")
        print(f"Sueldo máximo: ${np.max(sueldos):.2f}")
        print(f"Sueldo mínimo: ${np.min(sueldos):.2f}")

    def empleados_mayores_de(self, edad_limite):
        #Filtra empleados mayores de cierta edad
        edades = self.obtener_edades_numpy()
        mayores = edades > edad_limite
        print(f"\n---- EMPLEADOS MAYORES DE {edad_limite} ----")
        for i, e in enumerate(self.empleados):
            if mayores[i]:
                print(e)

    def aumentar_sueldos(self, porcentaje):
        #Aumenta el sueldo de todos los empleados
        print(f"\nAplicando aumento general del {porcentaje}%...")
        for e in self.empleados:
            e.aplicar_aumento(porcentaje)
# Programa principal
if __name__ == "__main__":
    # Crear la empresa
    empresa = Empresa("LaPalma Soluciones TEC")
    # Agregar empleados
    empresa.agregar_empleado(Empleado(101, "Iliana Palacios", 28, 3000))
    empresa.agregar_empleado(Empleado(102, "Andre Sanchez", 35, 4200))
    empresa.agregar_empleado(Empleado(103, "Alejandro Huachez", 41, 5000))
    empresa.agregar_empleado(Empleado(104, "Fatima Flores", 24, 2800))
    empresa.agregar_empleado(Empleado(105, "Zoila Herrera", 50, 5500))

    # Mostrar todos los empleados
    empresa.mostrar_empleados()

    # Calcular estadísticas con NumPy
    empresa.estadisticas_sueldos()

    # Filtrar mayores de 30 años
    empresa.empleados_mayores_de(30)

    # Aumentar sueldos un 10%
    empresa.aumentar_sueldos(10)

    # Verificar actualización
    empresa.mostrar_empleados()
