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
    namensUrsprung = moeglicheAntworten[2] # Zugriff auf Elemente einer Liste, hier: 3. Element
    print(f"Python ist benannt nach {namensUrsprung}!") # f-Strings sind Strings, die Variablen direkt enthalten können


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
    print("Welche Zahl ist 101010 in Dezimal? ")
    eingabe = input() # input ist eine Funktion, die den Benutzer nach einer Eingabe fragt
    if eingabe == "42":
        print("Korrekt!")
    else:
        print("Falsch! Die korrekte Antwort ist 42.")

# Beispiel für die enorme Lesbarkeit von Python
def why_short(): 
    eingabe = input("Welche Zahl ist 101010 in Dezimal? ") # input kann auch direkt mit 
                                                            # einer Frage versehen werden
    print("Korrekt.") if eingabe == "42" else print("Falsch! Die korrekte Antwort ist 42.") 
    # Ternäre Bedingungen: 
    # drucke "Korrekt." wenn eingabe ist 42 sonst drucke "Falsch!" - sehr sprachlich!


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
    os.system("python") # os.system führt einen Befehl in der Shell aus. 
    # In diesem Fall wird Python gestartet.

## Python, aber wo? ##
"""
Wenn du Python noch nicht installiert hast, kannst du es von der offiziellen 
Python-Website herunterladen und installieren.

https://www.python.org/downloads/

Um ein Python-Programm auszuführen, musst du es in einer 
Entwicklungsumgebung oder einem Texteditor schreiben. 
Hier sind die Schritte, um ein Python-Programm auszuführen:

1. Schreibe das Programm in deiner Entwicklungsumgebung oder deinem Texteditor.
2. Speichere das Programm als .py-Datei.
3. Öffne die Kommandozeile und navigiere zum Ordner, in dem das Programm gespeichert ist.
4. Gib den Befehl "python <Dateiname>.py" ein und drücke Enter.

Das war's! Dein Programm sollte nun ausgeführt werden.
"""

