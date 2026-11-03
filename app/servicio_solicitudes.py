"""Casos de uso del sistema, separados de la interfaz de consola."""

from collections import Counter

from app.modelos import DatosNuevaSolicitud, EstadoSolicitud, Prioridad, Solicitud
from app.repositorio import RepositorioSolicitudes


class SolicitudNoEncontradaError(LookupError):
    """Se produce cuando no existe una solicitud con el identificador dado."""


class ServicioSolicitudes:
    """Coordina los casos de uso y aplica reglas del dominio.

    SRP: no solicita datos ni imprime mensajes; esas tareas corresponden a consola.py.
    DIP: recibe el contrato del repositorio en el constructor.
    """

    def __init__(self, repositorio: RepositorioSolicitudes) -> None:
        # DIP: el servicio depende del contrato del repositorio, no de su clase concreta.
        self._repositorio = repositorio

    def registrar(self, datos: DatosNuevaSolicitud) -> Solicitud:
        # Introduce Parameter Object: el caso de uso recibe un único objeto con
        # los datos relacionados, en vez de varios argumentos independientes.
        # Validar y normalizar aquí mantiene las reglas de negocio fuera de la UI.
        titulo = datos.titulo.strip()
        tipo = datos.tipo.strip()
        if not titulo:
            raise ValueError("El título es obligatorio.")
        if not tipo:
            raise ValueError("El tipo de solicitud es obligatorio.")
        if not isinstance(datos.prioridad, Prioridad):
            raise TypeError("La prioridad debe ser ALTA, MEDIA o BAJA.")

        solicitud = Solicitud(
            identificador=self._repositorio.siguiente_identificador(),
            titulo=titulo,
            tipo=tipo,
            prioridad=datos.prioridad,
            responsable=datos.responsable.strip(),
        )
        self._repositorio.agregar(solicitud)
        return solicitud

    def asignar_responsable(self, identificador: int, responsable: str) -> Solicitud:
        solicitud = self._obtener_existente(identificador)
        nombre = responsable.strip()
        if not nombre:
            raise ValueError("El responsable es obligatorio.")
        solicitud.responsable = nombre
        return solicitud

    def cambiar_estado(self, identificador: int, estado: EstadoSolicitud) -> Solicitud:
        solicitud = self._obtener_existente(identificador)
        if not isinstance(estado, EstadoSolicitud):
            raise TypeError("El estado indicado no es válido.")
        solicitud.estado = estado
        return solicitud

    def consultar(self, identificador: int) -> Solicitud:
        return self._obtener_existente(identificador)

    def listar(self) -> list[Solicitud]:
        return sorted(
            self._repositorio.listar(), key=lambda solicitud: solicitud.identificador
        )

    def generar_reporte(self) -> dict[str, int]:
        conteo = Counter(solicitud.estado for solicitud in self._repositorio.listar())
        return {estado.value: conteo.get(estado, 0) for estado in EstadoSolicitud}

    # Extract Method / evitar duplicación: asignar, cambiar estado y consultar
    # reutilizan esta comprobación en lugar de repetir la búsqueda y el error.
    def _obtener_existente(self, identificador: int) -> Solicitud:
        solicitud = self._repositorio.buscar_por_id(identificador)
        if solicitud is None:
            raise SolicitudNoEncontradaError(
                f"No se encontró la solicitud con ID {identificador}."
            )
        return solicitud
