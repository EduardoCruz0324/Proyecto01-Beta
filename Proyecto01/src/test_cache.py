from cache import *
import unittest
class test_cache(unittest.TestCase):
    
    def test__init__(self):
        cache1=cache()
        dic={}
        self.assertIsInstance(cache1,cache)
        self.assertEqual(cache1.dic_cache,dic)

    def test_guardar_cache(self):
        cache1=cache()
        cache1.guardar_cache("hola","hello")
        dic={"hola":"hello"}
        self.assertEqual(cache1.dic_cache,dic)
        cache1.guardar_cache("MTY",35)
        dic ["MTY"]=35
        self.assertEqual(cache1.dic_cache,dic)

    def test_consultar_cache(self):
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