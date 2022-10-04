# PROYECTO 01.
## Cruz Campos Eduardo                          319312087
## Martínez Herrera Miguel Agustín              319180114

- - - -

DESCRIPCION:
Consiste en implementar una interfaz gráfica para consultar el clima a partir de claves de ciudades y una llave de OpenWeather.

Para correr el proyecto se necesita tener ciertos requerimento para hacer su funcionamiento optimo y eficiente, primero que nada vamos a necesitar tener instalado Python3, en caso de no tenerlo lo podemos descargar de la siguiente forma:
    Para Linux: 
        Para Debia, Ubuntu y derivados:
            $ sudo apt install python3
        Para Fedora:
            $ sudo dnf install python3
    Para Windows:
        Se necesita descargar desde el siguiente link, abrir la descarga y seguir el proceso de instalación.
        https://www.python.org/downloads/
    Para MacOs:
        Se necesita descargar desde el siguiente link, abrir la descarga y seguir el proceso de instalación.
        https://www.python.org/downloads/ 

Posteriormente para poder hacer que funcione necesitamos descargar algunas librerias de Python que ocupamos en la programación, estas librerias las descargaremos desde la terminal:
    ------------------------------TKINTER------------------------------
        Para Linux:
            Para Debia, Ubuntu y derivados: 
                & Sudo apt-get install python3-tk
            Para Fedora: 
                sudo dnf install tk
        Para Windows:
            Para poder instalar debemos consultar https://es.acervolima.com/como-instalar-tkinter-en-windows/
        Para MacOs:
            Para poder instalar debemos consultar https://www.geeksforgeeks.org/how-to-install-tkinter-on-macos/

Se debe estar ubicado dentro de la carpeta Proyecto01-Beta, a la altura de la carpeta Proyecto01, del pdf y del readme, luego ejecutar en la terminal el comando:

    $ python3 Proyecto01/src/main.py

Para correr las pruebas se tiene que estar ubicado dentro de la carpeta Proyecto01-Beta, a la altura de la carpeta Proyecto01, del pdf y del readme, luego ejecutar los siguientes comandos:

    $ python3 Proyecto01/test/test_solicitud.py 
    $ python3 Proyecto01/test/test_baseDeDatos.py 
    $ python3 Proyecto01/test/test_solicitud.py 
    Para correr cache se necesita remplazar  en el archivo cache.py la linea 1 por:
    from src.solicitud import *
    despues correr el siguiente comando:
    $ python3 Proyecto01/test/test_cache.py 
    "NOTA: se deja sin este import porque no lograria reconocer el modulo al momento de correr el main. :(
        
Referencias:
    Para crear Base De Datos se consultó :
        Leer archivo CSV con Python. (2020, 9 noviembre). Parzibyte's blog. Recuperado 3 de octubre de 2022, de https://parzibyte.me/blog/2020/11/09/leer-archivo-csv-python/
    
    Para realizar las pruebas se consultó :
        unittest — Unit testing framework — Python 3.10.7 documentation. (s. f.). Recuperado 3 de octubre de 2022, de https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises

