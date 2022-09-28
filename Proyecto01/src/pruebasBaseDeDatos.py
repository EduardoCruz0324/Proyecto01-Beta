from baseDeDatos import *

baseDeDatos=baseDeDatos()
print(baseDeDatos.dic_destino)

baseDeDatos.leer_datos("Proyecto01/RecursosExtra/dataset1.csv")

print(f"El diccionario origen contiene: {baseDeDatos.dic_origen.items()}\n\n")

print(f"El diccionario destino contiene: {baseDeDatos.dic_destino.items()}")

help(baseDeDatos)
