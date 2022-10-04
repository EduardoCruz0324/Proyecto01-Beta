import tkinter
from baseDeDatos import baseDeDatos
from cache import cache
from solicitud import solicitud
from tkinter import Tk, PhotoImage, Label, Button, Entry
class Elementos():
    """Clase que se encarga de componer los elementos para realizar la interfaz."""
    textos: dict[str, tkinter.Label] = {}
    botones: dict[str, tkinter.Button] = {}
    formas: dict[str, tkinter.Entry] = {}
    def __init__(self):
        pass
    def agregar_boton(self, name: str, boton: tkinter.Button):
        """Método que nos permité agregar botones."""
        self.botones[name] = boton
    def agregar_forma(self, name: str, forma: tkinter.Entry):
        """Método que nos permité agregar entradas."""
        self.formas[name] = forma
    def agregar_texto(self, name: str, forma: tkinter.Label):
        """Método que nos permité agregar cuadros de texto."""
        self.textos[name] = forma

class Interfaz():
    """Clase que se encarga de darle forma al proyecto a traves de una interfaz."""
    solicitudes = solicitud()
    cache = cache()
    baseDatos = baseDeDatos()
    baseDatos.leer_datos("Proyecto01/RecursosExtra/dataset1.csv")
    elementos = Elementos()

    def __init__(self):
        """Método que hace que podamos crear la interfaz, utilizando Tkinter, partiendo de una raíz con una
        imagén de fondo y dando funciones a los botones que se muestran en la interfaz."""
        self.raiz=Tk()
        self.raiz.title("Bienvenidos al AIFA")
        self.raiz.geometry("960x540")
        self.raiz.resizable(0,0)
        self.aifa = PhotoImage(file="Proyecto01/imagenes/aifa.png")
        # Set Labels insight interfaz
        Label(self.raiz,image=self.aifa).place(x = 0, y = 0, relwidth = 1, relheight = 1)
        Label(self.raiz ,text="Clave de la ciudad: ").place(x=75,y=200)
        Label(self.raiz ,text="Llave de OpenWeather:").place(x=50,y=260)
        texto_coordenadas = Label(self.raiz ,text="")
        texto_coordenadas.place(x=450, y=200)
        self.elementos.agregar_texto("coordenadas", texto_coordenadas)
        # Botones
        boton1 = Button(self.raiz, text="Consultar Clima", command=self.consultar_clima)
        boton1.place(x=50, y=320)
        self.elementos.agregar_boton("consultar", boton1)
        boton2 = Button(self.raiz, text="Reiniciar consultas", command=self.reiniciar).place(x=210 ,y= 320)
        self.elementos.agregar_boton("reiniciar consultas", boton2)
        boton3 = Button(self.raiz, text="Finalizar", command=self.raiz.destroy).place(x=700, y=320)
        self.elementos.agregar_boton("finalizar", boton3)
        #Entrys
        entrada_ciudad=Entry(self.raiz)
        entrada_ciudad.place(x=210, y=200)
        self.elementos.agregar_forma("entrada_ciudad",entrada_ciudad)
        entrada_llave=Entry(self.raiz)
        entrada_llave.place(x=210,y=260)
        self.elementos.agregar_forma("entrada_llave", entrada_llave)
        print(entrada_llave)
    
    def result(self):
        """Método el cual no arroja el resultado de la busqueda que el usuario
        desea hacer."""
        self.elementos.textos['coordenadas'].configure(text=self.solicitudes.obtener_clima())

    def consultar_clima(self):
        """Método que consulta el clima basandose en la clave de la ciudad proporcionada por el usuario
        y por la llave de la API que también será proporcionada por el usuario, partiendo de esto, este método
        checa las anteriores entradas que se han registrado en el cache para así poder realizar más busquedas 
        desde la API."""
        ciudadProporcionada = str(self.elementos.formas["entrada_ciudad"].get()).upper()
        llaveProporcionada = str(self.elementos.formas["entrada_llave"].get())
        self.solicitudes.recibir_llave(llaveProporcionada)

        if self.cache.consultar_cache(ciudadProporcionada) != False:
            self.elementos.textos['coordenadas'].configure(text=self.cache.consultar_cache(ciudadProporcionada))
            return

        self.solicitudes.recibir_llave(llaveProporcionada)
        if ciudadProporcionada in self.baseDatos.dic_origen:
            self.solicitudes.crear_url(self.baseDatos.dic_origen[ciudadProporcionada][0],self.baseDatos.dic_origen[ciudadProporcionada][1])
            if self.solicitudes.obtener_clima():
                dato = self.solicitudes.obtener_clima()
                self.cache.guardar_cache(ciudadProporcionada,dato)
                self.result()
                return
            else :
                self.elementos.textos['coordenadas'].configure(text="Error con la llave proporcionada")
                return
        elif ciudadProporcionada in self.baseDatos.dic_destino:
            self.solicitudes.crear_url(self.baseDatos.dic_destino[0],self.baseDatos.dic_destino[1])
            if self.solicitudes.obtener_clima :
                dato = self.solicitudes.obtener_clima()
                self.cache.guardar_cache(ciudadProporcionada,dato)
                self.result()
                return
            else :
                self.elementos.textos['coordenadas'].configure(text="Error con la llave proporcionada")
                return
        else :
            self.elementos.textos['coordenadas'].configure(text="La clave de la ciudad no sirve")
            return

    def reiniciar(self):
        """Método que funciona para poder reiniciar las consultas."""
        self.cache.borrar_cache()
        

