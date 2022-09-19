from importlib.metadata import entry_points
from webbrowser import get
from Csv import *
from cache import *
from request import *
from tkinter import*
from tkinter import ttk

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
def result():
    label = Label(raiz ,text="Hola")
    label.place(x=600, y=250)

#Método para procesar la busqueda del usuario.
def conCli():
    def conClim():
        print(entry.get())
        print(key.get())
        result

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



frm = ttk.Frame(raiz, padding=10)
frm.place(x=85, y=70)
p1 = ttk.Button(frm, text="Iniciar Consulta", command= conCli).grid(column=15, row=20)

raiz.mainloop()
