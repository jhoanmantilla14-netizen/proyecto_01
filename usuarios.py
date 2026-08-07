from persistence import cargar_datos, guardar_datos
from logger import registrar_log
archivo_usuarios = "usuarios.json" #Define la variable con el nombre del archivo JSON donde se almacenara la lista de usuarios

def obtener_usuarios():  #para recupperar el listado de usuarios
    return cargar_datos(archivo_usuarios) #retorna la lissta de usuarios cargada

def guardar_usuarios(usuarios, archivo_usuarios):
    guardar_datos(usuarios, archivo_usuarios)

def crear_usuarios(id_u, nombres, apellidos, telefono, direccion, tipo):
    usuarios = obtener_usuarios() #obtiene la lista de usuarios desde el archivo json
    if any(us['id'] == id_u for us in usuarios): #verifica si ya existe algun usuario en la lista igual al id agregado
        registrar_log(f"Intento fallido: Ya existe un usuario con ID {id_u}", " ERROR")
        return False, "El ID de usuario ya esta registrado."

    nuevo_usuario = {
        "id": id_u,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo.lower() # Administrador  o residente
    }    

    usuarios.append(nuevo_usuario) #agrega el nuevo diccionario a la lista de usuarios en memoria
    archivo_usuarios(usuarios) 
    registrar_log(f"Usuario crado existosamente: {id_u} - {nombres} {apellidos}")
    return "Usuario registrado correctamente."

def buscar_usuario(id_u):
    usuarios = obtener_usuarios()
    for us in usuarios:
        if us["id"] == id_u: # #compara si el ID del usuario iterado coincide con el id_u buscado
            return us
    return None

def actudalizar_usuario(id_u, nombres=None, apellidos=None, telefono=None, direccion=None, tipo=None):
    usuarios = obtener_usuarios() #carga la lista de usuarios almacenados
    for us in usuarios:
        if us["id"] == id_u: 
            if nombres: us["nombres"] = nombres
            if apellidos: us["apellidos"] = apellidos
            if telefono: us["telefono"] = telefono  
            if direccion: us["direccion"] = direccion
            if tipo: us["tipo"] = tipo.lower()
            guardar_usuarios(usuarios)
            registrar_log(f"Usuario {id_u} actualizado correctamente.")
            return True, "Usuario actualizado."
        return False, "Usuario no encontrado."

def eliminar_usuario(id_u):
    usuarios = obtener_usuarios()
    usuarios_filtrados = [us for us in usuarios if us["id"] != id_u]
    if len(usuarios == len(usuarios_filtrados)):
        return False, "Usuario no encontrado."
    guardar_usuarios(usuarios_filtrados)
    registrar_log(f"Usuario {id_u} eliminado.")
    return True, "Usuario eliminado correctamente."



           
    
                         