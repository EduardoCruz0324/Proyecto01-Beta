#Módulo para leer el csv(base de datos) y regresar los diccionarios origen y destino.

#Recibe como parámetro a leer el csv 
#Devuelve dos diccionarios, dic_origen y dic_destino 
#Compuestos como key=<nombre del pais> ej."MTY", y valor=["<latitud>","<longitud>"] ej.['25.7785', '-100.107']
def leer_csv(nombre_archivo):
    try:
        dic_origen={}
        dic_destino={}
        with open(nombre_archivo, "r") as archivo:
            # Omitir el encabezado
            next(archivo, None)
            for linea in archivo:
                # Remover salto de línea
                linea = linea.rstrip()
                # Ahora convertimos la línea a arreglo con split
                separador = ","
                lista = linea.split(",")
                # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
                pais_origen = lista[0]
                pais_destino = lista[1]
                origin_latitude = lista[2]
                origin_longitude = lista[3]
                destination_latitude= lista[4]
                destination_longitude=lista[5]

                dic_origen[lista[0]]= lista[2:4]
                dic_destino[lista[1]]= lista[4:6]
        #Para saber como quedaron los diccionarios, clave y valor.
        #print(f"El diccionario origen contiene: {dic_origen.items()}\n\n")
        #print(f"El diccionario destino contiene: {dic_destino.items()}")
        return dic_origen, dic_destino
    except FileNotFoundError:
        msg="Parece que el archivo "+nombre_archivo+" no existe."
        print(msg)
#Ejemplo para saber como consultar la latitud o longitud de un país a partir de su clave. Es analogo con dic_destino.
#print(f"La latitud de TLC es:  {dic_origen['TLC'][0]}")
#print(f"La longitud de TLC es:  {dic_origen['TLC'][1]}")