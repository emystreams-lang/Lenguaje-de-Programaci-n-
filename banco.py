from cliente import Cliente


class Banco:
    def __init__(self, nombre1, saldo1, nombre2, saldo2, nombre3, saldo3):
        self._cliente1 = Cliente(nombre1, saldo1)
        self._cliente2 = Cliente(nombre2, saldo2)
        self._cliente3 = Cliente(nombre3, saldo3)

    def operacion(self):
        print("\n=== RETIRAR DINERO ===")
        clientes = (self._cliente1, self._cliente2, self._cliente3)

        for cliente in clientes:
            print(f"\n-> Cliente actual: {cliente.nombre} | Saldo disponible: S/ {cliente.cantidad:.2f}")
            
            opcion = input(f"¿Deseas retirar dinero {cliente.nombre}? (si/no): ").strip().lower()

            if opcion == 'si':
                try:
                    monto = float(input(f"Ingrese el monto a retiar {cliente.nombre}: S/ "))
                    cliente.extraer(monto)
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número.")
            else:
                print(f"Operación omitida. No se realizó extracción para {cliente.nombre}.")

    def depositos(self):
        total = 0
        print("\n=== ESTADO FINAL DE SALDOS EN EL BANCO ===")
        for cliente in (self._cliente1, self._cliente2, self._cliente3):
            cliente.imprimir()
            total += cliente.devolver_cantidad()
        print("-" * 45)
        print(f"Total de dinero disponible en el banco: S/ {total:.2f}")
        print("-" * 45)
