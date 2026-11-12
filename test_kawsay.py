import pytest
import funciones as f


@pytest.fixture(autouse=True)
def datos_limpios():
    """Antes de cada prueba se vacían las colecciones."""
    f.pacientes.clear()
    f.medicos.clear()
    f.citas.clear()
    f.historial.clear()


def preparar():
    f.registrar_paciente("P001", "Juan Torres", "22")
    f.registrar_medico("M001", "Alex Rojas", "cardiología")


def test_normal():
    preparar()
    cita = f.programar_cita("C001", "P001", "M001", "05/11/2026")
    assert f.buscar_por_codigo("C001") is cita
    f.registrar_atencion("C001", "Gripe", "Reposo")
    assert len(f.historial_de_paciente("P001")) == 1


def test_extremo_edad_0_y_120():
    f.registrar_paciente("P010", "Ana Diaz", "0")
    f.registrar_paciente("P011", "Luis Paz", "120")
    assert f.pacientes["P010"].edad == 0
    assert f.pacientes["P011"].edad == 120


def test_extremo_fuera_de_rango():
    with pytest.raises(ValueError, match="entre 0 y 120"):
        f.registrar_paciente("P012", "Eva Ruiz", "-1")
    with pytest.raises(ValueError, match="entre 0 y 120"):
        f.registrar_paciente("P013", "Pedro Gil", "121")
    assert len(f.pacientes) == 0


def test_error_edad_no_numerica():
    with pytest.raises(ValueError, match="número entero"):
        f.registrar_paciente("P002", "Ana Diaz", "abc")
    assert len(f.pacientes) == 0


def test_duplicado():
    preparar()
    with pytest.raises(ValueError, match="ya existe"):
        f.registrar_paciente("P001", "Otro Nombre", "30")
    assert len(f.pacientes) == 1


def test_referencia_invalida():
    preparar()
    with pytest.raises(ValueError, match="paciente no existe"):
        f.programar_cita("C002", "P999", "M001", "06/11/2026")
    assert len(f.citas) == 0


def test_medico_sin_especialidad():
    with pytest.raises(ValueError, match="especialidad"):
        f.registrar_medico("M002", "Rosa Vega", "")
    assert len(f.medicos) == 0


def test_fecha_invalida():
    preparar()
    with pytest.raises(ValueError, match="fecha"):
        f.programar_cita("C003", "P001", "M001", "31/02/2026")


def test_cita_ya_atendida():
    preparar()
    f.programar_cita("C001", "P001", "M001", "05/11/2026")
    f.registrar_atencion("C001", "Gripe", "Reposo")
    with pytest.raises(ValueError, match="ya fue atendida"):
        f.registrar_atencion("C001", "Otra", "Otra")


def test_atencion_cita_inexistente():
    preparar()
    with pytest.raises(ValueError, match="cita no existe"):
        f.registrar_atencion("C999", "Gripe", "Reposo")
    assert len(f.historial) == 0


def test_historial_sin_atenciones():
    preparar()
    assert f.historial_de_paciente("P001") == []


def test_buscar_por_especialidad():
    preparar()
    assert len(f.buscar_por_especialidad("Cardiología")) == 1
    assert f.buscar_por_especialidad("neurología") == []


def test_buscar_por_codigo():
    preparar()
    assert f.buscar_por_codigo("P001").nombre == "Juan Torres"
    assert f.buscar_por_codigo("P999") is None


def test_ocultar_nombre():
    assert f.ocultar_nombre("Juan Torres") == "J*** T*****"

