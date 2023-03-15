### Python Aufgaben zu Lektion 3 - Operatoren ###

"""

Aufgabe 1 (~5 Minuten):
Schreiben Sie eine Funktion, die alle "Power Of Two" (Zweierpotenz) Zahlen bis 
zu einer Potenz n ausgibt.

also: 2, 4, 8, 16, 32, 64, 128 etc.

"""
def aufgabe_3_1(n: int):
    for i in range(1,n+1):
        print(2**i)


"""

Aufgabe 2 (~10 Minuten):
Schreiben Sie eine Funktion, die einen übergebenen Ganzzahlparameter darauf überprüft, 
ob er eine "Power of Two"-Zahl darstellt, die Zahl also das Ergebnis einer 
beliebigen Ganzzahl potenziert mit 2 ist.


"""
def aufgabe_3_2(n: int):
    pass



"""

Aufgabe 3 (~15 - 45 Minuten):
Schreiben Sie eine Funktion, die jeden Vokal (Umlaut und "Y" inklusive) eines Strings mit "o" 
austauscht, und den letzten Konsonanten des Strings mit "g".

"""
def aufgabe_3_3(string):
    resultat = ""
    for char in string:
        if char in "aeoiu":
            resultat += "o"
        else:
            resultat += char
    # for vokal in ["e","a","i","o","u"]:
    #     resultat = string.replace(vokal,"o")
    print(resultat)




"""

Aufgabe 4 (~20 Minuten):
Schreiben Sie einen Passwortgenerator mit folgenden Vorgaben. Das generierte Passwort soll
10 - 16 Zeichen lang sein, davon sollen 1 - 2 Großbuchstaben, 1 - 3 Zahlen und 
1 - 2 Sonderzeichen enthalten sein.

Tipp: Das Python-inklusive Modul "Random" liefert hierfür nützliche Funktionen wie randint(), 
shuffle() und choice(). 

"""
def aufgabe_3_4():
    import random
    return ""
