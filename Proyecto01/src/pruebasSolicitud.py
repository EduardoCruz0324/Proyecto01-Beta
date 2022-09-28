from solicitud import *

solicitud=solicitud()

solicitud.recibir_llave("Llave")

print(solicitud.llave)

solicitud.crear_url(44.34,10.99)
print(solicitud.url)

print(solicitud.obtener_clima())

help(solicitud)
help(imprimirClima)