from cache import *

cache=cache()

print(cache.dic_cache)

cache.guardar_cache("MTY", "Coordenadas de la ciudad: Latitud: 44.34 Longitud: 10.99 \nTemperatura: 10.81 \nVelocidad del viento: 2.77\nDescripción general: few clouds")

print(cache.consultar_cache("MTY"))

print(cache.consultar_cache("MEX"))

help(cache)