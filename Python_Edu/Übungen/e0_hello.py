### Python Aufgaben zu Lektion 0 - Hello Python ###

"""

Aufgabe 1 (~5 Minuten):
Wieso sollte man mehr als nur eine Sprache lernen? Schreiben Sie hierzu 5 Stichpunkte auf.

"""
def aufgabe_0_1():
    stichwort_1 = ""
    stichwort_2 = ""
    stichwort_3 = ""
    stichwort_4 = ""
    stichwort_5 = ""
    return f"Gründe mehr als nur eine Programmiersprache zu lernen:\n\t*{stichwort_1}\n\t*{stichwort_2}\n\t*{stichwort_3}\n\t*{stichwort_4}\n\t*{stichwort_5}\n\n"



"""

Aufgabe 2 (~10 Minuten): 
Welche Unterschiede zu C# fallen Ihnen direkt auf? Schreiben Sie sich 
2 Unterschiede auf und recherchieren Sie die Gründe für die Unterschiede im Internet.

"""
def aufgabe_0_2():
    unterschied_1 = ""
    gruende_unterschied_1 = ["","",""]
    unterschied_2 = ""
    gruende_unterschied_2 = ["","",""]

    antwort = "Der erste Unterschied zu C#: "+unterschied_1+"\n"
    for i in range(len(gruende_unterschied_1)):
        antwort += f"\tGrund {i+1}: "+gruende_unterschied_1[i]+"\n"
    antwort += "\n" + "Der zweite Unterschied zu C#: " + unterschied_2 + "\n"
    for i in range(len(gruende_unterschied_2)):
        antwort += f"\tGrund {i+1}: "+gruende_unterschied_2[i]+"\n"

    return antwort



"""

Aufgabe 3 (~10 Minuten):
Welche Anwendungen fallen Ihnen ein, bei denen Python nützlich sein könnte? 
Schreiben Sie eine Liste mit mindestens 5 Anwendungen auf und notieren Sie kurz, 
warum Python hier eine gute Wahl wäre.

"""
def aufgabe_0_3():
    anwendungen = {
        "anwendung 1": "begruendung 1",
        "anwendung 2": "begruendung 2",
        "anwendung 3": "begruendung 3",
        "anwendung 4": "begruendung 4",
        "anwendung 5": "begruendung 5"
    }

    for anwendung, begruendung in anwendungen.items():
        print(f"{anwendung}: {begruendung}")