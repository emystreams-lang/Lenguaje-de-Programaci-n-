class Medico:
    def __init__(self, codigo, nombre, especialidad):
        self._codigo=codigo 
        self._nombre = nombre 
        self._especialidad= especialidad 

    #Getters 
    @property 
    def codigo (self):
        return self._codigo 
    @property 
    def nombre (self):
        return self._nombre 
    @property 
    def especialidad  (self):
        return self._especialidad
    

    #Setters 
    @codigo.setter
    def codigo(self, valor):
        self._codigo=valor 
    @nombre.setter
    def nombre (self, valor):
        self.nombre=valor 
    @especialidad.setter
    def especialidad (self, valor):
        self._especialidad=valor 

    def resumen (self):
        return f"{self._codigo} - Dr. {self._nombre} con la especialidad {self._especialidad}"
class Cita:
    def __init__(self, codigo, paciente, medico, fecha ):
        self._codigo =codigo 
        self._paciente = paciente 
        self._medico =medico 
        self._fecha = fecha 
    # Getters
    @property
    def codigo(self):
        return self._codigo
     
    @property
    def paciente (self):
        return self._paciente
     
    @property
    def medico (self):
        return self._medico 
     
    @property
    def fecha (self):
        return self._fecha  

    # Setters
    @codigo.setter
    def codigo (self, valor):
        self._paciente=valor 

    @paciente.setter
    def paciente (self, valor):
        self._paciente=valor 

    @medico.setter
    def medico (self, valor):
        self._medico=valor 

    @fecha .setter
    def fecha  (self, valor):
        self._fecha=valor 

    def resumen (self):
        return f"{self ._codigo} - Paciente: {self._paciente.nombre} con el Dr. {self._medico.nombre} la fecha : {self._fecha}"
class Paciente:
    def __init__(self, codigo,nombre, edad):
        self._codigo =codigo 
        self._nombre= nombre
        self._edad= edad

    #Getters
    @property
    def codigo (self):
        return self._codigo
    @property
    def nombre (self):
        return self._nombre
    @property
    def edad (self):
        return self._edad

    #Setter
    @codigo.setter
    def codigo (self, valor):
        self._codigo=valor 
    @nombre.setter
    def nombre (self, valor):
        self._nombre=valor 
    @edad.setter
    def edad (self, valor):
        self._edad=valor

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._edad}"

p_01 = Paciente ("P001", "Juan Torres" , 22)
m_01 = Medico("M001","Alex Rojas", "cardiología")
c_01 = Cita ("C001", p_01, m_01,"05/11/2026")

print(p_01. resumen())
print(m_01. resumen())
print(c_01. resumen())
