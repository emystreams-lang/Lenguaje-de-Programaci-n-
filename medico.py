class Medico:
    def __init__(self, codigo, nombre, especialidad):
        self.codigo = codigo              
        self.nombre = nombre              
        self.especialidad = especialidad  

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def especialidad(self):
        return self._especialidad

    # Setters (validan el dato antes de guardarlo)
    @codigo.setter
    def codigo(self, valor):
        if valor.strip() == "":
            raise ValueError("El código no puede estar vacío")
        self._codigo = valor

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @especialidad.setter
    def especialidad(self, valor):
        if valor.strip() == "":
            raise ValueError("La especialidad no puede estar vacía")
        self._especialidad = valor

    def resumen(self):
        return f"{self._codigo} - Dr. {self._nombre} con la especialidad {self._especialidad}"

