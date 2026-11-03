import pytest

from app.repositorio import RepositorioEnMemoria
from app.servicio_solicitudes import ServicioSolicitudes


@pytest.fixture
def servicio():
    return ServicioSolicitudes(RepositorioEnMemoria())
