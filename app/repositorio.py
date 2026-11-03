"""Abstracción y repositorio en memoria para las solicitudes."""

from typing import Protocol

from app.modelos import Solicitud


# DIP / bajo acoplamiento: este contrato describe las operaciones requeridas por
# el servicio. Otra implementación de almacenamiento podría cumplirlo sin cambiar
# la lógica de negocio. El proyecto actual incluye solo la implementación en memoria.
class RepositorioSolicitudes(Protocol):
    """Contrato que debe cumplir cualquier mecanismo de almacenamiento."""

    def agregar(self, solicitud: Solicitud) -> None: ...
    def buscar_por_id(self, identificador: int) -> Solicitud | None: ...
    def listar(self) -> list[Solicitud]: ...
    def siguiente_identificador(self) -> int: ...


# Move Method / reubicación de responsabilidad: las operaciones de almacenamiento
# y la generación de identificadores viven en el repositorio, no en la interfaz
# ni en el servicio de negocio. Los datos se pierden al cerrar la aplicación.
class RepositorioEnMemoria:
    """Implementación simple que conserva los datos durante la ejecución."""

    def __init__(self) -> None:
        self._solicitudes: dict[int, Solicitud] = {}
        self._proximo_id = 1

    def agregar(self, solicitud: Solicitud) -> None:
        # Evita sobrescribir silenciosamente una solicitud con el mismo ID.
        if solicitud.identificador in self._solicitudes:
            raise ValueError(f"Ya existe la solicitud {solicitud.identificador}.")
        self._solicitudes[solicitud.identificador] = solicitud
        self._proximo_id = max(self._proximo_id, solicitud.identificador + 1)

    def buscar_por_id(self, identificador: int) -> Solicitud | None:
        return self._solicitudes.get(identificador)

    def listar(self) -> list[Solicitud]:
        return list(self._solicitudes.values())

    def siguiente_identificador(self) -> int:
        identificador = self._proximo_id
        self._proximo_id += 1
        return identificador
