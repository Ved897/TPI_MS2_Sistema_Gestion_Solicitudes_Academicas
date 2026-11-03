| N° | Criterio | Resultado | Observación |
| --- | --- | --- | --- |
| 1 | Nombres claros y consistentes | Cumple | Nomenclatura en español y coherente entre módulos |
| 2 | Funciones cortas con un solo propósito | Cumple | Las funciones de consola y servicio son breves |
| 3 | Sin estado global en app/ | Cumple | El estado vive en la instancia del repositorio |
| 4 | Dependencias hacia abstracciones | Cumple | El servicio depende del Protocol |
| 5 | Errores explícitos y coherentes | Parcial | Ver observación 1 |
| 6 | Sin duplicación de lógica | Cumple | Búsqueda unificada en _obtener_existente() |
| 7 | Las pruebas pasan en una instalación limpia | Cumple | 8 pruebas pasan |
| 8 | README completo e historial con tags | Cumple | Ver observación 2 |

| Obs. | Archivo | Observación | Acción tomada | Estado |
| --- | --- | --- | --- | --- |
| 1 | consola.py, servicio_solicitudes.py | El servicio lanza TypeError en algunos casos que la consola no captura, y _leer_enum() no reintenta como _leer_entero() | Se registra como mejora futura | Mejora pendiente, justificada |
| 2 | README.md | Quedan restos de la plantilla y datos de portada pendientes | Se limpia y completa el README | Corregida |
