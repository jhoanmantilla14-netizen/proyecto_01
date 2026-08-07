usuarios = []
def crear_usuario():
    print("-----REGISTRAR USUARIO-----")
    id_usuario = input("Ingrese el ID de usuario (Cedula/Documento): ")
    documento_existe = False
    for u in usuarios:
        if u['id'] == id_usuario:
            documento_existe = True
            break
    if documento_existe:
        print("Error: Ya existe un usuario resgistrado con ese documento.")
        return    

    nombres = input("Nombres del usuario: ")
    apellidos = input("Apellidos: ")
    telefono = input("Telefono: ")
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
        "Tipo de usuario": tipo
    }
    usuarios.append(usuario)
    print("-----Usuario registrado-----")

def listar_usuarios():
    print("-----LISTA DE USUARIOS-----")
    if not usuarios:
        print("No hay usuarios registrados.")
        return
for u in usuarios:
    print(f"ID: {u['id']} | Nombre: {u['nombres']},{u['apellidos']} | "
          f"Tel: {u['telefono']} | Dir: {u['direccion']} | Tipo: {u['tipo']}")

def buscar_usuario():
    print("---BUSCAR USUARIO---")
    id_usuario = input("Ingrese el ID del usuario: ")
    for u in usuarios:
        if u['id'] == id_usuario:
            print(f"Encontrado: {u}")
            return u
    print("Usuario no encontrado.")
    return None

def actualizar_usuario():
    print("-----ACTUALIZAR USUARIO-----")
    u = buscar_usuario()
    if u:
        print("Deja en blaco si no desea modificar el campo.")
        #mantiene el valor actual si la entrada del usuario queda vacia
        u['nombres'] = input(f"Nombres [{u['nombres']}]: ") or u['nombres']
        u['apellidos'] = input(f"Apellidos [{u['apellidos']}]: ") or u['apellidos']
        u['telefono'] = int(input(f"Telefono [{u['telefono']}]: ")) or u['telefono']
        u['direccion'] = input(f"Direccion [{u['direccion']}]: ") or u['direccion']
        print("Tipo: 1.Residente | 2.Administrador | presione Enter para omitir.")
        opcion_tipo = input("seleccione (1-2): ")
        if opcion_tipo == "1":
            u['tipo'] = "residente"
        elif opcion_tipo == "2":
            u['tipo'] = "administrador"
        print("-----USUARIO ACTUALIZADO-----") 

def eliminar_usuario():
    print("-----ELIMINAR USUARIO-----")
    id_u = input("Ingrese el ID del usuario a eliminar: ")
    for u in usuarios:
        if u['id'] == id_u:
            usuarios.remove(u)
            print("Usuario eliminado con exito.")
            return
print("Usuario no encontrado.")                       