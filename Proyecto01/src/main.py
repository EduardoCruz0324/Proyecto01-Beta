from ast import Break
from importlib.metadata import entry_points
from re import A
from webbrowser import get
from baseDeDatos import *
from cache import *
from solicitud import *
from interfaz import *
from tkinter import*
from tkinter import ttk
#Crear Objetos
def main():
    """Método que llama a la interfaz y hace funcionar el programa."""
    interfaz=Interfaz()
    interfaz.raiz.mainloop()

if __name__ == "__main__":
    main()

