
import unittest
import sys
sys.path.append('Proyecto01')
from src.cache import *
class test_cache(unittest.TestCase):
    """Clase que va a realizar las pruebas de la clase Caché"""
    
    def test__init__(self):
        """Método que nos sirve para probar la funcionalidad del Caché"""
        cache1=cache()
        dic={}
        self.assertIsInstance(cache1,cache)
        self.assertEqual(cache1.dic_cache,dic)

    def test_guardar_cache(self):
        """Método que nos sirve para observar si funciona guardar información en el Caché"""
        cache1=cache()
        cache1.guardar_cache("hola","hello")
        dic={"hola":"hello"}
        self.assertEqual(cache1.dic_cache,dic)
        cache1.guardar_cache("MTY",35)
        dic ["MTY"]=35
        self.assertEqual(cache1.dic_cache,dic)

    def test_consultar_cache(self):
        """Método que nos sirve para observar si podemos consultar información del Caché"""
        cache1=cache()
        cache1.guardar_cache("hola","hello")
        self.assertEqual(cache1.consultar_cache("hola"),"hello")
        self.assertEqual(cache1.consultar_cache("Ximena"),False)




if __name__ == '__main__':
    unittest.main()
"""
cache=cache()

print(cache.dic_cache)

cache.guardar_cache("MTY", "Coordenadas de la ciudad: Latitud: 44.34 Longitud: 10.99 \nTemperatura: 10.81 \nVelocidad del viento: 2.77\nDescripción general: few clouds")

print(cache.consultar_cache("MTY"))

print(cache.consultar_cache("MEX"))

help(cache)"""