# Sistema de Gestión de Solicitudes Académicas

Trabajo Práctico Integrador de Metodología de Sistemas II, Tecnicatura Universitaria en Programación a Distancia (UTN).

| Dato | Detalle |
| --- | --- |
| Integrantes | Claria, Carolina Rocio (Comision 7); Diaz, Natalia Ayelen (Comision 7); Diaz, Veronica Evangelina (Comision 4)|
| Fecha final de entrega | 8 de noviembre de 2026 |
| Video de defensa | El enlace correspondiente al video explicativo será incluido en el informe PDF |

## 1. Objetivo

Registrar y administrar solicitudes académicas en una aplicación de consola, utilizando el caso para analizar calidad interna, deuda técnica, principios SOLID, Clean Code, refactoring seguro y revisión técnica.

## 2. Funcionalidades

- Registrar una solicitud con título, tipo, prioridad y responsable opcional.
- Asignar un responsable.
- Cambiar el estado a `PENDIENTE`, `EN_PROCESO` o `RESUELTA`.
- Consultar una solicitud por identificador.
- Listar solicitudes.
- Generar un reporte por estado.
- Validar datos de entrada y comunicar errores de forma controlada.

Los datos se guardan en memoria y se pierden al cerrar la aplicación. Esto simula un repositorio para el alcance del TPI y no es persistencia permanente.

## 3. Tecnologías

- Python 3.10 o superior
- pytest y pytest-cov
- Git y GitHub

## 4. Instalación y ejecución

Desde la carpeta raíz, crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo (en Windows PowerShell: `.venv\Scripts\Activate.ps1`; en Linux o Mac: `source .venv/bin/activate`) y ejecutar:

```bash
python -m pip install -r requirements.txt
python -m app
```

Para ejecutar la versión inicial, usada como base de comparación:

```bash
cd version_inicial
python -m app.sistema_original
```

## 5. Pruebas

```bash
python -m pytest -v
python -m pytest --cov=app --cov-branch --cov-report=term-missing
```

La salida de la ejecución de las pruebas está en `docs/evidencias/pytest.txt`.

## 6. Estructura del proyecto

```text
app/                       # versión mejorada
  modelos.py               # entidades, enumeraciones y objeto de parámetros
  repositorio.py           # contrato de repositorio e implementación en memoria
  servicio_solicitudes.py  # reglas de negocio y casos de uso
  consola.py               # interfaz de usuario
  __main__.py              # punto de entrada
version_inicial/           # código base original, para comparar
tests/                     # pruebas automatizadas
docs/                      # diagnóstico, comparación, decisiones, code review y evidencias
```

## 7. Decisiones principales de diseño

- SRP: la consola, las reglas de negocio, los modelos y el almacenamiento están en módulos distintos.
- DIP: `ServicioSolicitudes` recibe un repositorio a través de su contrato, en vez de crear una implementación concreta.
- Introduce Parameter Object: `DatosNuevaSolicitud` agrupa los datos para registrar una solicitud.
- Move Method: las operaciones de almacenamiento están en el repositorio y las reglas de negocio en el servicio.
- Extract Method: la consola delega cada operación en una función específica.
- Enumeraciones para prioridades y estados, en lugar de cadenas dispersas.
- Errores explícitos: los datos inválidos producen `ValueError` y un identificador inexistente produce `SolicitudNoEncontradaError`.

No todos los principios SOLID se aplican por igual: OCP e ISP se aplican de forma parcial y LSP no aplica, porque no hay jerarquías de herencia.

## 8. Comparación antes/después

La carpeta `version_inicial/app/` conserva el prototipo original y `app/` contiene la versión refactorizada. Las operaciones visibles se mantienen, con mensajes más claros y validación de entradas más controlada. Ver `docs/diagnostico.md`, `docs/comparacion_antes_despues.md` y `docs/decisiones_tecnicas.md`.

## 9. Git y tags

| Tag | Hito |
| --- | --- |
| `estado-inicial` | Sistema base |
| `etapa-diagnostico` | Diagnóstico y code smells |
| `etapa-refactoring` | Versión refactorizada |
| `etapa-pruebas` | Pruebas y evidencias |
| `etapa-docs` | Documentación y code review |
| `estado-refactorizado` | Estado final del código |

Para verificarlos:

```bash
git tag -n
git log --oneline --decorate
```
