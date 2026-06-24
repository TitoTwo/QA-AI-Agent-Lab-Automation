def guardar_archivo(ruta, contenido):

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)