class Atencion:
    def __init__(self, cita, diagnostico, tratamiento):
        self._cita = cita
        self.diagnostico = diagnostico    # usa el setter (valida)
        self.tratamiento = tratamiento    # usa el setter (valida)

    # Getters
    @property
    def cita(self):
        return self._cita

    @property
    def diagnostico(self):
        return self._diagnostico

    @property
    def tratamiento(self):
        return self._tratamiento

    # Setters (validan que el campo no esté vacío)
    @diagnostico.setter
    def diagnostico(self, valor):
        if valor.strip() == "":
            raise ValueError("El diagnóstico no puede estar vacío")
        self._diagnostico = valor

    @tratamiento.setter
    def tratamiento(self, valor):
        if valor.strip() == "":
            raise ValueError("El tratamiento no puede estar vacío")
        self._tratamiento = valor

    def resumen(self):
        return (f"Cita {self._cita.codigo} - Diagnóstico: {self._diagnostico} "
                f"- Tratamiento: {self._tratamiento}")

