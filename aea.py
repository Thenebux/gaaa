from abc import ABC, abstractmethod
class Vehiculo(ABC):
    estados_validos=["Disponible","En Mantenimiento","Transportando"]
    def __init__(self,id_vehiculo,capacidad_tn,estado):
        self._id_vehiculo=id_vehiculo
        self._capacidad_tn=0
        self._estado=None
        self.capacidad=capacidad_tn
        self.cambiar_Estado(estado)
    
    @property
    def idVehiculo(self):
        return self._id_vehiculo
    
    @property
    def capacidad(self):
        return self._capacidad_tn
    
    @capacidad.setter
    def capacidad(self,valor):
        if valor<0:
            print("Ingrese una capacidad positiva")
            return
        else:
            self._capacidad_tn=valor
        
    def cambiar_Estado(self,nuevo_estado):
        if nuevo_estado in self.estados_validos:
            self._estado=nuevo_estado
        else:
            print(f"Error: {nuevo_estado} no es un estado valido. Estados permitidos {self.estados_validos}")

    @abstractmethod
    def calcular_rendimiento(self):
        pass

    def __str__(self):
        return f"Id del vehiculo: {self._id_vehiculo} | Capacidad: {self._capacidad_tn} | Estado: {self._estado}"
        
class CamionTolva(Vehiculo):
    def __init__(self, id_vehiculo, capacidad_tn, estado,tipo_suspension,num_ejes,resistencia_chasis):
        super().__init__(id_vehiculo, capacidad_tn, estado)
        self.tipo_suspension=tipo_suspension
        self.num_ejes=num_ejes
        self.resistencia_chasis=resistencia_chasis

    def calcular_rendimiento(self):
        pass

class VolqueteArticulado(Vehiculo):
    def __init__(self, id_vehiculo, capacidad_tn, estado,tipo_suspension,num_ejes,resistencia_chasis):
        super().__init__(id_vehiculo, capacidad_tn, estado)
        self.tipo_suspension=tipo_suspension
        self.num_ejes=num_ejes
        self.resistencia_chasis=resistencia_chasis

    def calcular_rendimiento(self):
        pass


class CamionLigero(Vehiculo):
    def __init__(self, id_vehiculo, capacidad_tn, estado,tipo_suspension,num_ejes,resistencia_chasis):
        super().__init__(id_vehiculo, capacidad_tn, estado)
        self.tipo_suspension=tipo_suspension
        self.num_ejes=num_ejes
        self.resistencia_chasis=resistencia_chasis

    def calcular_rendimiento(self):
        pass

class Operador(ABC):
    def _init_(self,nombre,dni,licencia):
        self._nombre=nombre
        self._dni=dni
        self._licencia=licencia
        
    @abstractmethod
    def registrar_operacion(self):
        pass
    
    def calcular_bonos(self):
        return 0
    
class OperadorCamion(Operador):
    def registrar_operacion(self):
        print(f"{self._nombre} registró la operación de transporte en camión")
        
    def calcular_bonos(self):
        return 200
    
class SupervisorTransporte(Operador):
    def registrar_operacion(self):
        print(f"{self._nombre} registró supervisión de transporte")

    def calcular_bonos(self):
        return 300
class ControladorAlmacen(Operador):
    def registrar_operacion(self):
        print(f"{self._nombre} registró control de almacén")

    def calcular_bonos(self):
        return 280