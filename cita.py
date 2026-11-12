from datetime import datetime


class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self.codigo = codigo      # usa el setter (valida)
        self._paciente = paciente
        self._medico = medico
        self.fecha = fecha        # usa el setter (valida)

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    # Setters
    @codigo.setter
    def codigo(self, valor):
        if valor.strip() == "":
            raise ValueError("El código no puede estar vacío")
        self._codigo = valor

    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor

    @medico.setter
    def medico(self, valor):
        self._medico = valor

    @fecha.setter
    def fecha(self, valor):
        try:
            datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha debe ser válida y tener el formato dd/mm/aaaa")
        self._fecha = valor

    def resumen(self):
        return (f"{self._codigo} - Paciente: {self._paciente.nombre} "
                f"con el Dr. {self._medico.nombre} la fecha : {self._fecha}")

