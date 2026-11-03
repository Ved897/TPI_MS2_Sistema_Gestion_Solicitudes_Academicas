from app import consola
from app.modelos import EstadoSolicitud, Prioridad
from app.repositorio import RepositorioEnMemoria
from app.servicio_solicitudes import ServicioSolicitudes


def preparar(monkeypatch, entradas):
    valores = iter(entradas)
    monkeypatch.setattr("builtins.input", lambda _mensaje="": next(valores))


def test_leer_entero_reintenta_entrada_invalida(monkeypatch):
    preparar(monkeypatch, ["abc", "12"])
    assert consola._leer_entero("Número: ") == 12


def test_leer_enum_rechaza_valor_invalido():
    from unittest.mock import patch

    with patch("builtins.input", return_value="urgente"):
        try:
            consola._leer_enum("Prioridad: ", Prioridad)
        except ValueError as error:
            assert "ALTA, MEDIA, BAJA" in str(error)
        else:
            raise AssertionError("Se esperaba ValueError")


def test_ejecutar_salida(monkeypatch, capsys):
    preparar(monkeypatch, ["0"])
    consola.ejecutar()
    assert "Programa finalizado" in capsys.readouterr().out


def test_ejecutar_opcion_invalida(monkeypatch, capsys):
    preparar(monkeypatch, ["77", "0"])
    consola.ejecutar()
    assert "Opción inválida" in capsys.readouterr().out


def test_ejecutar_registro_y_listado(monkeypatch, capsys):
    preparar(
        monkeypatch,
        [
            "1",
            "Constancia de estudio",
            "CERTIFICADO",
            "ALTA",
            "Secretaría",
            "6",
            "0",
        ],
    )
    consola.ejecutar()
    salida = capsys.readouterr().out
    assert "Solicitud registrada con ID 1" in salida
    assert "Constancia de estudio" in salida


def test_ejecutar_error_de_validacion_controlado(monkeypatch, capsys):
    preparar(monkeypatch, ["1", "", "CERTIFICADO", "ALTA", "", "0"])
    consola.ejecutar()
    assert "El título es obligatorio" in capsys.readouterr().out


def test_acciones_servicio_en_consola(monkeypatch, capsys):
    servicio = ServicioSolicitudes(RepositorioEnMemoria())
    monkeypatch.setattr("builtins.input", lambda _mensaje="": "Solicitud de prueba")
    # Las funciones específicas se prueban con entradas controladas por cada llamada.
    entradas = iter(["Solicitud de prueba", "CERTIFICADO", "MEDIA", "Área académica"])
    monkeypatch.setattr("builtins.input", lambda _mensaje="": next(entradas))
    consola._registrar(servicio)
    assert "ID 1" in capsys.readouterr().out

    entradas = iter(["1", "Área de alumnos"])
    monkeypatch.setattr("builtins.input", lambda _mensaje="": next(entradas))
    consola._asignar(servicio)
    assert servicio.consultar(1).responsable == "Área de alumnos"

    entradas = iter(["1", "RESUELTA"])
    monkeypatch.setattr("builtins.input", lambda _mensaje="": next(entradas))
    consola._cambiar_estado(servicio)
    assert servicio.consultar(1).estado is EstadoSolicitud.RESUELTA

    monkeypatch.setattr("builtins.input", lambda _mensaje="": "1")
    consola._consultar(servicio)
    assert "Solicitud de prueba" in capsys.readouterr().out


def test_reporte_y_lista_vacia(capsys):
    servicio = ServicioSolicitudes(RepositorioEnMemoria())
    consola._mostrar_reporte(servicio)
    consola._listar(servicio)
    salida = capsys.readouterr().out
    assert "PENDIENTE: 0" in salida
    assert "No hay solicitudes registradas" in salida
