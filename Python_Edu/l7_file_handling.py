### Dateibearbeitung ###
with open("z1_todo.txt") as file:
    print(file.read())



"""

Folgende Argumente können dem Filestream übergeben werden:

    r   Read    Datei Lesen             Das Dokument wird gelesen (Defaultwert)

    x   Create  Datei Erstellen         Fehlerrückgabe falls Datei bereits vorhanden.
    w   Write   Datei (über)schreiben   Überschreibung falls Datei bereits vorhanden.
    a   Append  Datei erweitern         Erweiterung der Datei am Ende des Dokuments.

Ein mit "r" geöffnetes Dokument, kann durch read() (und andere Methoden) gelesen werden.

Ein mit "x", "w" und "a" geöffnetes Dokument, kann durch write(string) beschrieben werden.

Das zweite Argument des Filestreams kann "t" für text oder "b" für binary darstellen. Hierbei
ist "t" der default-Wert und muss deswegen nicht angeführt werden.

Um ein Dokument zu löschen muss das "os"-Modul importiert und seine remove() Funktion
ausgeführt werden. 

"""
def read_and_return(doc) -> str:
    f = open(doc)
    string = f.read()
    f.close()
    return string

def write_in_mode(mode, doc, string):
    f = open(doc,mode)
    f.write(string)
    f.close()

def delete_doc(doc):
    import os
    os.remove(doc)

"""
Häufig ist sowohl Lese- als auch Schreibberechtigung bei dem Bearbeiten von Dateien erwünscht.
Um das gewünschte Verhalten zu erreichen sind folgende Argument"kombinationen" möglich:

    r+      Datei Lesen und überschreibend erweitern.

        -> Fehlerrückgabe falls Datei nicht vorhanden.  
        -> Der "Cursor" wird an den Anfang des Dokuments platziert.

    w+      Datei überschreiben und Lesen.

        -> Erstellt neue Datei falls nicht vorhanden.
        -> Überschreibt neue Datei falls vorhanden.

    a+      Datei erweitern und Lesen.

        -> Erstellt neue Datei falls nicht vorhanden.
        -> Der "Cursor" wird an das Ende des Dokuments platziert.
    
"""

"""

Das "with" Keyword beinhaltet dieselben Funktionen und ist eine Zeile kürzer.
Das Schließen wird hier automatisch übernommen.
Fehler (etwa bei dem Versuch ein Dokument mit "x" zu erstellen das bereits existiert)
werden gehandlet und führen nicht zu einer Beendigung der Ausführung.

"""
def create_with_with(doc: str="y1_playground.html"):
    with open(doc,"x") as file:
        file.write("Trexxak was Here")
