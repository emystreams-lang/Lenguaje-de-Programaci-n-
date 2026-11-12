class Paciente:
    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo      # usa el setter (valida)
        self.nombre = nombre      # usa el setter (valida)
        self.edad = edad          # usa el setter (valida)

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

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

    @edad.setter
    def edad(self, valor):
        if valor < 0 or valor > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        self._edad = valor

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._edad}"

