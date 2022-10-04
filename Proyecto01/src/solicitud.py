import requests
class solicitud():
    """Clase para crear objetos que tenga como atributos la llave de OpenWheater 
    y la url para hacer la solicitud. Contiene métodos para guardar la llave, crear la url
    y por último obtener los datos climáticos."""

    def __init__(self):
        """Método constructor que define que el objeto tendrá como atributos una url y una llave."""
        self.url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric"
        self.llave=""
        

    def recibir_llave(self,llave):
        """Método para meter la llave del usuario como la propiedad del objeto."""
        self.llave=llave
            

    def crear_url(self,latitud,longitud):
        """Método para crear la url necesaria para realizar las peticiones en la red.
        Recibe como parámetros la latitud y longitud de la ciudad a la que se le quiere hacer la petición"""
        self.url ="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(latitud,longitud,self.llave)
   
    def obtener_clima(self):
        """Método para hacer la solicitud a la red con los atributos almacenados en el objeto.
        Devuelve un string con la información  climática."""
        res = requests.get(self.url)
        if res.status_code==200:
            data = res.json()
            info_clima=obtenerInformacionClimatica(data)
            return info_clima
        else :
            return False


def obtenerInformacionClimatica(data):
    """Funcion auxiliar para procesar un objeto JSON con la información climática y 
    devolverla en un formato de cadena. Recibe como parámetro el JSON con la información climática
    y devuelve una cadena con la información climática necesaria."""
    try:
        temp = str(data["main"]["temp"])
        vel_viento = str(data["wind"]["speed"])
        latitud = str(data["coord"]["lat"])
        longitud = str(data["coord"]["lon"])
        descripcion = str(data["weather"][0]["description"])
        info_clima="Coordenadas de la ciudad: Latitud: "+latitud+" Longitud: "+longitud+"\nTemperatura: "+temp+"\nVelocidad del viento: "+vel_viento+"\nDescripción general: "+descripcion
        return info_clima
    except TypeError:
        print("El parámetro data no es un JSON con la información climática.")