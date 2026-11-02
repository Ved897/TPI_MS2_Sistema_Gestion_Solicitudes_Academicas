"""Repositorio de la versión inicial; se conserva para comparar el refactoring."""


class RepositorioSolicitudes:
    # DT-03: recibe y conserva una lista compartida, que puede ser la lista global.
    # DT-09: los registros se representan como diccionarios sin una estructura
    # de dominio que ayude a detectar errores en claves o tipos.
    def __init__(self, solicitudes=None):
        if solicitudes is None:
            solicitudes = []

        self.solicitudes = solicitudes

        self.siguiente_id = (
            max((solicitud["id"] for solicitud in self.solicitudes), default=0) + 1
        )

    # DT-06: esta búsqueda se invoca desde varias ramas del flujo principal.
    def buscar_por_id(self, numero):
        for solicitud in self.solicitudes:
            if solicitud["id"] == numero:
                return solicitud

        return None

    def agregar(self, solicitud):
        self.solicitudes.append(solicitud)

    def generar_id(self):
        identificador = self.siguiente_id
        self.siguiente_id += 1
        return identificador

    def listar(self):
        return self.solicitudes.copy()
