import os

### Hello Python - Eine Einführung ###
print("Hallo Python!")



## Was ist Python? ##
"""

Python ist eine auf Lesbarkeit ("readability") vom holländischen
Softwareentwickler Guido van Rossum konzipierte Skriptsprache.

Python wird insbesondere häufig in folgenden Kontexten verwendet:

    * Webentwicklung (serverseitig)
    * Wissenschaft und Forschung
    * Künstliche Intelligenz
    * "Rapid Prototyping" (bspw. CAD)
    * "System Scripting" (bspw. Shell- oder Bash-Scripts)

"""
def what():
    moeglicheAntworten = ['der Würgeschlange',
                        'einem Kofferwort',
                        'der britischen Komikergruppe "Monty Python"',
                        'das Inselvolk der Pythonier']
    namensUrsprung = moeglicheAntworten[2]  
    print(f"Python ist benannt nach {namensUrsprung}!")



## Wieso Python? ##
"""

Pythons Vorteile beinhalten unter Anderem:

    * Plattformunabhängige Unterstützung
    * Einprägsame Syntax, dadurch auch für Anfänger geeignet
    * Schnelle Ausführung des Codes, dadurch schnelles Prototypisieren und Debuggen
    * Keine IDE notwendig
    * Open Source
    * Starke Popularität, dadurch reichlich Lern- und Unterstützungsmaterial vorhanden

"""
def why():
    eingabe = input("Welche Zahl ist 101010 in Dezimal? ")
    print("Korrekt.") if eingabe == "42" else print("Falsch.")



## Python, aber wie? ##
"""

Wie schon erwähnt benötigt Python keinerlei IDE, ein Texteditor reicht.
Es lässt sich aber sogar (nach Installation) in der Shell ausführen!

Selbstverständlich macht es Sinn dennoch in einer Entwicklungsumgebung zu schreiben.
Hier eine kleine Auswahl der populärsten Möglichkeiten:

    * Visual Studio / Visual Studio Code
    * IDLE
    * PyCharm
    * Sublime
    * Eclipse mit PyDev
    * Anaconda

"""
def how():
    os.system("python")
