### Python Aufgaben zu Lektion 2 - Datentypen ###

"""

Aufgabe 1 (~5 Minuten):
Geben Sie die einzelnen Zeichen eines beliebigen Strings aus 
ohne Escape-Sequenzen zu verwenden.

"""
def aufgabe_2_1(input: str = "Hallo Welt!"):    
    pass



"""

Aufgabe 2 (~10 - 30 Minuten):
Schreiben Sie eine Funktion mit mehreren Parametern, die einen als HTML-formatierten String
zurückliefert. Der String soll einen Titel, ein Heading- und ein Paragraph-Element 
enthalten.

Also:
        <!DOCTYPE html>
        <html>
            <head>
                <title>Titel</title>
            </head>
            <body>
                <h1>Überschrift</h1>
                <p>Lorem Ipsum</p>
                <img src="testpixel.png"/>
            </body>
        </html>

Bonus: Fügen Sie unterhalb des Paragraph-Elements eine ungeordnete Liste hinzu.

Doppel-Bonus: Binden Sie zwischen Überschrift und Paragraph ein Bild aus dem Internet ein.

Dreifach-Bonus: Fügen Sie beliebig viele weitere Parameter ein um CSS-Stilelemente zu bestimmen.


"""
def aufgabe_2_2(title:str, heading:str, paragraph:str): 
    full_html = f"""<!DOCTYPE html>
    
    </html>
    """

    return full_html


"""

Aufgabe 3 (~15 Minuten):
Schreiben Sie einen HTML-Parser, der die eingebundenen Bilder einer einfachen HTML-Seite in 
einer Liste zurückgibt.

"""

def aufgabe_2_3(html_page:str):   

    pictures = [] 
    print(pictures)


beispiel_html = """
<!DOCTYPE html>
<html>
<head>
<title>Meine Webseite :)</title>
</head>
<body>
<h1>Ja was ist das denn?</h1>
<img src="https://via.placeholder.com/1920x1080.png">
<p>Das ist ein Test! Ui!</p>
</body>
</html>
"""

