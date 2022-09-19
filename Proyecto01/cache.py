from request import *

"""
Método para guardar los JSON climáticos en un diccionario que actuará 
como cache del programa.
Recibe como parametros el diccionario cache la llave y el JSON que se quiere guardar.
"""
def guardar_cache(dic_cache, pais_key, JSON):
    diccionario={}
    if type(JSON)==type(diccionario):
        dic_cache [pais_key]= JSON
    else:
        print("No se pudo guardar en el caché")    

"""
Método para consultar si ya tenemos la información climática del país requerido
dentro de nuestro diccionario caché.
Recibe como parámetros el diccionario y la llave que se quiere buscar. Si encuentra la llave
manda llamar función imprimirClima() y devuelve true, en otro caso devuelve False.
"""
def consultar_cache(dic_cache, pais_key):
    if pais_key in dic_cache :
        #imprimirClima(dic_cache[pais_key])
        return True
    else :
        return False    