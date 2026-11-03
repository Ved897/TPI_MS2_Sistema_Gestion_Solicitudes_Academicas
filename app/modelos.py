"""Modelos y valores controlados del dominio."""

from dataclasses import dataclass
from enum import Enum


# Clean Code: las enumeraciones reemplazan cadenas mágicas y concentran los
# valores válidos en un único lugar (DT-05 de la versión inicial).
class Prioridad(str, Enum):
    ALTA = "ALTA"
    MEDIA = "MEDIA"
    BAJA = "BAJA"


class EstadoSolicitud(str, Enum):
    PENDIENTE = "PENDIENTE"
    EN_PROCESO = "EN_PROCESO"
    RESUELTA = "RESUELTA"


# Refactoring: Introduce Parameter Object. Agrupa los datos relacionados de
# una solicitud nueva y evita pasar muchos parámetros independientes.
@dataclass(frozen=True)
class DatosNuevaSolicitud:
    """Objeto de parámetros para registrar una solicitud."""

    titulo: str
    tipo: str
    prioridad: Prioridad
    responsable: str = ""


# Modelo de dominio explícito: reemplaza los diccionarios de la versión inicial
# por atributos con nombres y tipos claros (mejora de legibilidad y mantenimiento).
@dataclass
class Solicitud:
    identificador: int
    titulo: str
    tipo: str
    prioridad: Prioridad
    responsable: str = ""
    estado: EstadoSolicitud = EstadoSolicitud.PENDIENTE

    def como_diccionario(self) -> dict[str, object]:
        """Devuelve una representación simple para mostrar o serializar."""
        return {
            "id": self.identificador,
            "titulo": self.titulo,
            "tipo": self.tipo,
            "prioridad": self.prioridad.value,
            "responsable": self.responsable,
            "estado": self.estado.value,
        }
