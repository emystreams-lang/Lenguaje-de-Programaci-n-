class Cliente:
    def __init__(self, nombre, cantidad=0):
        self._nombre = nombre
        self._cantidad = cantidad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor >= 0:
            self._cantidad = valor
        else:
            print("El saldo no puede ser negativo.")

    def depositar(self, monto):
        if monto > 0:
            self._cantidad += monto
            print(f"[DEPÓSITO] {self._nombre} depositó: S/ {monto:.2f}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def extraer(self, monto):
        if monto <= 0:
            print("El monto a extraer debe ser mayor que cero.")
        elif monto > self._cantidad:
            print(f"[RETIRO FALLIDO] {self._nombre}: fondos insuficientes para extraer S/ {monto:.2f}.")
        else:
            self._cantidad -= monto
            print(f"[EXTRACCIÓN EXITOSA] {self._nombre} extrajo: S/ {monto:.2f}")

    def devolver_cantidad(self):
        return self._cantidad

    def imprimir(self):
        print(f"Cliente: {self._nombre:<12} | Saldo actual: S/ {self._cantidad:.2f}")
