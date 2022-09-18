from Csv import *
from request import *
from cache import *
"""
Al ejecutar este programa se prueban las funciones que se 
crearon para el buen funcionamiento de Csv.py
"""

"""
Pruebas de Csv.py
"""
print("Empiezan pruebas Csv: ")
#Definir el archivo csv
nombre_archivo="dataset1.csv"

#Método para recibir dic_origen y dic_destino a partir del csv.
dic_origen, dic_destino= leer_csv(nombre_archivo)

print(f"Diccionario origen: {dic_origen}\n\n")
print(f"Diccionario destino: {dic_destino}?\n\n")

#Ejemplo para saber como consultar la latitud o longitud de un país a partir de su clave. Es analogo con dic_destino.
print(f"La latitud de TLC es:  {dic_origen['TLC'][0]}")
print(f"La longitud de TLC es:  {dic_origen['TLC'][1]}")

"""
Pruebas de request.py
"""
print("Empiezan pruebas request: ")
#Ejemplo para saber como usar la función obtener clima:
lat=dic_origen['TLC'][0]
lon=dic_origen['TLC'][1]
api_key=input("Escribe tu llave: ")
data=obtener_clima(lat,lon,api_key)

imprimirClima(data)

""""
Pruebas de cache.py
"""
print("Empiezan pruebas cache: ")
dic_cache={}
print("Si encuentra en el cache la info la imprime, en otro caso no hace nada")
guardar_cache(dic_cache,'TLC',data)
consultar_cache(dic_cache,'TLC')
