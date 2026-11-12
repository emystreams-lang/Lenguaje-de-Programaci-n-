from funciones import *
def mostrar_menu():
    print("\n===== SISTEMA KAWSAY =====")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Buscar por código")
    print("4. Programar cita")
    print("5. Registrar atención")
    print("6. Consultar historial de un paciente")
    print("7. Buscar médicos por especialidad")
    print("0. Salir")


def buscar_y_mostrar(codigo):
    objeto = buscar_por_codigo(codigo)
    if objeto is None:
        print("No se encontró el código.")
        return
    print(objeto.resumen())
    if codigo in pacientes:
        for cita in citas_de_paciente(codigo):
            print("  Cita:", cita.resumen())
            atencion = atencion_de_cita(cita.codigo)
            if atencion is not None:
                print("    Atención:", atencion.resumen())
    elif codigo in citas:
        if atencion_de_cita(codigo) is None:
            print("  Estado: pendiente de atención.")
        else:
            print("  Estado: atendida.")


def main():
    cargar_datos_prueba()
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        try:
            if opcion == "1":
                codigo = input("Código del paciente (ejemplo P004): ")
                nombre = input("Nombre del paciente: ")
                edad = input("Edad: ")
                registrar_paciente(codigo, nombre, edad)
                print("Paciente registrado correctamente.")

            elif opcion == "2":
                codigo = input("Código del médico (ejemplo M005): ")
                nombre = input("Nombre del médico: ")
                especialidad = input("Especialidad: ")
                registrar_medico(codigo, nombre, especialidad)
                print("Médico registrado correctamente.")

            elif opcion == "3":
                codigo = input("Código a buscar (P001, M001 o C001): ")
                buscar_y_mostrar(codigo)

            elif opcion == "4":
                codigo = input("Código de la cita (ejemplo C004): ")
                cod_paciente = input("Código del paciente: ")
                cod_medico = input("Código del médico: ")
                fecha = input("Fecha (dd/mm/aaaa): ")
                programar_cita(codigo, cod_paciente, cod_medico, fecha)
                print("Cita programada correctamente.")

            elif opcion == "5":
                cod_cita = input("Código de la cita: ")
                diagnostico = input("Diagnóstico (ficticio): ")
                tratamiento = input("Tratamiento (ficticio): ")
                registrar_atencion(cod_cita, diagnostico, tratamiento)
                print("Atención registrada correctamente.")

            elif opcion == "6":
                cod_paciente = input("Código del paciente: ")
                if cod_paciente not in pacientes:
                    raise ValueError("El paciente no existe")
                lista = historial_de_paciente(cod_paciente)
                if len(lista) == 0:
                    print("El paciente no tiene atenciones registradas.")
                for atencion in lista:
                    paciente = atencion.cita.paciente
                    print(ocultar_nombre(paciente.nombre), "-", atencion.resumen())

            elif opcion == "7":
                especialidad = input("Especialidad: ")
                lista = buscar_por_especialidad(especialidad)
                if len(lista) == 0:
                    print("No hay médicos con esa especialidad.")
                for medico in lista:
                    print(medico.resumen())

            elif opcion == "0":
                print("Saliendo del Sistema Kawsay...")

            else:
                print("Opción no válida.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

