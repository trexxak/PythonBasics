### Python Aufgaben zu Lektion 5 - Klassen ###

"""

Aufgabe 1 (~5 Minuten):
Stellen Sie sich eine einfache Vererbungsbeziehung vor und stellen Sie sie durch
Einsatz von Klassen abstrakt dar.

"""
def aufgabe_5_1():
    class Pass:
        pass



"""

Aufgabe 2 (~10 Minuten):
Stellen Sie die Beziehungen einer Unterrichtssituation dar. Schreiben Sie mindestens je eine
Eigenschaft und eine Methode pro Klasse.

"""
def aufgabe_5_2():

    class Person():
        def __init__(self, name: str, alter: int):
            self.name = name
            self.alter = alter
        def wie_alt(self):
            print(f"{self.name} ist {self.alter} alt.")

    class Raum():
        def __init__(self, stockwerk: int, personen_platz: int, nummer: int):
            self.stockwerk = stockwerk
            self.personen_platz = personen_platz
            self.nummer = nummer
        def wo_ist(self):
            print(f"Der Raum befindet sich in der {self.stockwerk}. Etage. "+ 
            f"Es ist das {self.nummer}. Zimmer und verfügt Platz "+
            f"für {self.personen_platz} Personen.")

    class Lehrer(Person):
        def __init__(self, name, alter, unterrichtsfaecher):
            super().__init__(name, alter)
            self.unterrichtsfaecher = unterrichtsfaecher
        def lehrt_was(self):
            print_string = f"{self.name} unterrichtet:"
            for item in self.unterrichtsfaecher:
                print_string += "\n\t"+item 
            print(print_string)

    class Schueler(Person):
        def __init__(self, name, alter, stufe: int, noten: dict):
            super().__init__(name, alter)
            self.stufe = stufe
            self.noten = noten
        def welche_noten(self):
            print(f"{self.name} ist in der {self.stufe}.")

    class Unterricht(Raum):
        def __init__(self, stockwerk, personen_platz, nummer, fach, uhrzeit, schueler, lehrer):
            super().__init__(stockwerk, personen_platz, nummer)
            self.fach = fach
            self.uhrzeit = uhrzeit
            self.schueler = schueler
            self.lehrer = lehrer
        def wann_und_was_und_wer(self):
            printstring = f"Um {self.uhrzeit[0]} - {self.uhrzeit[1]} findet dieser Unterricht statt.\n"
            printstring += f"{self.lehrer.name} leitet den Unterricht zu {self.fach}.\n"
            printstring += "Folgende Schüler sind für den Unterricht eingetragen:"
            for item in self.schueler:
                printstring += f"\n\t{item.name}"
            print(printstring)

    def scenario():
        t_0 = Lehrer("Frank",49,["Englisch", "Deutsch","Mathe"])
        s_0 = Schueler("Emil",18,10,{"Deutsch": 4, "Englisch": 3, "Mathe": 2})
        s_1 = Schueler("Dörte",18,10,{"Deutsch": 2, "Englisch": 2, "Mathe": 4})
        s_2 = Schueler("Bernd",19,10,{"Deutsch": 5, "Englisch": 3, "Mathe": 4})
        s_3 = Schueler("Chris", 20, 10,{"Deutsch": 5, "Englisch": 5, "Mathe": 4})
        s_4 = Schueler("Alex", 19, 10,{"Deutsch": 2, "Englisch": 2, "Mathe": 1})
        u_0 = Unterricht(0,6,2,"Mathe",(8,12),[s_0,s_1,s_2,s_3,s_4],t_0)

        u_0.wo_ist()
        u_0.wann_und_was_und_wer()
    
    scenario()
