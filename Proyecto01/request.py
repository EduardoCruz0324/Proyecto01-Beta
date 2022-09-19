import requests

'''
Recibe como parámetros la latitud y longitud del país deseado,
además la llave de la API openWheather
Devuelve un JSON con los datos pertinentes al clima listos para ser manipulados.
'''
def obtener_clima(lat,lon,api_key):
    try:
        url ="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(lat,lon,api_key)
        res = requests.get(url)

        if res.status_code==200:
            data = res.json()
            return data
        else :
            raise KeyError
    except KeyError:
        msg="Algo salió mal... la llave proporcionada ó las coordenadas de la ciudad son incorrectas."
        print(msg)

'''
Recibe como parámero un JSON con la información del clima de una ciudad.
Imprime los datos pertinentes del clima.
'''
def imprimirClima(data):
    try:
        temp = str(data["main"]["temp"])
        vel_viento = str(data["wind"]["speed"])
        latitud = str(data["coord"]["lat"])
        longitud = str(data["coord"]["lon"])
        descripcion = str(data["weather"][0]["description"])
        #puedes agregar los datos que quieras, hay muchos más, revisar en documentación de 
        #OpenWheater.
        info_clima="Coordenadas de la ciudad: "+latitud+longitud+"\nTemperatura: "+temp+"\nVelocidad del viento: "+vel_viento+"\nDescripción general: "+descripcion
        return info_clima
        #print("Temperatura: ", temp)
        #print("Velocidad del viento: {} m/s".format(vel_viento))
        #print("Latitud: {}".format(latitud))
        #print("Longitud: {}".format(longitud))
        #print("Descripción: {}".format(descripcion))
    except TypeError:
        print("El parámetro data no es un JSON con la información climática.")