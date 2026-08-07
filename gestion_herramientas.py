#importar o crear la crapeta json
import json
try:
    archivo = open("herramientas.json", "r")
    herramientas = json.load(archivo)
    archivo.close()
except:
    herramientas = {}
    archivo = open("herramientas.json", "w")
    json.dump(herramientas, archivo, indent=4)
    archivo.close()
#------------------------Funciones-----------------------
def registrar_herramientas():
    try:
        id_herramienta = input("ID de la herramienta: ") 
        if  id_herramienta in herramientas:
                print("El ID ya existe.")
                return

        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        cantidad = int(input("Cantidad disponible: "))
        estado = input("Estado (activa, En reparacion, Fuera de servicio): ")
        valor = float(input("Valor estimado: "))

        herramientas[id_herramienta]= {
            "id": id_herramienta,
            "nombre": nombre,
            "categoria": categoria,
            "cantidad": cantidad,
            "estado": estado,
            "valor": valor
        }
        archivo = open("herramientas.json", "w")
        json.dump(herramientas, archivo, indent=4)
        archivo.close()
        print("Herramienta registrada correctamente")
    except ValueError:
         print("Error: Debe ingresar numeros donde corresponda. ")

def listar_herramientas():
    if len(herramientas) == 0:
        print("No hay herramientas registradas. ")
        return
    for id_herramienta, datos in herramientas.items():
         print("---------------------------------------")
         print("ID:", datos["id"])
         print("Nombre:", datos["nombre"])
         print("categoria:", datos["categoria"])
         print("Cantidad:", datos["cantidad"])
         print("Estado:", datos["estado"])
         print("Valor:", datos["valor"])

def buscar_herramientas():
    id_herramienta = input("Ingrese el ID")
    if id_herramienta in herramientas:
        datos = herramientas[id_herramienta]
        print("Nombre:", datos["nombre"])
        print("categoria:", datos["categoria"])
        print("Cantidad:", datos["cantidad"])
        print("Estado:", datos["estado"])
        print("Valor:", datos["valor"])
    else:
        print("Herramienta no encontrada. ")

def actualizar_herramientas():
    id_herramienta = input("ID de la herramienta")
    if id_herramienta not in herramientas:
        print("No existe.")
        return
    try:
        herramientas[id_herramienta]["cantidad"] = int(input("Nueva cantidad: "))
        herramientas[id_herramienta]["estado"] = input("Nuevo estado: ")
        herramientas[id_herramienta]["valor"] = float(input("Nuevo valor:"))
        print("Informacion actualizada correctamene.")
    except ValueError:
        print("Dato invalido.")

def eliminar_herramienta():
    id_herramienta = input("ID de la herramienta:")
    if id_herramienta in herramientas:
        herramientas[id_herramienta]["estado"] = "inactiva"
        print("Herramienta inactiva.")
    else:
        print("No existe.")
    

#---------------------Menú---------------------
opcion = 0

while opcion != 6:
    try:
        print("\n------------SISTEMA DE HERRAMIENTA ----------------")
        print("1. Resgistrar herramienta")
        print("2. Listar herramientas")
        print("3. Buscar herramienta")
        print("4. Actualizar herramientas")
        print("5. Eliminar herramienta")
        print("6. Salir")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            registrar_herramientas()
        elif opcion == 2:
            listar_herramientas()
        elif opcion == 3:
            buscar_herramientas()
        elif opcion == 4:
            actualizar_herramientas()
        elif opcion == 5:
            eliminar_herramienta()
        elif opcion == 6:
            print("Gracias por usar el sistema de herramientas. ")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

    except ValueError as e:
        print("Error en la opcion ingresada. Digite un numero entero.")
    except Exception as e:
        print("Error ", e)