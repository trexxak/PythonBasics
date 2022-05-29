### Python Aufgaben zu Lektion 4 - Aufzählungen ###

"""

Aufgabe 1 (~5 Minuten):
Lesen Sie die erste Zeile der Funktion aufmerksam durch, führen Sie sie aus, und weisen
Sie ihre Interpretation des Codes der Variable "antwort" zu.

"""
def aufgabe_4_1(**kwargs):
    [kwargs.update({f"{i} + {i} =": i+i}) if i % 2 == 0 else kwargs.update({f"{i} * -{i} =": i*-i}) for i in range(10)]
    antwort = """  """
    print(antwort)
    return kwargs



"""

Aufgabe 2 (~10 Minuten):
Geben sie "MARZIPAN" nur durch Aneinanderreihung der "s"-Werte, 
und "MACHWERK" nur durch Aneinanderreihung der "t"-Werte aus.

"""
def aufgabe_4_2():
    o = {
        "A":
        {
            "A":
            {
                "A":
                {
                    "s": "A",
                    "t": "K",
                },

                "B":
                {
                    "s": "M",
                    "t": "E",
                }
            },

            "B":
            {
                "A":
                {
                    "s": "A",
                    "t": "R",
                },

                "B":
                {
                    "s": "P",
                    "t": "C",
                }
            }
        },
        "B":
        {
            "A":
            {
                "A":
                {
                    "s": "R",
                    "t": "H",
                },

                "B":
                {
                    "s": "I",
                    "t": "W",
                }
            },

            "B":
            {
                "A":
                {
                    "s": "N",
                    "t": "A",
                },

                "B":
                {
                    "s": "Z",
                    "t": "M",
                }
            }
        },

    }
    print()



"""

Aufgabe 3 (~15 Minuten):
    Geben Sie anhand einer Parameterübergabe eine 5x5-Zeichen große "Karte" aus.
    Hindernisse sollen durch ein "x" markiert werden, die eigene Position durch ein "o"
    und alle freien Stellen durch ein " ".

Beispiel für die Ausgabe: 
    
    x xxx
    xo  x
    xxx x
        x
    xxxxx

"""
def aufgabe_4_3(own_position: tuple = (1,1), free_spaces: tuple = ((0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0))):
    map = {}
    display = ""
    print(display)
