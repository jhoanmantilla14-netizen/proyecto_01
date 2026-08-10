from usuarios import obtener_usuarios, crear_usuarios, buscar_usuario, actualizar_usuario, eliminar_usuario, guardar_usuarios
from persistence import guardar_datos, cargar_datos
from logger import registrar_log

def menu_administrador(user):
    while True:
        print("-----MENU ADMINISTRADOR------ ")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Herramientas")
        print("3. Aprobar / Rechazar Prestamos")
        print("4. Registrar Devolucion")
        print("5. Consultas y Reportes")
        print("6. Cerrar Sesion")
        opcion = input("Seleccione una opcion del menu: ")

        if opcion == "1":
            print("-----GESTION DE USUARIOS-----")
            print("1. Crear 2. Listar 3. Buscar")
            sub = input("Opcion: ")
            if sub == "1":
                id_u = input("ID: ")
                nom = input("Nombres: ")
                ape = input("Apellidos: ")
                tel = input("Telefono: ")
                dir_u = input("Direccion: ")
                tipo = input("Tipo (administrador/residente): ")
                msg = crear_usuarios(id_u, nom, ape, tel, dir_u, tipo)
                print(msg)
            elif sub == "2":
                for u in obtener_usuarios():
                    print(u)
            elif sub == "3":
                id_u = input("ID a buscar: ")
                print(buscar_usuario(id_u) or "No encontrado")
        if opcion == "6":
            break        


def menu_residente(user):
    while True:
        print("-----MENU RESIDENTE-----")
        print("1. Consultar Catalogo de Herramientas")
        print("2. Solicitar Prestamo")
        print("3. Ver Mis Prestamos")
        print("4. Cerrar Sesion")
        opcion = input("Seleccione una opcion: ")