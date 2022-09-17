from Csv import *

#Definir el archivo csv
nombre_archivo="dataset1.csv"

#Método para recibir dic_origen y dic_destino a partir del csv.
dic_origen, dic_destino= leer_csv(nombre_archivo)


print(f"Diccionario origen: {dic_origen}\n\n")
print(f"Diccionario destino: {dic_destino}")

#Ejemplo para saber como consultar la latitud o longitud de un país a partir de su clave. Es analogo con dic_destino.
print(f"La latitud de TLC es:  {dic_origen['TLC'][0]}")
print(f"La longitud de TLC es:  {dic_origen['TLC'][1]}")

