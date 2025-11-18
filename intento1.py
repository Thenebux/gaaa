from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, idVehiculo, capacidad=0, estado="Disponible"):
        self._id_vehiculo = idVehiculo
        self._capacidad_tn = 0
        self._estado = estado
        self.capacidad_tn = capacidad

    @property
    @abstractmethod
    def capacidad_tn(self):
        return self._capacidad_tn
    
    @capacidad_tn.setter
    @abstractmethod
    def capacidad_tn(self, capacidad):
        if capacidad > 0:
            self._capacidad_tn = capacidad
        else: print("La capacidad no puede ser negativa, seteando en 0 por defecto...")
    
    @abstractmethod
    def calcular_rendimiento(self):
        pass

class Operador(ABC):
    def __init__(self, nombre, dni, licencia):
        self._nombre = nombre
        self._dni = dni
        self._licencia = licencia
    
    @abstractmethod
    def registrar_operacion(self):
        pass

    @abstractmethod
    def calcular_bonos(self):
        pass

class CargaMineral():
    def __init__(self, mineral, humedad, pesoTransportado):
        self.tipo_mineral = mineral
        self.humedad = humedad
        self.pesoTransportado = pesoTransportado
    
    @property
    def pesoTransportado(self):
        return self.peso_transportado
    
    @pesoTransportado.setter
    def pesoTransportado(self, pesoTransportado):
        if pesoTransportado > 0:
            self.peso_transportado = pesoTransportado

class CamionTolva(Vehiculo):
    @property
    def capacidad_tn(self):
        return self._capacidad_tn
    
    @capacidad_tn.setter
    def capacidad_tn(self, capacidad):
        if capacidad > 0:
            self._capacidad_tn = capacidad
        else: print("La capacidad no puede ser negativa, seteando en 0 por defecto...")
        
    def calcular_rendimiento(self):
        pass

class VolqueteArticulado(Vehiculo):
    @property
    def capacidad_tn(self):
        return self._capacidad_tn
    
    @capacidad_tn.setter
    def capacidad_tn(self, capacidad):
        if capacidad > 0:
            self._capacidad_tn = capacidad
        else: print("La capacidad no puede ser negativa, seteando en 0 por defecto...")
        
    def calcular_rendimiento(self):
        pass

class CamionLigero(Vehiculo):
    @property
    def capacidad_tn(self):
        return self._capacidad_tn
    
    @capacidad_tn.setter
    def capacidad_tn(self, capacidad):
        if capacidad > 0:
            self._capacidad_tn = capacidad
        else: print("La capacidad no puede ser negativa, seteando en 0 por defecto...")
        
    def calcular_rendimiento(self):
        pass

class OperadorCamion(Operador):
    def registrar_operacion(self):
        
        pass

    def calcular_bonos(self):
        pass

class SupervisorTransporte(Operador):
    def registrar_operacion(self):
        pass

    def calcular_bonos(self):
        pass

class ControladorAlmacen(Operador):
    def registrar_operacion(self):
        pass

    def calcular_bonos(self):
        pass

class OperacionTransporte:
    def __init__(self, operador, vehiculo, cargaMineral):
        self.operador = operador
        self.vehiculo = vehiculo
        self.cargaMineral = cargaMineral




camion1 = CamionTolva(123,10,"Disponible")

print(camion1._capacidad_tn)

objeto1 = CargaMineral("Plata", 10, 20)

print(objeto1.peso_transportado)