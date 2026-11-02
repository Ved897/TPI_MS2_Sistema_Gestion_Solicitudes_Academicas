# Sistema de Gestión de Solicitudes Académicas

**Trabajo Práctico Integrador — Metodología de Sistemas II**
Tecnicatura Universitaria en Programación

> Plantilla académica mejorada. Antes de entregar, completar integrantes, comisión, fecha, enlace al repositorio y evidencias reales de ejecución.

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

Los datos se guardan **en memoria** y se pierden al cerrar la aplicación. Esto simula un repositorio para el alcance del TPI; no es persistencia permanente.

## 3. Tecnologías

- Python 3.10 o superior
- pytest y pytest-cov
- Git y GitHub

## 4. Instalación y ejecución

Desde la carpeta raíz:

```bash
python -m venv .venv
```

Activar el entorno virtual y ejecutar:

```bash
python -m pip install -r requirements.txt
python -m app
```

En Windows PowerShell, la activación suele realizarse con:

```powershell
.venv\Scripts\Activate.ps1

```

## 5. Ejecutar las pruebas

```bash
python -m pytest -v
python -m pytest --cov=app --cov-branch --cov-report=term-missing
python -m pytest --cov=app --cov-report=term-missing

type nul > pyproject.toml
type nul > .gitignore
```

No incluir porcentajes de cobertura en el informe hasta ejecutar el comando en la versión final y guardar la salida como evidencia.

## 6. Estructura del proyecto

```text
app/
  modelos.py                 # Entidades, enumeraciones y objeto de parámetros
  repositorio.py             # Contrato de repositorio e implementación en memoria
  servicio_solicitudes.py    # Reglas de negocio y casos de uso
  consola.py                 # Interfaz de usuario
  __main__.py                # Punto de entrada
version_inicial/             # Código base original recibido para comparación
 tests/                      # Pruebas automatizadas
 docs/                       # Diagnóstico, decisiones, revisión y evidencias
```

## 7. Decisiones principales de diseño

- **SRP:** la consola, las reglas de negocio, los modelos y el almacenamiento se separan en módulos distintos.
- **DIP:** `ServicioSolicitudes` recibe un repositorio a través de su contrato, en vez de crear una implementación concreta internamente.
- **Introduce Parameter Object:** `DatosNuevaSolicitud` agrupa los datos necesarios para registrar una solicitud.
- **Move Method / reubicación de responsabilidad:** las operaciones de almacenamiento están en el repositorio y las reglas de negocio en el servicio.
- **Extract Method:** la interfaz de consola delega cada operación en una función específica.
- **Nombres y valores explícitos:** se usan `Enum` para prioridades y estados en lugar de cadenas dispersas.
- **Errores explícitos:** los datos inválidos producen `ValueError` y la consulta de un identificador inexistente produce `SolicitudNoEncontradaError`.

No se afirma que todos los principios SOLID se apliquen por igual: LSP, OCP e ISP deben evaluarse según el alcance real y no forzarse sin una necesidad de diseño.

## 8. Comparación antes/después

- **Base:** `version_inicial/app/` conserva los archivos del prototipo recibido.
- **Mejorada:** `app/` contiene la separación por responsabilidades y las pruebas.
- **Comportamiento esperado:** las operaciones visibles se mantienen; la validación de entradas y los mensajes de error son más controlados.

Consultar `docs/diagnostico.md` y `docs/comparacion_antes_despues.md`.

## 9. Git y etiquetas requeridas por la cátedra

El ZIP no puede demostrar por sí solo el historial ni los tags del repositorio. Una vez creado el repositorio Git, registrar commits reales y crear las etiquetas sobre los commits correctos:

```bash





```

Reemplazar los marcadores por hashes reales. No crear todos los tags apuntando al mismo commit si representan hitos diferentes. Si el repositorio ya está publicado, comprobar los tags con `git tag -n` y el historial con `git log --oneline --decorate`.

## 10. Antes de entregar

- [ ] Completar los datos de la portada y README.
- [ ] Ejecutar todas las pruebas y conservar la salida real.
- [ ] Completar las evidencias en `docs/evidencias/`.
- [ ] Verificar el comportamiento manualmente antes/después.
- [ ] Crear los tags requeridos en GitHub.
- [ ] Agregar el enlace al repositorio y al video.
- [ ] Declarar el uso real de herramientas de IA y adjuntar las interacciones relevantes.
- [ ] Confirmar que cada integrante puede explicar el código y sus decisiones.