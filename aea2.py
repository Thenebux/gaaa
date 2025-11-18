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
    def __init__(self, id_vehiculo, capacidad_tn, estado,num_ejes,resistencia_chasis):
        super().__init__(id_vehiculo, capacidad_tn, estado)
        self._num_ejes=num_ejes
        self._resistencia_chasis=resistencia_chasis # Normal o Reforzado
    #Su rendimiento del camion tolva se basa en modificar su capacidad base antes de calcular los viajes
    #rendimiento = (capacidad base + sobrecarga segura) * viajes fijos por Hora
    def calcular_rendimiento(self):
        capacidad_efectiva=self.capacidad #el camion lleva su capacidad normal
        viajes_hora=2 #Se puede llevar 2 viajes pesados por hora
        if self._resistencia_chasis=="Reforzado":
            sobrecarga=self._num_ejes*1.5 #Si es reforzada gana 1.5 toneladas extra por cada eje
            capacidad_efectiva=self.capacidad+sobrecarga
        #calculo final
        rendimiento_total=capacidad_efectiva*viajes_hora
        print(f"Rendimiento del camion Tolva: ID [{self.idVehiculo}]: {rendimiento_total:.2f} Tn/hr")
        return rendimiento_total

class VolqueteArticulado(Vehiculo): 
    def __init__(self, id_vehiculo, capacidad_tn, estado,angulo_giro):
        super().__init__(id_vehiculo, capacidad_tn, estado)
        self.angulo_giro=angulo_giro
    #rendimiento = capacidad del viaje/tiempo del viaje en horas
    def calcular_rendimiento(self):
        tiempo_ciclo=15.0 #tiempo promedio 
        #calcular ahorro de tiempo
        ahorrar_tiempo=0
        if self.angulo_giro>40: #inventamos que el giro "normal" es 40 grados
            ahorrar_tiempo=(self.angulo_giro-40)*0.01 #ahorras 6 segundos (0.1) minutos por cada grado extra de giro
        #calculamos el tiempo real del ciclo
        tiempo_calculado_min= tiempo_ciclo-ahorrar_tiempo

        tiempo_ciclo_fin_min=max(1.0,tiempo_calculado_min) #asegura que el tiempo no sea menor a 1 minuto
        tiempo_ciclo_fin_hr=tiempo_ciclo_fin_min/60.0      #convertimos minutos a horas porque el rendimiento es en Tn/Hora
        #calculo final
        rendimiento_total=self.capacidad/tiempo_ciclo_fin_hr

        print(f"Rendimiento Volquete Art. [ID:{self.idVehiculo}] Rendimiento: {rendimiento_total:.2f} Tn/Hr")
        return rendimiento_total

class CamionLigero(Vehiculo):
    def __init__(self, id_vehiculo, capacidad_tn, estado,tipo_combustible,velocidad_max):
        super().__init__(id_vehiculo, capacidad_tn, estado)
        self._tipo_combustible=tipo_combustible
        self._velocidad_max=velocidad_max
    
    #rendimiento = (Velocidad / distancia ruta)*capacidad
    def calcular_rendimiento(self):
        distancia_promedio=20 #una ruta fija de 20km (ida y vuelta)
        # 1.Calcula viajes 
        #si el camion va a 80 km/h y la ruta es de 20 km la formula es 80/20 = 4 viajes por hora
        viajes_hora=self._velocidad_max/max(1,distancia_promedio) #formula para calcular cuantos viajes hace en 1 hora
        rendimiento_base=self.capacidad*viajes_hora #numero de viajes * la carga que hace por viaje
        rendimiento_total=rendimiento_base #por si no usa gasolina no se le descuenta una penalidad y se queda el rendimiento base
        if self._tipo_combustible== "Gasolina":
            penalidad=rendimiento_base*0.05     #supongamos que la gasolina es 5% menos eficiente
            rendimiento_total=rendimiento_base-penalidad
        print(f"[Rendimiento Camión Ligero ID: {self.idVehiculo}]: {rendimiento_total:.2f} Tn/hr")
        return rendimiento_total

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