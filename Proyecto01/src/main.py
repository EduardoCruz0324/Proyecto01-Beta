from baseDeDatos import *
from cache import *
from solicitud import *
from interfaz import *
from tkinter import*
def main():
    """Método que llama a la interfaz y hace funcionar el programa."""
    interfaz=Interfaz()
    interfaz.raiz.mainloop()

if __name__ == "__main__":
    main()

