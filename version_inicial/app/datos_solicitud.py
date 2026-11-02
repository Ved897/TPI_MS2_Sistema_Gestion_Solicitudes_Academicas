"""Objeto de datos de la versión inicial, mantenido como referencia histórica."""

from dataclasses import dataclass

# import dataclass: importa el decorador dataclass, que permite crear clases destinadas principalmente a almacenar datos


@dataclass
class DatosSolicitud:
    titulo: str
    tipo: str
    # En la versión inicial prioridad es una cadena libre; la versión mejorada
    # utiliza la enumeración Prioridad para limitar los valores admitidos.
    prioridad: str
    responsable: str = ""
