from datetime import datetime
def registrar_log(mensaje, tipo="ERROR", nombre_archivo="app.log"):
    timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    linea = f"[{timestamp}] [{tipo.upper()}]: {mensaje}\n" 
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as archivo: 
            archivo.write(linea)
    except Exception as e:
        print(f"Error al escribir en el log: {e}")

#datetime permite obtener la fecha y la hora
#datetime.now() captura el momento exacto en que se ejecuta la línea. 
# .strftime("%Y-%m-%d %H:%M:%S") convierte ese objeto en un texto con formato Año-Mes-Día Hora:Minuto:Segundo
# .upper() convierte el tipo a mayuscula
# encoding="utf-8": Permkite guardar tildes, caracteres especiales y la letra ñ