from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion

pacientes = {}    # código -> Paciente
medicos = {}      # código -> Medico
citas = {}        # código -> Cita
historial = []    # lista de objetos Atencion


def convertir_edad(texto):
    """Convierte el texto a número entero; si no es número lanza ValueError."""
    try:
        return int(texto)
    except ValueError:
        raise ValueError("La edad debe ser un número entero")


def ocultar_nombre(nombre):
    """Deja solo la primera letra de cada palabra: Juan Torres -> J*** T*****"""
    ocultas = []
    for parte in nombre.split():
        ocultas.append(parte[0] + "*" * (len(parte) - 1))
    return " ".join(ocultas)


# RF03 - Buscar por código (paciente, médico o cita)
def buscar_por_codigo(codigo):
    if codigo in pacientes:
        return pacientes[codigo]
    if codigo in medicos:
        return medicos[codigo]
    if codigo in citas:
        return citas[codigo]
    return None


def crear_persona(tipo, codigo, nombre, dato):
    """Crea un Paciente (dato = edad) o un Medico (dato = especialidad)."""
    if buscar_por_codigo(codigo) is not None:
        raise ValueError("El código ya existe")
    if tipo == "paciente":
        nuevo = Paciente(codigo, nombre, dato)
        pacientes[codigo] = nuevo
    elif tipo == "medico":
        nuevo = Medico(codigo, nombre, dato)
        medicos[codigo] = nuevo
    else:
        raise ValueError("Tipo de persona no válido")
    return nuevo


# RF01 - Registrar paciente
def registrar_paciente(codigo, nombre, edad_texto):
    edad = convertir_edad(edad_texto)
    return crear_persona("paciente", codigo, nombre, edad)


# RF02 - Registrar médico
def registrar_medico(codigo, nombre, especialidad):
    return crear_persona("medico", codigo, nombre, especialidad)


# RF04 - Programar cita
def programar_cita(codigo, cod_paciente, cod_medico, fecha):
    if buscar_por_codigo(codigo) is not None:
        raise ValueError("El código ya existe")
    if cod_paciente not in pacientes:
        raise ValueError("El paciente no existe")
    if cod_medico not in medicos:
        raise ValueError("El médico no existe")
    nueva = Cita(codigo, pacientes[cod_paciente], medicos[cod_medico], fecha)
    citas[codigo] = nueva
    return nueva


# RF05 - Registrar atención (se añade al historial)
def registrar_atencion(cod_cita, diagnostico, tratamiento):
    if cod_cita not in citas:
        raise ValueError("La cita no existe")
    if atencion_de_cita(cod_cita) is not None:
        raise ValueError("La cita ya fue atendida")
    nueva = Atencion(citas[cod_cita], diagnostico, tratamiento)
    historial.append(nueva)
    return nueva


# Consultas
def atencion_de_cita(cod_cita):
    for atencion in historial:
        if atencion.cita.codigo == cod_cita:
            return atencion
    return None


def citas_de_paciente(cod_paciente):
    resultado = []
    for cita in citas.values():
        if cita.paciente.codigo == cod_paciente:
            resultado.append(cita)
    return resultado


def historial_de_paciente(cod_paciente):
    resultado = []
    for atencion in historial:
        if atencion.cita.paciente.codigo == cod_paciente:
            resultado.append(atencion)
    return resultado


# Paradigma funcional: filter() con lambda, sin modificar la colección
def buscar_por_especialidad(especialidad):
    buscada = especialidad.strip().lower()
    return list(filter(lambda m: m.especialidad.lower() == buscada, medicos.values()))


def cargar_datos_prueba():
    crear_persona("paciente", "P001", "Juan Torres", 22)
    crear_persona("paciente", "P002", "María Quispe", 35)
    crear_persona("paciente", "P003", "Luis Ramos", 19)
    crear_persona("medico", "M001", "Alex Rojas", "cardiología")
    crear_persona("medico", "M002", "Carlos Mendoza", "pediatría")
    crear_persona("medico", "M003", "Raúl Vega", "medicina general")
    crear_persona("medico", "M004", "Diego Salas", "medicina general")
    programar_cita("C001", "P001", "M001", "05/11/2026")
    programar_cita("C002", "P002", "M002", "06/11/2026")
    programar_cita("C003", "P003", "M003", "07/11/2026")
    registrar_atencion("C001", "Control general", "Reposo e hidratación")

