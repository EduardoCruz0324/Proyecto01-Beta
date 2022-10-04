import unittest
import sys
sys.path.append('Proyecto01')
from src.solicitud import *
class test_solicitud(unittest.TestCase):
    
    def test__init__(self):
        """Método que nos sirve para probar la funcionalidad de las solicitudes."""
        solicitud1=solicitud()
        vacio=""
        self.assertIsInstance(solicitud1,solicitud)
        self.assertEqual(solicitud1.url,"https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric")
        self.assertEqual(solicitud1.llave,vacio)

    def test_recibir_llave(self):
        """Método que nos sirve para probar si funciona las consultas de la llave."""
        solicitud1=solicitud()
        solicitud1.recibir_llave("asijuhij73883jdhj")
        self.assertEqual(solicitud1.llave,"asijuhij73883jdhj")
        solicitud1.recibir_llave("holaquehace")
        self.assertEqual(solicitud1.llave,"holaquehace")
        solicitud1.recibir_llave("")
        self.assertEqual(solicitud1.llave,"")

    def test_crear_url(self):
        """Método que nos sirve para probar si podemos crear una url."""
        solicitud1=solicitud()
        solicitud1.crear_url("15.2","34.2")
        self.assertEqual(solicitud1.url,"https://api.openweathermap.org/data/2.5/weather?lat=15.2&lon=34.2&appid=&units=metric")
        solicitud1.crear_url(34,45)
        self.assertEqual(solicitud1.url,"https://api.openweathermap.org/data/2.5/weather?lat=34&lon=45&appid=&units=metric")
        solicitud1.crear_url(True,False)
        self.assertEqual(solicitud1.url,"https://api.openweathermap.org/data/2.5/weather?lat=True&lon=False&appid=&units=metric")

    def test_obtener_clima(self):
        """Método que nos sirve para probar si se nos puede devolver el clima de alguna ciudad."""
        solicitud1=solicitud()
        self.assertEqual(solicitud1.obtener_clima(),"Algo salió mal... la llave proporcionada ó las coordenadas de la ciudad son incorrectas.")
        solicitud1.crear_url(4,3)
        self.assertEqual(solicitud1.obtener_clima(),"Algo salió mal... la llave proporcionada ó las coordenadas de la ciudad son incorrectas.")
        solicitud1.recibir_llave("hola")
        self.assertEqual(solicitud1.obtener_clima(),"Algo salió mal... la llave proporcionada ó las coordenadas de la ciudad son incorrectas.")

    def test_imprimir_clima(self):
        """Método que nos sirve para probar si se puede imprimir el clima de alguna ciudad consultada."""
        data={'coord': {'lon': 10.99, 'lat': 44.34}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 11.52, 'feels_like': 10.97, 'temp_min': 8.66, 'temp_max': 12.41, 'pressure': 1004, 'humidity': 86, 'sea_level': 1004, 'grnd_level': 919}, 'visibility': 10000, 'wind': {'speed': 2.68, 'deg': 200, 'gust': 4.33}, 'clouds': {'all': 96}, 'dt': 1664504673, 'sys': {'type': 2, 'id': 2004688, 'country': 'IT', 'sunrise': 1664514732, 'sunset': 1664557192}, 'timezone': 7200, 'id': 3163858, 'name': 'Zocca', 'cod': 200}
        info_clima="Coordenadas de la ciudad: Latitud: 44.34 Longitud: 10.99\nTemperatura: 11.52\nVelocidad del viento: 2.68\nDescripción general: overcast clouds"
        self.assertEqual(imprimirClima(data),info_clima)

if __name__ == '__main__':
    unittest.main()
"""
solicitud=solicitud()

solicitud.recibir_llave("llave")

print(solicitud.llave)

solicitud.crear_url(44.34,10.99)
print(solicitud.url)

print(solicitud.obtener_clima())

help(solicitud)
help(imprimirClima)"""