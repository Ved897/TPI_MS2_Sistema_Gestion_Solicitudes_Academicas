# Comparación antes/después

| Aspecto | Antes | Después | Evidencia que debe adjuntarse |
| --- | --- | --- | --- |
| Responsabilidades | Una función `procesar()` reúne la mayoría de las operaciones. | La consola, el servicio, los modelos y el repositorio tienen responsabilidades separadas. | Captura de ambas estructuras y comparación de archivos. |
| Parámetros | Una función recibe numerosos parámetros, varios irrelevantes para cada operación. | `DatosNuevaSolicitud` agrupa los datos de registro y existen métodos con parámetros específicos. | Firmas de métodos antes/después. |
| Almacenamiento | Lista global compartida. | Repositorio inyectado al servicio. | Inicialización del sistema y constructor del servicio. |
| Tipos de estado/prioridad | Cadenas de texto dispersas. | Enumeraciones `EstadoSolicitud` y `Prioridad`. | Definiciones y validaciones. |
| Búsqueda y errores | La búsqueda y los mensajes se repiten en varias ramas. | `_obtener_existente()` centraliza la consulta y usa una excepción específica. | Código y pruebas de ID inexistente. |
| Reporte | Contadores manuales por estado. | Conteo centralizado y resultado con claves conocidas. | Método `generar_reporte()` y test de reporte. |
| Pruebas | Dependencia de la lista global y de una función multipropósito. | Pruebas aisladas sobre servicio y repositorio. | Salida real de `pytest`. |

## Refactorings documentados

### 1. Extract Method

**Antes:** las ramas de `procesar()` contienen detalles de registro, asignación, cambio de estado, consulta y reporte.  
**Después:** cada acción de consola se delega a `_registrar()`, `_asignar()`, `_cambiar_estado()`, `_consultar()`, `_mostrar_reporte()` o `_listar()`; el servicio mantiene los casos de uso.  
**Beneficio:** cada función tiene un propósito más claro y puede revisarse por separado.

### 2. Move Method / reubicación de responsabilidad

**Antes:** búsqueda, generación de identificadores y operaciones de almacenamiento se mezclan con el flujo general.  
**Después:** las operaciones de almacenamiento pertenecen a `RepositorioEnMemoria`; las reglas de negocio están en `ServicioSolicitudes`.  
**Beneficio:** los cambios de almacenamiento pueden realizarse sin modificar la interfaz de consola.

### 3. Introduce Parameter Object

**Antes:** `procesar()` recibe varios parámetros independientes, incluso cuando la operación no los utiliza.  
**Después:** `DatosNuevaSolicitud` agrupa título, tipo, prioridad y responsable para el caso de registro.  
**Beneficio:** llamadas más expresivas y menos posibilidades de confundir argumentos.

### 4. Replace Primitive with Enum / eliminar cadenas mágicas

**Antes:** estados y prioridades se representan con cadenas sueltas.  
**Después:** `EstadoSolicitud` y `Prioridad` limitan los valores admitidos y mejoran la legibilidad.  
**Beneficio:** reglas explícitas y menor riesgo de errores tipográficos.

## Seguridad del refactoring

La seguridad se verifica ejecutando pruebas sobre las operaciones principales: registro, validación, asignación, cambio de estado, consulta, listado y reporte. Para una comparación académica completa, ejecutar también los mismos escenarios manuales sobre la versión inicial y conservar capturas de ambas ejecuciones. No afirmar equivalencia absoluta solo por tener pruebas: indicar qué escenarios fueron comprobados y cuáles quedan fuera del alcance.
