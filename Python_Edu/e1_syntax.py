### Python Aufgaben zu Lektion 1 - Syntax ###

"""

Aufgabe 1 (~5 Minuten):
Schreiben Sie die auskommentierte C#-Funktion in ausführbaren Python-Code um.

Tipp: Schauen Sie sich die Python-Dokumentation zur input()-Funktion an: 
https://python-reference.readthedocs.io/en/latest/docs/functions/input.html


#void aufgabe_1_1()
#{
#string my_name = Console.ReadLine();
#Console.WriteLine("Hello, "+ my_name);
#}

"""
def aufgabe_1_1():
    pass



"""

Aufgabe 2 (~10 Minuten): 
a) Korrigieren Sie die Syntaxfehler der auskommentierten Funktion 
b) Bringen Sie die Bestandteile in eine leichter lesbare Form (Namenskonventionen).

#     def AufgabeEinsZweixD(konstante : Int):
# MEINEVARIABLE = 3.177;
#     meine_konstante = konstantee
#         if MEINEVARIABLE + meine_konstante > 0:
#             XxmEiN__bOoL__wErTxX = 1
#                 else
#                     {
#                         bool XxmEiN__bOoL__wErTxX = 0
#                     }
#   XxmEiN__bOoL__wErTxX.print()

"""
def aufgabe_1_2():
    pass



"""

Aufgabe 3 (~15 Minuten):
Vervollständigen Sie die Funktion, um bei geraden Zahlen "G" auszugeben, bei ungeraden Zahlen "O",
und bei negativen Zahlen "B".

Tipp:

if ...:
    print("?")
elif ...:
    print("?")
else:
    print("?")

"""
def aufgabe_1_3():

    ### Eingabe ###
    list_of_numbers = []
    for i in range(1, 11):
        new_number = input(f"Geben Sie die {i}. Zahl ein:\t")
        list_of_numbers.append(new_number)

    ### Ausgabe ###
    for i in range(1, len(list_of_numbers)+1):
        pass
