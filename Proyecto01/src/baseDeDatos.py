class baseDeDatos():
    """Clase para crear un objeto que tenga como propiedades dos diccionarios que contendran 
    la información pertinente a las ciudades de origen y de destino junto con sus coordenadas. 
    Tambien el objeto es capaz de leer la base de datos y guardar la información pertinente."""

    def __init__(self):
        """Constructor del objeto, donde se definen dos propiedades, 
        que son los diccionarios que contendrá"""
        self.dic_origen={}
        self.dic_destino={}

    def leer_datos(self,nombre_archivo):
        """Método que recibe como parámetro una ruta del archivo que se quiere leer, el método 
        lee los datos y guarda la información en sus atributos."""
        try:
            with open(nombre_archivo, "r") as archivo:
                next(archivo, None)
                for linea in archivo:
                    linea = linea.rstrip()
                    separador = ","
                    lista = linea.split(",")
                    pais_origen = lista[0]
                    pais_destino = lista[1]
                    origin_latitude = lista[2]
                    origin_longitude = lista[3]
                    destination_latitude= lista[4]
                    destination_longitude=lista[5]
                    self.dic_origen[lista[0]]= lista[2:4]
                    self.dic_destino[lista[1]]= lista[4:6]
        except FileNotFoundError:
            msg="Parece que el archivo "+nombre_archivo+" no existe."
            print(msg)