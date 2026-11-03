# Decisiones técnicas

1. **Python y consola:** se conserva el alcance pequeño del prototipo y no se agrega una interfaz web que no exige la consigna.
2. **Repositorio en memoria:** se elige por simplicidad y facilidad de pruebas; los datos no sobreviven al cierre. Si la cátedra exige persistencia duradera, esta decisión debe cambiarse.
3. **Dataclasses:** representan una solicitud y los parámetros de registro de forma explícita.
4. **Enumeraciones:** restringen los valores de estado y prioridad.
5. **Servicio de aplicación:** concentra reglas y casos de uso fuera de la interfaz.
6. **Contrato de repositorio:** permite sustituir la implementación de almacenamiento sin modificar el servicio, ilustrando DIP.
7. **Errores de dominio:** distinguir una solicitud inexistente de una entrada inválida hace que el manejo de errores sea más claro.
8. **Pruebas con repositorio nuevo:** evita que los datos de una prueba contaminen a otra.

## Límites conocidos

- No hay persistencia permanente.
- No se implementan autenticación ni permisos.
- No se aplican reglas avanzadas de transición de estados.
- No se trata concurrencia.
- La consola es la única interfaz.

Estos límites son deliberados para mantener acotado el módulo; deben mencionarse en las conclusiones.
