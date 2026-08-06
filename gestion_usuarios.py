usuario = []
def crear_usuario():
    id_usuario = input("Ingrese el ID de usuario (Cedula/Documento): ")

    nombres = input("nNombre del usuario: ")
    apellidos = input("Apellidos: ")
    telefono = int(input("Telefono: "))
    direccion = input("Direccion: ")

    print("Tipo de usuario: \n1.Residente \n2.Administrador")
    opcion_usuario = input("seleccione (1-2): ")
    tipo = "administrador" if opcion_usuario == "2" else "residente"

    usuario = {
        "id": id_usuario,
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Telefono": telefono,
        "Direccion": direccion,
        "Tipo de usuario": opcion_usuario
    }