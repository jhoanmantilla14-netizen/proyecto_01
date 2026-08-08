# Inventario de herramientas
herramientas = [
    {
        "id": 1,
        "nombre": "Taladro",
        "stock": 5
    },
    {
        "id": 2,
        "nombre": "Martillo",
        "stock": 10
    },
    {
        "id": 3,
        "nombre": "Destornillador",
        "stock": 8
    }
]


# Lista donde se guardan los préstamos
prestamos = []


# Registrar préstamo
def registrar_prestamo():
    
    id_prestamo = len(prestamos) + 1
    
    usuario = input("Nombre del usuario: ")
    herramienta_nombre = input("Herramienta solicitada: ")
    cantidad = int(input("Cantidad: "))
    
    # Buscar herramienta
    herramienta_encontrada = None
    
    for herramienta in herramientas:
        if herramienta["nombre"].lower() == herramienta_nombre.lower():
            herramienta_encontrada = herramienta


    # Verificar si existe la herramienta
    if herramienta_encontrada == None:
        print("La herramienta no existe")
        return


    # Verificar disponibilidad
    if herramienta_encontrada["stock"] < cantidad:
        print("No hay suficiente stock disponible")
        return


    # Restar cantidad del inventario
    herramienta_encontrada["stock"] -= cantidad


    fecha_inicio = input("Fecha de inicio: ")
    fecha_devolucion = input("Fecha estimada de devolución: ")
    observaciones = input("Observaciones: ")


    prestamo = {
        "id": id_prestamo,
        "usuario": usuario,
        "herramienta": herramienta_nombre,
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio,
        "fecha_devolucion": fecha_devolucion,
        "estado": "Prestado",
        "observaciones": observaciones
    }


    prestamos.append(prestamo)

    print("Préstamo registrado correctamente")


# Mostrar préstamos
def mostrar_prestamos():

    if len(prestamos) == 0:
        print("No existen préstamos")
        return

    for prestamo in prestamos:
        print("----------------------")
        print("ID:", prestamo["id"])
        print("Usuario:", prestamo["usuario"])
        print("Herramienta:", prestamo["herramienta"])
        print("Cantidad:", prestamo["cantidad"])
        print("Estado:", prestamo["estado"])



# Devolver herramienta
def devolver_herramienta():

    id_buscar = int(input("Ingrese ID del préstamo: "))


    for prestamo in prestamos:

        if prestamo["id"] == id_buscar:

            if prestamo["estado"] == "Devuelto":
                print("Este préstamo ya fue devuelto")
                return


            # Cambiar estado
            prestamo["estado"] = "Devuelto"


            # Restaurar stock
            for herramienta in herramientas:
                if herramienta["nombre"] == prestamo["herramienta"]:
                    herramienta["stock"] += prestamo["cantidad"]


            print("Herramienta devuelta correctamente")
            return


    print("Préstamo no encontrado")



# Mostrar inventario
def mostrar_inventario():

    for herramienta in herramientas:
        print("----------------")
        print("Herramienta:", herramienta["nombre"])
        print("Stock:", herramienta["stock"])



# Menú principal

while True:

    print("""
    
    SISTEMA DE PRÉSTAMOS

    1. Registrar préstamo
    2. Mostrar préstamos
    3. Devolver herramienta
    4. Mostrar inventario
    5. Salir

    """)

    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        registrar_prestamo()

    elif opcion == "2":
        mostrar_prestamos()

    elif opcion == "3":
        devolver_herramienta()

    elif opcion == "4":
        mostrar_inventario()

    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida")