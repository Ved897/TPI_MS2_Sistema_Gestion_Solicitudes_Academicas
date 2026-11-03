"""Versión inicial utilizada como línea base para el diagnóstico.

Los comentarios DT-xx vinculan el código con los code smells documentados en
`docs/diagnostico.md`. Esta versión se conserva para comparar antes/después.
"""

from app.datos_solicitud import DatosSolicitud
from app.repositorio_solicitudes import RepositorioSolicitudes

# DT-03 — Estado global: todas las operaciones comparten esta lista, lo que
# dificulta aislar pruebas y crear instancias independientes del sistema.
solicitudes = []


# Validación separada parcialmente, pero devuelve mensajes en lugar de un
# resultado de dominio tipado; la versión inicial mezcla validación y flujo.
def validar_solicitud(titulo, tipo, prioridad):
    if titulo == "":
        return "Titulo obligatorio"

    if tipo == "":
        return "Tipo obligatorio"

    if prioridad == "":
        return "Prioridad obligatoria"

    if prioridad not in ("ALTA", "MEDIA", "BAJA"):
        return "Prioridad invalida"

    return None


def buscar_solicitud(numero):
    repositorio = RepositorioSolicitudes(solicitudes)
    return repositorio.buscar_por_id(numero)


# Esta función coordina validación, creación del repositorio, generación del
# identificador y construcción del registro. En la refactorización estas
# responsabilidades se distribuyen entre servicio, modelo y repositorio.
def registrar_solicitud(datos: DatosSolicitud):

    error = validar_solicitud(datos.titulo, datos.tipo, datos.prioridad)

    if error is not None:
        return error

    repositorio = RepositorioSolicitudes(solicitudes)

    nuevo_id = repositorio.generar_id()

    solicitud = {
        "id": nuevo_id,
        "titulo": datos.titulo,
        "tipo": datos.tipo,
        "prioridad": datos.prioridad,
        "responsable": datos.responsable,
        "estado": "PENDIENTE",
    }

    repositorio.agregar(solicitud)

    return "Solicitud registrada"


# DT-01 / DT-02 — God Function y condicionales extensos: concentra seis casos
# de uso en una sola función, por lo que cada cambio aumenta el riesgo de afectar
# ramas no relacionadas.
# DT-04 — Exceso de parámetros: cada operación recibe argumentos que muchas
# veces no necesita. Se reemplaza en la versión mejorada por métodos específicos
# y por el objeto DatosNuevaSolicitud.
def procesar(
    opcion, titulo="", tipo="", prioridad="", responsable="", numero=0, estado=""
):

    if opcion == 1:
        datos = DatosSolicitud(
            titulo=titulo, tipo=tipo, prioridad=prioridad, responsable=responsable
        )

        return registrar_solicitud(datos)

    elif opcion == 2:
        solicitud = buscar_solicitud(numero)

        if solicitud is None:
            return "Solicitud no encontrada"

        solicitud["responsable"] = responsable
        return "Responsable asignado"

    elif opcion == 3:
        solicitud = buscar_solicitud(numero)

        if solicitud is None:
            return "Solicitud no encontrada"

        if estado not in ("PENDIENTE", "EN_PROCESO", "RESUELTA"):
            return "Estado invalido"

        solicitud["estado"] = estado
        return "Estado actualizado"

    elif opcion == 4:
        solicitud = buscar_solicitud(numero)

        if solicitud is None:
            return "Solicitud no encontrada"

        return str(solicitud)

    elif opcion == 5:
        # DT-10 — El conteo manual duplica la lógica para cada estado; agregar un
        # estado nuevo exige modificar este bloque. La versión refactorizada usa
        # Counter y recorre los valores definidos en EstadoSolicitud.
        pendientes = 0
        en_proceso = 0
        resueltas = 0

        for s in solicitudes:
            if s["estado"] == "PENDIENTE":
                pendientes += 1
            elif s["estado"] == "EN_PROCESO":
                en_proceso += 1
            elif s["estado"] == "RESUELTA":
                resueltas += 1

        return (
            "Pendientes: "
            + str(pendientes)
            + " | En proceso: "
            + str(en_proceso)
            + " | Resueltas: "
            + str(resueltas)
        )

    elif opcion == 6:
        return str(solicitudes)

    else:
        return "Opcion invalida"


# DT-07 / DT-08 — La interfaz está acoplada a las reglas de negocio y convierte
# entradas directamente con int(input(...)); una entrada no numérica puede
# provocar una excepción no controlada.
def main():
    while True:
        print("\nSISTEMA DE SOLICITUDES ACADEMICAS")
        print("1. Registrar solicitud")
        print("2. Asignar responsable")
        print("3. Cambiar estado")
        print("4. Consultar solicitud")
        print("5. Generar reporte")
        print("6. Listar solicitudes")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            print("Programa finalizado")
            break

        if opcion == "1":
            titulo = input("Titulo: ")
            tipo = input("Tipo: ")
            prioridad = input("Prioridad (ALTA/MEDIA/BAJA): ")
            responsable = input("Responsable: ")
            print(procesar(1, titulo, tipo, prioridad, responsable))

        elif opcion == "2":
            numero = int(input("ID de solicitud: "))
            responsable = input("Responsable: ")
            print(procesar(2, responsable=responsable, numero=numero))

        elif opcion == "3":
            numero = int(input("ID de solicitud: "))
            estado = input("Estado (PENDIENTE/EN_PROCESO/RESUELTA): ")
            print(procesar(3, numero=numero, estado=estado))

        elif opcion == "4":
            numero = int(input("ID de solicitud: "))
            print(procesar(4, numero=numero))

        elif opcion == "5":
            print(procesar(5))

        elif opcion == "6":
            print(procesar(6))

        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()
