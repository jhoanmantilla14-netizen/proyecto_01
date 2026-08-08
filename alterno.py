from logger import registrar_log


def registrar_herramienta():
    try:
        id_herramienta = input("ID de la herramienta: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        cantidad = int(input("Cantidad disponible: "))
        estado = input("Estado (Activa, En reparación, Fuera de servicio): ")
        valor = float(input("Valor estimado: "))

        mensaje = (
            f"ID={id_herramienta} | "
            f"Nombre={nombre} | "
            f"Categoría={categoria} | "
            f"Cantidad={cantidad} | "
            f"Estado={estado} | "
            f"Valor={valor}"
        )

        registrar_log(mensaje, "INFO")

        print("Herramienta registrada correctamente.")

    except ValueError:
        print("Error: la cantidad debe ser un número "
              "y el valor debe ser un número decimal.")


def mostrar_herramientas():
    try:
        archivo = open("app.log", "r", encoding="utf-8")

        encontrado = False

        for linea in archivo:
            if "[INFO]" in linea and "ID=" in linea:
                print(linea.strip())
                encontrado = True

        archivo.close()

        if not encontrado:
            print("No hay herramientas registradas.")

    except FileNotFoundError:
        print("No existe ningún registro todavía.")


def buscar_herramienta():
    id_buscar = input("Ingrese el ID de la herramienta: ")

    try:
        archivo = open("app.log", "r", encoding="utf-8")

        encontrado = False

        for linea in archivo:
            if f"ID={id_buscar} " in linea:
                print("\nHerramienta encontrada:")
                print(linea.strip())
                encontrado = True

        archivo.close()

        if not encontrado:
            print("No se encontró una herramienta con ese ID.")

    except FileNotFoundError:
        print("No existen herramientas registradas.")


def menu():
    opcion = 0

    while opcion != 4:
        print("\n========== GESTIÓN DE HERRAMIENTAS ==========")
        print("1. Registrar herramienta")
        print("2. Mostrar herramientas")
        print("3. Buscar herramienta")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_herramienta()

            elif opcion == 2:
                mostrar_herramientas()

            elif opcion == 3:
                buscar_herramienta()

            elif opcion == 4:
                print("Programa finalizado.")

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debe ingresar un número.")


menu()