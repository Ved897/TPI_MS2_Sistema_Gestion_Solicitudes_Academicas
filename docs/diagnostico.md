# Diagnóstico de calidad interna y externa

## Alcance y evidencia

Se toma como versión base el prototipo ubicado en `version_inicial/app/sistema_original.py`. La revisión del código permite observar las debilidades descritas abajo. Para la entrega final, agregar capturas con el archivo y las líneas visibles o referencias `archivo:línea` comprobadas en el editor.

## Calidad externa e interna

**Calidad externa:** el usuario puede registrar, asignar responsable, cambiar estado, consultar y listar solicitudes, y obtener un reporte por estado.

**Calidad interna:** la versión base concentra operaciones distintas en una función `procesar()`, usa una lista global, transmite datos mediante muchos parámetros y repite la búsqueda de solicitudes en varias ramas. Estas decisiones hacen más difícil probar las operaciones aisladamente y extender el sistema.

## Registro de deuda técnica y code smells

| ID | Code smell/debilidad | Evidencia en la versión base | Impacto y riesgo | Prioridad | Mejora aplicada/propuesta |
| --- | --- | --- | --- | --- | --- |
| DT-01 | God Function / demasiadas responsabilidades | `sistema_original.py`, función `procesar()` | Una función decide la operación, valida datos, modifica registros y genera reportes; los cambios pueden afectar ramas no relacionadas. | Alta | Separar casos de uso en `ServicioSolicitudes` y acciones de consola. |
| DT-02 | Condicionales extensos | Cadena de `if/elif` dentro de `procesar()` | Cada nueva operación aumenta la complejidad y la probabilidad de error. | Alta | Delegar cada opción en una función específica. |
| DT-03 | Estado global | Lista global `solicitudes` | Acopla operaciones y pruebas; dificulta usar más de una instancia aislada. | Alta | Inyectar una instancia de repositorio al servicio. |
| DT-04 | Exceso de parámetros | Firma de `procesar(opcion, titulo, tipo, prioridad, responsable, numero, estado)` | La llamada depende de argumentos posicionales y muchos parámetros no aplican a cada operación. | Alta | Introducir `DatosNuevaSolicitud` y métodos específicos. |
| DT-05 | Cadenas mágicas | Valores como `"PENDIENTE"`, `"ALTA"` y `"RESUELTA"` dispersos | Errores tipográficos pueden producir estados inconsistentes. | Media | Usar enumeraciones `EstadoSolicitud` y `Prioridad`. |
| DT-06 | Código repetido | Búsqueda y validación de existencia repetidas en distintas ramas | Si cambia la regla de búsqueda, hay que actualizar varios lugares. | Media | Centralizar la obtención en `_obtener_existente()`. |
| DT-07 | Acoplamiento entre interfaz y negocio | La función `main()` solicita datos y decide operaciones mediante códigos numéricos | Dificulta probar reglas sin simular la consola. | Alta | Separar `consola.py` de `servicio_solicitudes.py`. |
| DT-08 | Manejo de entradas insuficiente | Conversión directa `int(input(...))` en el menú original | Una entrada no numérica puede terminar el programa por excepción no controlada. | Alta | Crear `_leer_entero()` y capturar errores de operación en la interfaz. |
| DT-09 | Representación de datos poco estructurada | Diccionarios con claves de texto para cada solicitud | Los errores en claves y valores se detectan tarde y la estructura no expresa su dominio. | Media | Introducir dataclass `Solicitud`. |
| DT-10 | Reporte con lógica manual repetida | Contadores separados para cada estado | Al sumar estados nuevos hay que modificar el bucle y el formato. | Media | Centralizar el conteo con `Counter` y enumerar estados admitidos. |

**Nota metodológica:** los smells se identifican en el código base, no se presentan como defectos de la versión mejorada sin evidencia. La prioridad es una evaluación cualitativa del impacto y el riesgo.

## Relación con calidad externa e interna

La funcionalidad de cara al usuario puede ser correcta aunque la estructura interna sea frágil. El refactoring busca preservar los casos de uso visibles mientras disminuye el acoplamiento, mejora los límites entre módulos y hace más fácil verificar reglas mediante pruebas.

