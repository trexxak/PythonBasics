### Python Module ###
import re                           # importiert das Modul "re".
from webbrowser import open         # importiert aus dem Modul "webbrowser" die Funktion "open".
from datetime import *              # importiert ALLES aus dem Modul "datetime".
from platform import system as plt  # importiert aus dem Modul "platform" die Funktion "system" mit dem Bezeichner "plt".



## Built-In Module ##
"""

Python liefert bereits einige Module mit, die vor Verwendung gesondert importiert werden
müssen. Der Grund hierfür ist einen Funktionsüberfluss und entsprechende 
Performanceeinschränkungen zu verhindern. Eine Liste aller dieser Module findet sich
hier:           
            https://docs.python.org/3/py-modindex.html

"""
def builtin_modules():
    if plt() == "Windows":
        open("https://docs.python.org/3/py-modindex.html")
        print(datetime.now().strftime("Today is %A, %d. of %B, %Y.\nYour local time is %H:%M"))



## Eigene Module ##
"""

Module sind nichts weiter als Python Skripte. Das bedeutet also um eigene Python Skripte
als Module zu laden ist es ausreichend, wenn das gewünschte Modul im selben Ordner
vorliegt. So kann das Skript dann wie ein Modul importiert werden.

"""
def own_modules():
    import y0_this_is_my_module            
    y0_this_is_my_module.dummy_function()



## Externe Module ##
"""

Externe Module sollten über den "pip" Python Packet Manager heruntergeladen werden.
Dies geschieht über die Shell/ Bash über den Befehl:

                pip install <paketname>                 aktuelle Version des Moduls
                    Bsp: pip install numpy

Das Paket wird (wenn nicht virtuelle Umgebungen verwendet werden) im Directory 
"/lib/site-packages" des Python Ordners gespeichert.              

#py -m pip install -> workaround
"""
def external_modules():
    import numpy as np
    arr = np.array([[0,1,0,0], [0,0,1,0]])
    print(arr)