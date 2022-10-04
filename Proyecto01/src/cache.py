from solicitud import *
class cache():
    dic_cache = {}
    """Clase para simular un objeto cache, que contiene un diccionario como atributo, 
    el objeto es capaz de hacer consultas en su diccionario y devolver la información contenida."""
    def __init__(self):
        """Método constructor que inicializa como atributo un diccionario que guardará
        la información ya consultada para que funcione como 'cache'."""

    """
    Método para guardar la cadena con la información climática en nuestro atributo dic_cache
    Recibe como parametros la clave de la ciudad consultada y su respectiva información climática.
    """
    def guardar_cache(self,clave_ciudad, info_clima):
        """Método para guardar la cadena con la información climática en nuestro atributo dic_cache
        Recibe como parámetros la clave de la ciudad consultada y su respectiva información climática."""
        self.dic_cache[clave_ciudad] = info_clima
 
    def consultar_cache(self,clave_ciudad):
        """Método para consultar si ya tenemos la información climática del país requerido
        dentro de nuestro diccionario caché.
        Recibe como parámetro la clave de la ciudad que se quiere buscar. Si encuentra la llave
        devuelve su valor asociado, en otro caso devuelve False."""
        if clave_ciudad in self.dic_cache :
            return self.dic_cache[clave_ciudad]
        else :
            return False