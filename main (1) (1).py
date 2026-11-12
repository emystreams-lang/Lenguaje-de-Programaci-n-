from paciente import Paciente
from medico import Medico
from cita import Cita 

p_01 = Paciente ("P001", "Juan Torres" , 22)
m_01 = Medico("M001","Alex Rojas", "cardiología")
c_01 = Cita ("C001", p_01, m_01,"05/11/2026")

print(p_01. resumen())
print(m_01. resumen())
print(c_01. resumen())
