from banco import Banco

if __name__ == "__main__":
    print("=== Registro de clientes ===")
    datos = []
    for i in range(1, 4):
        nombre = input(f"Nombre del cliente {i}: ")
        saldo = float(input(f"Saldo inicial de {nombre}: S/ "))
        datos.extend([nombre, saldo])

    banco = Banco(*datos)
    banco.operacion()
    banco.depositos()
