from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

# ============================================================================
# CLASES ABSTRACTAS BASE
# ============================================================================

class Vehiculo(ABC):
    """Clase abstracta base para todos los vehículos de transporte"""
    
    def __init__(self, id_vehiculo: str, capacidad_tn: float):
        self._id_vehiculo = id_vehiculo
        self.capacidad_tn = capacidad_tn  # Usa el setter para validar
        self._estado = "Disponible"  # Disponible, En Mantenimiento, Transportando
    
    @property
    def id_vehiculo(self) -> str:
        return self._id_vehiculo
    
    @property
    def capacidad_tn(self) -> float:
        return self._capacidad_tn
    
    @capacidad_tn.setter
    def capacidad_tn(self, valor: float):
        if valor < 0:
            raise ValueError("La capacidad no puede ser negativa")
        self._capacidad_tn = valor
    
    @property
    def estado(self) -> str:
        return self._estado
    
    def cambiar_estado(self, nuevo_estado: str):
        """Cambia el estado del vehículo"""
        estados_validos = ["Disponible", "En Mantenimiento", "Transportando"]
        if nuevo_estado in estados_validos:
            self._estado = nuevo_estado
        else:
            raise ValueError(f"Estado inválido. Debe ser uno de: {estados_validos}")
    
    @abstractmethod
    def calcular_rendimiento(self, distancia_km: float, peso_tn: float) -> float:
        """Método abstracto para calcular el rendimiento del vehículo"""
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} {self._id_vehiculo} - Capacidad: {self._capacidad_tn}tn - Estado: {self._estado}"


class Operador(ABC):
    """Clase abstracta base para todos los operadores"""
    
    def __init__(self, nombre: str, dni: str, licencia: str):
        self._nombre = nombre
        self._dni = dni
        self._licencia = licencia
        self._operaciones_realizadas = 0
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def dni(self) -> str:
        return self._dni
    
    @property
    def licencia(self) -> str:
        return self._licencia
    
    @abstractmethod
    def registrar_operacion(self, operacion) -> str:
        """Método abstracto para registrar una operación"""
        pass
    
    @abstractmethod
    def calcular_bonos(self) -> float:
        """Método abstracto polimórfico para calcular bonos según tipo de operador"""
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self._nombre} (DNI: {self._dni}, Lic: {self._licencia})"


# ============================================================================
# CLASES CONCRETAS DE VEHÍCULOS (Herencia + Polimorfismo)
# ============================================================================

class CamionTolva(Vehiculo):
    """Camión con tolva para transporte de mineral a granel"""
    
    def __init__(self, id_vehiculo: str, capacidad_tn: float, tipo_suspension: str, num_ejes: int):
        super().__init__(id_vehiculo, capacidad_tn)
        self.tipo_suspension = tipo_suspension
        self.num_ejes = num_ejes
    
    def calcular_rendimiento(self, distancia_km: float, peso_tn: float) -> float:
        """Rendimiento basado en toneladas-kilómetro por eje"""
        if self.num_ejes == 0:
            return 0
        return (peso_tn * distancia_km) / self.num_ejes


class VolqueteArticulado(Vehiculo):
    """Volquete articulado para terrenos difíciles"""
    
    def __init__(self, id_vehiculo: str, capacidad_tn: float, resistencia_chasis: str, traccion: str):
        super().__init__(id_vehiculo, capacidad_tn)
        self.resistencia_chasis = resistencia_chasis
        self.traccion = traccion  # 4x4, 6x6, etc.
    
    def calcular_rendimiento(self, distancia_km: float, peso_tn: float) -> float:
        """Rendimiento ajustado por tracción y resistencia del chasis"""
        factor_traccion = 1.3 if "6x6" in self.traccion else 1.0
        factor_resistencia = 1.2 if self.resistencia_chasis == "Alta" else 1.0
        return (peso_tn * distancia_km * factor_traccion * factor_resistencia) / 100


class CamionLigero(Vehiculo):
    """Camión ligero para cargas pequeñas y distancias cortas"""
    
    def __init__(self, id_vehiculo: str, capacidad_tn: float, tipo_carroceria: str):
        super().__init__(id_vehiculo, capacidad_tn)
        self.tipo_carroceria = tipo_carroceria
    
    def calcular_rendimiento(self, distancia_km: float, peso_tn: float) -> float:
        """Rendimiento simple para vehículos ligeros"""
        return (peso_tn * distancia_km) / 10


# ============================================================================
# CLASES CONCRETAS DE OPERADORES (Herencia + Polimorfismo)
# ============================================================================

class OperadorCamion(Operador):
    """Operador responsable de conducir los vehículos"""
    
    def __init__(self, nombre: str, dni: str, licencia: str, años_experiencia: int):
        super().__init__(nombre, dni, licencia)
        self.años_experiencia = años_experiencia
    
    def registrar_operacion(self, operacion) -> str:
        self._operaciones_realizadas += 1
        return f"Operación registrada por {self._nombre}: Transporte de {operacion.carga.peso_tn}tn de {operacion.carga.tipo_mineral}"
    
    def calcular_bonos(self) -> float:
        """Bono basado en operaciones realizadas y experiencia"""
        bono_base = 50.0
        bono_operaciones = self._operaciones_realizadas * 20.0
        bono_experiencia = self.años_experiencia * 10.0
        return bono_base + bono_operaciones + bono_experiencia


class SupervisorTransporte(Operador):
    """Supervisor que coordina las operaciones de transporte"""
    
    def __init__(self, nombre: str, dni: str, licencia: str, area_supervision: str):
        super().__init__(nombre, dni, licencia)
        self.area_supervision = area_supervision
    
    def registrar_operacion(self, operacion) -> str:
        self._operaciones_realizadas += 1
        return f"Supervisión registrada por {self._nombre} en {self.area_supervision}: Operación validada correctamente"
    
    def calcular_bonos(self) -> float:
        """Bono basado en operaciones supervisadas"""
        bono_base = 100.0
        bono_supervision = self._operaciones_realizadas * 30.0
        return bono_base + bono_supervision


class ControladorAlmacen(Operador):
    """Controlador encargado de la recepción en almacén"""
    
    def __init__(self, nombre: str, dni: str, licencia: str, turno: str):
        super().__init__(nombre, dni, licencia)
        self.turno = turno
    
    def registrar_operacion(self, operacion) -> str:
        self._operaciones_realizadas += 1
        return f"Recepción registrada por {self._nombre} (Turno {self.turno}): {operacion.carga.peso_tn}tn de {operacion.carga.tipo_mineral}"
    
    def calcular_bonos(self) -> float:
        """Bono basado en recepciones procesadas"""
        bono_base = 70.0
        bono_recepciones = self._operaciones_realizadas * 15.0
        return bono_base + bono_recepciones


# ============================================================================
# COMPOSICIÓN: CargaMineral
# ============================================================================

class CargaMineral:
    """Clase que representa la carga de mineral transportada (COMPOSICIÓN)"""
    
    def __init__(self, tipo_mineral: str, humedad: float, peso_tn: float):
        self._tipo_mineral = tipo_mineral
        self._humedad = humedad
        self.peso_tn = peso_tn  # Usa el setter para validar
    
    @property
    def tipo_mineral(self) -> str:
        return self._tipo_mineral
    
    @property
    def humedad(self) -> float:
        return self._humedad
    
    @property
    def peso_tn(self) -> float:
        return self._peso_tn
    
    @peso_tn.setter
    def peso_tn(self, valor: float):
        if valor < 0:
            raise ValueError("El peso no puede ser negativo")
        self._peso_tn = valor
    
    def calcular_peso_seco(self) -> float:
        """Calcula el peso seco del mineral considerando la humedad"""
        return self._peso_tn * (1 - self._humedad / 100)
    
    def __str__(self):
        return f"{self._tipo_mineral}: {self._peso_tn}tn (Humedad: {self._humedad}%)"


# ============================================================================
# CLASE OPERACIÓN DE TRANSPORTE (Agregación + Composición)
# ============================================================================

class OperacionTransporte:
    """Representa una operación completa de transporte de mineral"""
    
    def __init__(self, operador: OperadorCamion, vehiculo: Vehiculo, 
                 tipo_mineral: str, humedad: float, peso_tn: float, distancia_km: float):
        # AGREGACIÓN: operador y vehículo existen independientemente
        self.operador = operador
        self.vehiculo = vehiculo
        
        # COMPOSICIÓN: CargaMineral depende de esta operación
        self.carga = CargaMineral(tipo_mineral, humedad, peso_tn)
        
        self.distancia_km = distancia_km
        self.hora_inicio = datetime.now()
        self.hora_fin = None
        self._validada = False
    
    def validar_carga(self) -> bool:
        """Valida que el peso no exceda la capacidad del vehículo"""
        if self.carga.peso_tn > self.vehiculo.capacidad_tn:
            print(f"⚠️ ADVERTENCIA: Peso {self.carga.peso_tn}tn excede capacidad {self.vehiculo.capacidad_tn}tn")
            return False
        self._validada = True
        return True
    
    def iniciar_transporte(self):
        """Inicia la operación de transporte"""
        if not self._validada:
            raise Exception("La operación debe ser validada antes de iniciar")
        
        self.vehiculo.cambiar_estado("Transportando")
        print(f"\n🚛 Iniciando transporte: {self.vehiculo.id_vehiculo}")
        print(f"   Operador: {self.operador.nombre}")
        print(f"   Carga: {self.carga}")
        print(f"   Distancia: {self.distancia_km} km")
    
    def finalizar_transporte(self):
        """Finaliza la operación de transporte"""
        self.hora_fin = datetime.now()
        self.vehiculo.cambiar_estado("Disponible")
    
    def calcular_rendimiento_operacion(self) -> float:
        """Calcula el rendimiento de la operación (polimorfismo)"""
        return self.vehiculo.calcular_rendimiento(self.distancia_km, self.carga.peso_tn)
    
    def generar_reporte(self) -> str:
        """Genera reporte detallado de la operación (polimorfismo)"""
        duracion = (self.hora_fin - self.hora_inicio).seconds / 60 if self.hora_fin else 0
        rendimiento = self.calcular_rendimiento_operacion()
        
        reporte = f"""
{'='*70}
REPORTE DE OPERACIÓN DE TRANSPORTE
{'='*70}
Vehículo: {self.vehiculo}
Operador: {self.operador.nombre} (Experiencia: {self.operador.años_experiencia} años)
Carga: {self.carga}
Peso Seco: {self.carga.calcular_peso_seco():.2f}tn
Distancia: {self.distancia_km} km
Duración: {duracion:.1f} minutos
Rendimiento: {rendimiento:.2f} unidades
Estado: {"✓ COMPLETADA" if self.hora_fin else "⏳ EN PROCESO"}
{'='*70}
"""
        return reporte


# ============================================================================
# ALMACÉN MINERAL (Agregación)
# ============================================================================

class AlmacenMineral:
    """Gestiona el inventario de mineral recibido (AGREGACIÓN)"""
    
    def __init__(self, nombre: str, capacidad_total_tn: float):
        self.nombre = nombre
        self.capacidad_total_tn = capacidad_total_tn
        self._inventario = {
            "Cobre": 0.0,
            "Plata": 0.0,
            "Oro": 0.0,
            "Mineral Mixto": 0.0
        }
        self._operaciones_recibidas: List[OperacionTransporte] = []
    
    def registrar_ingreso(self, operacion: OperacionTransporte, controlador: ControladorAlmacen) -> bool:
        """Registra el ingreso de una operación al almacén"""
        tipo = operacion.carga.tipo_mineral
        peso = operacion.carga.peso_tn
        
        if self.calcular_stock_total() + peso > self.capacidad_total_tn:
            print(f"⚠️ Almacén lleno. Capacidad excedida.")
            return False
        
        if tipo in self._inventario:
            self._inventario[tipo] += peso
            self._operaciones_recibidas.append(operacion)
            print(f"\n✓ Ingreso registrado al almacén {self.nombre}")
            print(f"  {controlador.registrar_operacion(operacion)}")
            print(f"  Stock actual de {tipo}: {self._inventario[tipo]:.2f}tn")
            return True
        else:
            print(f"⚠️ Tipo de mineral '{tipo}' no reconocido")
            return False
    
    def calcular_stock_total(self) -> float:
        """Calcula el stock total en el almacén"""
        return sum(self._inventario.values())
    
    def obtener_reporte_mensual(self) -> str:
        """Genera reporte mensual del almacén"""
        reporte = f"""
{'='*70}
REPORTE MENSUAL - ALMACÉN {self.nombre}
{'='*70}
Capacidad Total: {self.capacidad_total_tn}tn
Stock Actual: {self.calcular_stock_total():.2f}tn
Ocupación: {(self.calcular_stock_total()/self.capacidad_total_tn)*100:.1f}%

INVENTARIO POR TIPO DE MINERAL:
"""
        for mineral, cantidad in self._inventario.items():
            reporte += f"  • {mineral}: {cantidad:.2f}tn\n"
        
        reporte += f"\nTotal de operaciones recibidas: {len(self._operaciones_recibidas)}\n"
        reporte += "="*70
        return reporte


# ============================================================================
# SISTEMA PRINCIPAL
# ============================================================================

class SistemaGestionTransporte:
    """Sistema principal de gestión de transporte minero"""
    
    def __init__(self):
        self.vehiculos: List[Vehiculo] = []
        self.operadores: List[Operador] = []
        self.operaciones: List[OperacionTransporte] = []
        self.almacenes: List[AlmacenMineral] = []
    
    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)
    
    def agregar_operador(self, operador: Operador):
        self.operadores.append(operador)
    
    def agregar_almacen(self, almacen: AlmacenMineral):
        self.almacenes.append(almacen)
    
    def generar_reporte_diario(self) -> str:
        """Genera reporte completo del día"""
        reporte = f"""
{'#'*70}
REPORTE DIARIO - SISTEMA DE GESTIÓN DE TRANSPORTE
ETCIPSA S.A.
Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}
{'#'*70}

FLOTA DE VEHÍCULOS ({len(self.vehiculos)}):
"""
        for v in self.vehiculos:
            reporte += f"  • {v}\n"
        
        reporte += f"\nOPERADORES REGISTRADOS ({len(self.operadores)}):\n"
        for op in self.operadores:
            reporte += f"  • {op} - Bono: S/.{op.calcular_bonos():.2f}\n"
        
        reporte += f"\n\nOPERACIONES REALIZADAS ({len(self.operaciones)}):\n"
        total_peso_transportado = sum(op.carga.peso_tn for op in self.operaciones)
        total_distancia = sum(op.distancia_km for op in self.operaciones)
        reporte += f"  • Peso total transportado: {total_peso_transportado:.2f}tn\n"
        reporte += f"  • Distancia total recorrida: {total_distancia:.2f}km\n"
        
        reporte += "\n" + "#"*70
        return reporte


# ============================================================================
# ESCENARIO DE EJECUCIÓN
# ============================================================================

def ejecutar_escenario():
    """Escenario completo de demostración del sistema"""
    
    print("\n" + "="*70)
    print("SISTEMA DE GESTIÓN DE TRANSPORTE DE MINERAL - ETCIPSA S.A.")
    print("="*70)
    
    # Crear el sistema
    sistema = SistemaGestionTransporte()
    
    # 1. CREAR VEHÍCULOS DE DIFERENTES TIPOS
    print("\n📦 Registrando vehículos...")
    camion1 = CamionTolva("CT-001", 25.0, "Neumática", 6)
    camion2 = VolqueteArticulado("VA-002", 35.0, "Alta", "6x6")
    camion3 = CamionLigero("CL-003", 10.0, "Volcadora")
    
    sistema.agregar_vehiculo(camion1)
    sistema.agregar_vehiculo(camion2)
    sistema.agregar_vehiculo(camion3)
    print(f"  ✓ {len(sistema.vehiculos)} vehículos registrados")
    
    # 2. REGISTRAR OPERADORES
    print("\n👷 Registrando operadores...")
    operador1 = OperadorCamion("Juan Pérez", "12345678", "A3B", 8)
    operador2 = OperadorCamion("María González", "87654321", "A3B", 5)
    supervisor = SupervisorTransporte("Carlos Ruiz", "11223344", "A2", "Zona Norte")
    controlador = ControladorAlmacen("Ana Torres", "55667788", "A1", "Diurno")
    
    sistema.agregar_operador(operador1)
    sistema.agregar_operador(operador2)
    sistema.agregar_operador(supervisor)
    sistema.agregar_operador(controlador)
    print(f"  ✓ {len(sistema.operadores)} operadores registrados")
    
    # 3. CREAR ALMACÉN
    print("\n🏭 Configurando almacén...")
    almacen = AlmacenMineral("Almacén Central", 500.0)
    sistema.agregar_almacen(almacen)
    print(f"  ✓ Almacén '{almacen.nombre}' creado con capacidad {almacen.capacidad_total_tn}tn")
    
    # 4. EJECUTAR OPERACIONES DE TRANSPORTE
    print("\n" + "="*70)
    print("EJECUTANDO OPERACIONES DE TRANSPORTE")
    print("="*70)
    
    # OPERACIÓN 1: Cobre
    print("\n--- OPERACIÓN 1: TRANSPORTE DE COBRE ---")
    op1 = OperacionTransporte(operador1, camion1, "Cobre", 5.2, 24.0, 15.5)
    if op1.validar_carga():
        op1.iniciar_transporte()
        print(operador1.registrar_operacion(op1))
        print(supervisor.registrar_operacion(op1))
        op1.finalizar_transporte()
        sistema.operaciones.append(op1)
        almacen.registrar_ingreso(op1, controlador)
        print(op1.generar_reporte())
    
    # OPERACIÓN 2: Oro
    print("\n--- OPERACIÓN 2: TRANSPORTE DE ORO ---")
    op2 = OperacionTransporte(operador2, camion2, "Oro", 3.8, 30.0, 22.0)
    if op2.validar_carga():
        op2.iniciar_transporte()
        print(operador2.registrar_operacion(op2))
        print(supervisor.registrar_operacion(op2))
        op2.finalizar_transporte()
        sistema.operaciones.append(op2)
        almacen.registrar_ingreso(op2, controlador)
        print(op2.generar_reporte())
    
    # OPERACIÓN 3: Plata
    print("\n--- OPERACIÓN 3: TRANSPORTE DE PLATA ---")
    op3 = OperacionTransporte(operador1, camion3, "Plata", 4.5, 9.5, 8.0)
    if op3.validar_carga():
        op3.iniciar_transporte()
        print(operador1.registrar_operacion(op3))
        print(supervisor.registrar_operacion(op3))
        op3.finalizar_transporte()
        sistema.operaciones.append(op3)
        almacen.registrar_ingreso(op3, controlador)
        print(op3.generar_reporte())
    
    # OPERACIÓN 4: Mineral Mixto (demostración de sobrepeso)
    print("\n--- OPERACIÓN 4: INTENTO DE SOBRECARGA ---")
    op4 = OperacionTransporte(operador2, camion3, "Mineral Mixto", 6.0, 15.0, 12.0)
    if not op4.validar_carga():
        print("❌ Operación rechazada por exceso de peso\n")
    
    # OPERACIÓN 5: Demostrar validación de setter de capacidad
    print("\n--- DEMOSTRACIÓN: VALIDACIÓN DE CAPACIDAD NEGATIVA ---")
    try:
        print(f"Capacidad actual de {camion3.id_vehiculo}: {camion3.capacidad_tn}tn")
        print("Intentando asignar capacidad negativa (-5.0)...")
        camion3.capacidad_tn = -5.0
    except ValueError as e:
        print(f"✓ Validación exitosa: {e}")
    
    # OPERACIÓN 6: Demostrar modificación válida de capacidad
    print("\n--- DEMOSTRACIÓN: MODIFICACIÓN VÁLIDA DE CAPACIDAD ---")
    try:
        print(f"Capacidad actual de {camion1.id_vehiculo}: {camion1.capacidad_tn}tn")
        print("Modificando capacidad a 30.0tn después de mejora técnica...")
        camion1.capacidad_tn = 30.0
        print(f"✓ Nueva capacidad: {camion1.capacidad_tn}tn")
    except ValueError as e:
        print(f"Error: {e}")
    
    # OPERACIÓN 7: Demostrar validación de peso en CargaMineral
    print("\n--- DEMOSTRACIÓN: VALIDACIÓN DE PESO NEGATIVO EN CARGA ---")
    try:
        print("Intentando crear carga con peso negativo...")
        carga_invalida = CargaMineral("Cobre", 5.0, -10.0)
        carga_invalida.peso_tn = -10.0
    except ValueError as e:
        print(f"✓ Validación exitosa: {e}")
    
    # 5. GENERAR REPORTES FINALES
    print("\n" + "="*70)
    print("REPORTES FINALES")
    print("="*70)
    
    print(almacen.obtener_reporte_mensual())
    print(sistema.generar_reporte_diario())
    
    # DEMOSTRACIÓN DE POLIMORFISMO
    print("\n" + "="*70)
    print("DEMOSTRACIÓN DE POLIMORFISMO")
    print("="*70)
    
    print("\n🔄 Cálculo de bonos (polimorfismo en calcular_bonos()):")
    for operador in sistema.operadores:
        print(f"  • {operador.nombre} ({operador.__class__.__name__}): S/.{operador.calcular_bonos():.2f}")
    
    print("\n🔄 Rendimiento de vehículos (polimorfismo en calcular_rendimiento()):")
    for op in sistema.operaciones:
        print(f"  • {op.vehiculo.id_vehiculo}: {op.calcular_rendimiento_operacion():.2f} unidades")
    
    print("\n✅ Sistema ejecutado exitosamente")
    print("="*70 + "\n")


# EJECUTAR EL ESCENARIO
if __name__ == "__main__":
    ejecutar_escenario()