from ast import Break
from importlib.metadata import entry_points
from webbrowser import get
from Csv import *
from cache import *
from request import *
from tkinter import*
from tkinter import ttk

#Definir el archivo csv
nombre_archivo="dataset1.csv"

#Método para recibir dic_origen y dic_destino a partir del csv.
dic_origen, dic_destino= leer_csv(nombre_archivo)
dic_cache = {}

#Interfaz
raiz=Tk()
raiz.title("Bienvenidos al AIFA")
raiz.geometry("960x540")
#raiz.resizable(1,1)
#raiz.config(bg="red")

#Fondo de la interfaz
aifa = PhotoImage(file="aifa.png")
background = Label(image = aifa, text = "Imagen S.O de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#Método para mostrar el resultado de la busqueda.
def result(data):
    label = Label(raiz ,text=imprimirClima(data))
    label.place(x=600, y=200)

#Método para procesar la busqueda del usuario.
def conCli():
    def conClim():

        claAir = str(entry.get())
        claOpWe = str(key.get())

        url ="https://api.openweathermap.org/data/2.5/weather?lat=19.3371&lon=-99.566&appid={}&units=metric".format(claOpWe)
        res = requests.get(url)

        
        if consultar_cache(dic_cache, claAir):
            label = Label(raiz ,text=imprimirClima(dic_cache[claAir]))
            label.place(x=50, y=360)
            reCon = ttk.Button(raiz, text="Hacer una nueva busqueda", command=label.destroy)
            reCon.place(x=50,y=390) 
            return
        elif res.status_code!=200:
            label = Label(raiz ,text="Tu llave de OpenWeather es incorrecta.")
            label.place(x=50, y=360)
            reCon = ttk.Button(raiz, text="Hacer una nueva busqueda", command=label.destroy)
            reCon.place(x=50,y=390)
            return 
        elif claAir in dic_origen :
            dato = obtener_clima(dic_origen[claAir][0],dic_origen[claAir][1],claOpWe)
            guardar_cache(dic_cache, claAir, dato)
            result(dato)
            return

        elif claAir in dic_destino :
            dato = obtener_clima(dic_destino[claAir][0],dic_destino[claAir][1],claOpWe)
            guardar_cache(dic_cache, claAir, dato)
            result(dato) 
            return 
        
        else :
            label = Label(raiz ,text="La clave del aeropuerto no sirve")
            label.place(x=50, y=360)
            reCon = ttk.Button(raiz, text="Hacer una nueva busqueda", command=label.destroy)
            reCon.place(x=50,y=390)
        

    labelCla = Label(raiz ,text="Introduce la clave del aeropuerto: ")
    labelCla.place(x=50,y=200)
    entry = ttk.Entry(raiz)
    entry.place(x=50, y=230)
    labelKey = Label(raiz ,text="Introduce tu llave de OpenWeather: ")
    labelKey.place(x=50,y=260)
    key = ttk.Entry(raiz)
    key.place(x=50,y=290)
    buscar = ttk.Button(raiz, text="Buscar", command= conClim)
    buscar.place(x=85, y=320)


#Botón para iniciar conuslta
frm = ttk.Frame(raiz, padding=10)
frm.place(x=85, y=70)
p1 = ttk.Button(frm, text="Iniciar Consulta", command= conCli).grid(column=15, row=20)

#Botón para finalizar programa
frm = ttk.Frame(raiz, padding=10)
frm.place(x=585, y=70)
p2 = ttk.Button(frm, text="Finalizar", command= raiz.destroy).grid(column=15, row=20)

raiz.mainloop()
