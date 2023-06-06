### Python Syntax ###
def do_nothing(): 
    pass # "pass" ist ein Platzhalter, der nichts tut, aber syntaktisch korrekt ist!



## Einrückungen ##
"""

Das markanteste Feature der Python-Skriptsprache ist wohl der komplette Wegfall
von Semikolons als "End of Line"-Symbol. 

Funktionale Ebenen innerhalb des Codes werden durch Indents (Einrückungen) markiert. 

"""

# ACHTUNG! Einrückungen sind nicht optional! Bitte daran denken! Einrückungen sind für Python 
# essentiell und werden auch von der Ausführung des Codes berücksichtigt! Bitte daran denken!

def indents():
    eingabe = input("Bitte geben Sie keine Vollzahl ein: ")
    if eingabe.isdigit() is False:
        try:
            print(eingabe + " ist keine Vollzahl. Vielen Dank!")
        except:
            print("Ihre Eingabe verwirrt mich.")
        print()
    else:
        print("Bitte KEINE Vollzahl!")
        for j in range(3):
            print()

# Weiterhin: Immer dieselbe Einrückung (Tab- oder Space-Anzahl) verwenden! Bitte daran denken! 
# Bitte!
# Bitte daran denken! Bitte daran denken! Bitte denken Sie daran! Bitte daran denken!



## Variablen ##
"""

Anders als beispielsweise C# ist Python (so wie JavaScript) schwach typisiert. 
Das Konzept der Deklarierung und der Initialisierung ist Python also fremd. 
Variablen werden stattdessen durch das bloße Zuweisen eines Wertes definiert.

"""
def variables(n = 42):
    i = "Holundergeruch"
    c = 3.14159
    e = False
    return [n,i,c,e]


## Type Hints ##
"""

Seit Python 3.5 sind "Type Hints" möglich um Variablendeklarationen zu imitieren.
Vorteil ist hier die leichtere Fehlerbehandlung und einfachere Lesbarkeit bei 
komplexeren Programmen. Type Hints sind in jedem Fall optional, können aber abhängig
von der gewählten Entwicklungsumgebung das Coden vereinfachen.

"""
def type_hints(n: int = 42) -> list:
    i: str = "Hamstervater"
    c: float = 3.14159
    e: bool = False
    return [n,i,c,e]



## Casting- und Type-Funktionen ##
"""

Casting und Typinformationen abrufen sind in Python der jeweiligen Datentypklasse implizite 
Funktionen. 

Zum Casten wird also der Name des Zieldatentyps verwendet, als Argument der zu
castende Wert (oder Variable) angegeben, und zurückgegeben wird das Argument im neuem
Zieldatentyp.

also:   x = str(42) -> x = "42" (String)

"""
def casting(f = "42"):
    u = int(f) -41
    n = [type(f), type(u)]
    return [f,u,n]


## Namenskonventionen ##
"""

Folgende Namenskonventionen sind für Python üblich:

    * PascalCase                Klassen
    * snake_case                Variablen, Funktionen, Methoden, Module
    * SCREAMING_SNAKE_CASE      Konstante

Diese Namenskonventionen haben ihren Ursprung in der PEP 8, der Python Style Guide:
    
    https://www.python.org/dev/peps/pep-0008/
    
"""
def naming():
    import y0_this_is_my_module
    class ThisIsMyClass:
        def this_is_its_method():
            THIS_IS_A_CONSTANT = 42
            this_is_a_variable = "Caerbannog"





