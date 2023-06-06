### Python Kontrollstrukturen und Funktionen ###

def lost_control(x, y, z):
    return (x + y + z) if x > y else (x - y + z) if y > z else (x * y * z) if x != y and y != z else x == y and y == z and z == x

## Kontrollstrukturen ##
"""
Kontrollstrukturen ermöglichen es, Entscheidungen und Bedingungen in den Ablauf eines 
Python-Programms einzubauen. Hierzu zählen unter anderem if-, else-, elif-, 
und while-Anweisungen.

Eine if-Anweisung ermöglicht es, Code in Abhängigkeit einer Bedingung auszuführen. 
Ist die Bedingung wahr, wird der Code innerhalb des if-Blocks ausgeführt, 
ansonsten wird er übersprungen.

elif- und else-Anweisungen können im Anschluss an eine if-Anweisung verwendet werden, 
um weitere Bedingungen abzudecken. elif steht für else if.

"""

def control_structures_example():
    number = int(input("Geben Sie eine Zahl ein: "))
    if number > 10:
        print("Die Zahl ist größer als 10.")
    elif number < 10:
        print("Die Zahl ist kleiner als 10.")
    else:
        print("Die Zahl ist 10.")

## Funktionen ##
"""
Funktionen sind ein wichtiger Bestandteil von Python und ermöglichen es, 
Code zu strukturieren und wiederzuverwenden.

Eine Funktion wird mit dem def-Schlüsselwort definiert und kann Parameter entgegennehmen 
und Rückgabewerte liefern.

Das Schlüsselwort return gibt einen Wert zurück, der von der Funktion berechnet wurde.

Das Schlüsselwort pass ist ein Platzhalter, der verwendet wird, wenn noch keine 
Funktionalität implementiert wurde.

"""

def sum_numbers(a, b):
    return a + b

def pass_this():
    pass


## Schleifen ##
"""
Schleifen sind eine Möglichkeit, um Code wiederholt auszuführen. 
Es gibt zwei Arten von Schleifen: for-Schleifen und while-Schleifen.

Eine for-Schleife wird verwendet, um eine Liste, ein Tupel oder einen anderen 
iterierbaren Datentyp zu durchlaufen. Dabei wird der Code innerhalb der Schleife 
einmal für jedes Element im iterierbaren Datentyp ausgeführt.

Eine while-Schleife wird solange ausgeführt, wie eine Bedingung wahr ist.

"""

def loops_example():
# for-Schleife
    for i in range(10):
        print(i)
    # while-Schleife
        i = 0
        while i < 10:
            print(i)
            i += 1

list = [0, "auto", 3.3]


# foreach
for item in list:
    print(item)