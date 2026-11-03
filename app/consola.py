"""Interfaz de consola: solicita entradas y presenta resultados."""

from app.modelos import DatosNuevaSolicitud, EstadoSolicitud, Prioridad
from app.repositorio import RepositorioEnMemoria
from app.servicio_solicitudes import ServicioSolicitudes


# Extract Method: concentra la lectura y validación de números enteros para
# que las operaciones no repitan el mismo manejo de entradas inválidas.
def _leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Ingrese un número entero válido.")


def _leer_enum(mensaje: str, enum_tipo):
    valor = input(mensaje).strip().upper()
    try:
        return enum_tipo(valor)
    except ValueError as error:
        opciones = ", ".join(item.value for item in enum_tipo)
        raise ValueError(f"Valor inválido. Opciones permitidas: {opciones}.") from error


def ejecutar() -> None:
    # La consola compone las dependencias y traduce las opciones del usuario en
    # casos de uso. El servicio conserva las reglas y el repositorio los datos.
    servicio = ServicioSolicitudes(RepositorioEnMemoria())
    acciones = {
        "1": lambda: _registrar(servicio),
        "2": lambda: _asignar(servicio),
        "3": lambda: _cambiar_estado(servicio),
        "4": lambda: _consultar(servicio),
        "5": lambda: _mostrar_reporte(servicio),
        "6": lambda: _listar(servicio),
    }

    while True:
        print("\nSISTEMA DE GESTIÓN DE SOLICITUDES ACADÉMICAS")
        print("1. Registrar solicitud\n2. Asignar responsable\n3. Cambiar estado")
        print(
            "4. Consultar solicitud\n5. Generar reporte\n6. Listar solicitudes\n0. Salir"
        )
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            print("Programa finalizado.")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida.")
            continue
        try:
            accion()
        except (ValueError, LookupError) as error:
            print(f"No se pudo completar la operación: {error}")


# Extract Method: cada acción tiene una función pequeña con un propósito claro.
def _registrar(servicio: ServicioSolicitudes) -> None:
    datos = DatosNuevaSolicitud(
        titulo=input("Título: "),
        tipo=input("Tipo: "),
        prioridad=_leer_enum("Prioridad (ALTA/MEDIA/BAJA): ", Prioridad),
        responsable=input("Responsable (opcional): "),
    )
    solicitud = servicio.registrar(datos)
    print(f"Solicitud registrada con ID {solicitud.identificador}.")


def _asignar(servicio: ServicioSolicitudes) -> None:
    identificador = _leer_entero("ID de solicitud: ")
    responsable = input("Responsable: ")
    servicio.asignar_responsable(identificador, responsable)
    print("Responsable asignado.")


def _cambiar_estado(servicio: ServicioSolicitudes) -> None:
    identificador = _leer_entero("ID de solicitud: ")
    estado = _leer_enum("Estado (PENDIENTE/EN_PROCESO/RESUELTA): ", EstadoSolicitud)
    servicio.cambiar_estado(identificador, estado)
    print("Estado actualizado.")


def _consultar(servicio: ServicioSolicitudes) -> None:
    solicitud = servicio.consultar(_leer_entero("ID de solicitud: "))
    print(solicitud.como_diccionario())


def _mostrar_reporte(servicio: ServicioSolicitudes) -> None:
    reporte = servicio.generar_reporte()
    print(" | ".join(f"{estado}: {cantidad}" for estado, cantidad in reporte.items()))


def _listar(servicio: ServicioSolicitudes) -> None:
    solicitudes = servicio.listar()
    if not solicitudes:
        print("No hay solicitudes registradas.")
        return
    for solicitud in solicitudes:
        print(solicitud.como_diccionario())


if __name__ == "__main__":
    ejecutar()
