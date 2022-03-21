import random

### Python Datentypen ###
false = "true"
false is True if false is False else false is False



## Überblick ##
"""

Python erlaubt, neben speziellen Fällen, folgende primitive Datentypen:

    Zahlen:
        * Ganzzahlen        int         42
        * Gleitkommazahlen  float       3.14159
        * Komplexe Zahlen   complex     1 + 1j

    Text:                   
        * Zeichenketten     str         "Bello", 'bellt'

    Logische Werte:
        * Boolean           bool        True, False

    Aufzählungen:
        * Liste             list        ["Apfel", "Birne", "Mango"]
        * Tupel             tuple       ("Apfel", "Birne", "Mango")
        * Set               set         {"Apfel", "Birne", "Mango"}

        * Wörterbuch        dict        {Key: Value, Key: Value, Key: Value}
    

"""
def get_data():
    name = input("Name: ")
    age = int(input("Alter: "))
    is_of_legal_age = False if age < 18 else True
    data = {"Name": name, "Volljährig": is_of_legal_age}
    return data



## Zahlen ##
"""

Zahlen jeglichen Datentyps können problemlos miteinander operieren. 
Hierbei nimmt das Ergebnis den jeweils komplexesten Datentyp an, also
in der Reihenfolge: int -> float -> complex.

Eine komplexe Zahl besteht aus einer reelen Zahl (etwa 1) und einer imaginären Zahl (etwa 1j).
Der imaginäre Teilwert wird mit einem "j" hinter der Zahl markiert.

Achtung: Komplexe Zahlen lassen sich (ohne Weiteres) NICHT mit Vergleichsoperatoren verwenden!

"""
def calculate_damage(base_damage: int, damage_modifier: float, crit_chance: float):
    buffed_damage = base_damage * (1 + damage_modifier)
    if random.random() < crit_chance:
        print("CRIT!")
        return 1.5 * buffed_damage
    else:
        return buffed_damage

"""

Es lässt sich eine Gleitkommazahl in eine Ganzzahl casten und umgekehrt.
Gleitkommazahlen und Ganzzahlen lassen sich ebenfalls in Komplexe Zahlen casten.

Komplexe Zahlen lassen sich jedoch nicht (ohne Weiteres) in einen anderen Zahlentyp umwandeln!

"""
def casting_works():
    print(int(1.337), float(42), complex(1.337), complex(42))

def casting_fails():
    print(int(4j+4), float(4j+4))

"""

Das math-Modul bietet einige erweiterte mathematische Methoden und mathematische Konstanten:

Konstanten:

    * math.pi       Kreiszahl Pi        float
    * math.tau      Tau (2 * Pi)        float
    * math.e        Euler'sche Zahl     float
    * math.inf      Positiv Unendlich   float
    * math.nan      "Not A Number"      float
    
Nützliche math-Methoden:

    * math.pow(zahl1, zahl2)    gibt zahl1 potenziert mit zahl2 zurück.
    * math.sqrt(zahl)           gibt die Quadratwurzel aus "zahl" zurück.
    * math.fsum(collection)     gibt die Summe aller Zahlen einer Collection zurück.
    * math.gcd(zahl1, zahl2)    gibt den kleinsten gemeinsamen Nenner zweier Ganzzahlen zurück.
    
"""
def more_math():
    import math

    PI = math.pi
    E = math.e
    constants = (PI, E)
    numbers = (9,180)

    print(f"{PI} hoch {E} ist:\n{math.pow(PI,E)}")
    print(f"Die Quadratwurzel aus {numbers[0]} ist:\n{math.sqrt(numbers[0])}")
    print(f"Alle Zahlen in {constants} aufsummiert ist:\n{math.fsum(constants)}")
    print(f"Der kleinste gemeinsame Nenner von {numbers[0]} und {numbers[1]} ist:\n{math.gcd(numbers[0],numbers[1])}")

## Strings ##
"""

Merkmale:

    * Strings werden durch "" oder '' markiert 
        (jedoch nicht gemischt - "string' wird nicht erkannt).
    * Strings in Python sind implizit Abfolgen einzelner Zeichen, 
        die jedoch ebenfalls als String gespeichert sind.
    * Verbatim Strings können durch dreifache doppelte Anführungszeichen markiert werden. 
    * Verkettung zwischen Strings erfolgt durch den '+'-Operator.
    * Strings können entweder durch die "format()"-Methode oder 
        durch f-String formatiert werden.

"""
def vertical_string(string: str = "What is the airspeed velocity of an unladen 'swallow'?"):
    my_string = string
    for char in my_string:
        print(char)

def verbatim_string():
    ascii_art = """
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;,,;;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,,;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,;;:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::;;;;;,,,;;;;::::ccccccc:::;;,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,;;:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::ccccccccc:::;::ccccccccccccccccccc::;,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:ccccccccccclllllllccccccccccccccccccccc:;;,,,,,,,,,,,,,
    ,,,,,,,,,,,;:;;,;;;;;;;;;;;;;;;;;;;;;;;;;;:cclcloddddxxxkkkkkkkxxxxxddolccccccccccccc:;,,,,,,,,,,,,,
    ,,,,,,,,,;::;,;;;;;;;;;;;;;;;;;;;;;;;;;::ccllcoxOOOOOOkkOkkkkkkkkkkOOOOkxolcccccccccc:;,,,,,,,,,,,,,
    ,,,,,,,;;:;,,;;;;;;;;;;;;;;;;;;::::::cccllllclxOkxxddddooxkdlcllllodkkkkOkxocclcccc::;,,,,,,,,,,,,,,
    ,,,,,;;:;;,,,;;;;;;;;;;;;;;;;:ccclllllooolllcokOkoll:;,;:dkxc,,,:loxkkkkkkkxlcccc:,,,,;,,,,,,,,,,,,,
    ,,,,;;:;,,,,,;,,,;;;;;;;;;;;::ccllooooooollccdOOkkkkl,''cxOkl,',cxOkkkkkkkOxlcccc;,''',,;,,,,,,,,,,,
    ,,,,;;,,,,,,,,,,,,,;;;;;;;;;;:cclllloooollcccdOOkkkko,''cxOkl,',cxOkkkkkkkOxlccccc;,,'',,,,,,,,,,,,,
    ,,,;;,,,,,,,,,,,,,,;;;;;;;;;;;:cccccllllllcccokOkkkkd;',cxOko;,;lkOOkkkkkkOkdccccccc:;;,,,,,,,,,,,,,
    ,,,;;,,,,,,,,,,,,,;;;;;;;;;;;;;;::cccllllccccdkOkkkOkdooxkOOkxddkOOkkxdddddxkxoccccllccc:::;;,,,,,,,
    ,,;:;,,,,,,,,,,,,,,,;;;,,;;;;;;;;:cclllllccoxkkkkOOOOOOOOOOOOOOOkkkkkkOOkxdodOkdccclllllcccc:;,,,,,,
    ,,;:;,,,,,,,,,,,,,,,,;;;;::::::cccclllllcldxdoodxxxxxxxxkkkxxxxkkO0KXNNXKOkolxOOdccllllllccc:;,,,,,,
    ,,;;;,,,,,,,,,,,,,,,;;:cccccccclllllllcclddodxO0K000OOkkkkOOO00KXXNNNNNNX0kdldkOxlcclllllcccc;;,,,,,
    ,,;;,,,,,,,,,,,,,,,;:ccccccclllllllllcccddoxOKNNNNNNNNNNNNNNNNNNNNNNNNNNX0kdldkOxlcclllllccc:;;,,,,,
    ,,;;,,,,,,,,,,,,,,;:ccccclllllllllllccclxdox0XNNNNNNNNNNNNNNNNNNNNNNNNNXX0koldOOdcccllllccc:,,;,,,,,
    ,,;;,,,,,,,,,,,,,,;cccccllcccccccllllcclxkdox0XNNNNNNNNNNNNNNNNNNNNNNNXXKOdlokkdlccllllccc:,,,,,,,,,
    ,,;;,,,,,,,,,,,,,,;ccccccc:;;,,;:cclllccokOxodkKXXNNNNNNNNNNNNNNNNNNNXXKOdloxkolcccllllccc:,,,;,,,,,
    ,,;;,,,,,,,,,,,,'.':ccc:;,'.....',:clllccokOkxddxkO0KKXXXXXNNNNNNXXXXK0xoloxdlccc:::ccccccc:;;,,,,,,
    ,;:;,,,,,,,,,,,::;'';;,'..........,;clllccldkkOkxddddxxkkkkkO00000Okxdolclolcccc:,'';:cccccc:;,,,,,,
    ,;;,,,,,,,,,,coxkxoc:;,''..........',;::::;;::cloddxxdooolllooollcc:;;,,,';ccccc;'...;cccccc:;,,,,,,
    ,;;,,,,,,,,;lxOOOOOOOkkxoc;,''.......'''''''...':oxxkxo:;;;,,,,'''''.....',;:::,'....,:cccc:;;,,,,,,
    ,,;;,,,,,,,cxOOOOOOOOOOOOOkkxd:'..............,lkOOOO0kc'...................''......':ccc::;;,,,,,,,
    ,,;;,,',,,,cxOOOOOOOOOOOOOOOOOkl,'...........'ckOOOOOOOo,...................';lllllc:cccl:,,;,,,,,,,
    ,,;;,',,,,,;lxOOOOOOOOOOOOOOOOOOxo:,'........,oOOOOOOOOl'.......'............:k000Oxooddxd:,,,,,,,,,
    ,,,;;,,,,,,,,:ldkOOOOOOOOOOOOOOOOOkxl:,'.....;xOOOOOOOx:'....................,d0OOOOkkkxkxl;,,,,,,,,
    ,,,,;;,,,,,,,,,;:ldxkOOOOOOOOOOOOOOOOOxoc;'',okOOOOOOOkxoc,..................'oO0OOOkkkxxkd:,,,,,,,,
    ,,,,,;;,,,,,,,,,,,,;::codkOOOOOOOOOOOOOOOkxdxkOOOOOOOOOOOOkl,................'dOOOOOkkkxkkd:,,,,,,,,
    ,,,,,;;;,,,,,,,,,,'.....',;cldxkOOOOOOOOOOOOOOOOOOOOOOOOOOOOo,...............:k0OOOkkkkkkxo;,,,,,,,,
    ,,,,,,;;,,,,,,,,'.............',:codxkOOOOOOOOOOOOOOOOOOOO00kc..............:xOOOOOkkkkkko:,,,,,,,,,
    ,,,,,,,;;;,,,,,'....................';:cldxkkOOOOOOOOOOOO000Oc...........':okOOOOOkkkkkxo:;,,,,,,,,,
    ,,,,,,,,;;;,,,'...........................',;:clxOOOOOOOOO0Od,........,:okO00OOOkkkkkxdc;,,,,,,,,,,,
    ,,,,,,,,,;;,,'..................................,codkOOO0Oxl,......,:okO00OOOOOOkkkxo:;,,,,,,,,,,,,,
    ,,,,,,,,,,,;;'.....................................';cool:,......;okO00OOOOOOOkkkdc,',,,,,,,,,,,,,,,
    ,,,,,,,,,,,,;,.................................................,okO0OOOOOOkkkkdc;'..',,,,,,,,,,,,,,,
    ,,,,,,,,,,,,;,................................................:xOOOOOOOOkkkdc;'...',,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,;,'..............................................;x00OOOOOOkxo;'.....',,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,;,.............................................,dOOOOOOkOkd:......',,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,'...........................................lO0OOOOkkkx:....',,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,'.........................................,xOOOOkkkkko,..',,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,'.......................................;xOOOkkkkkkx:,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,''..................................,dOOkkkkkkkkd:,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''....................'',cxOOkkkkkkkd:,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;coxxkkxxdoc;,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;:cllc:;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    """
    print(ascii_art)

def formatted_string():
    string_1 = "Bello"
    string_2 = "bellt"

    format_a = "{} {}".format(string_1, string_2)
    format_b = "{1} {0}".format(string_2, string_1)
    format_c = f"{string_1} {string_2}"

    print(format_a + " " + format_b + " " + format_c)

def formatted_number_string(zahl):
    with_decimals = f"{zahl:.2f}"
    as_percentage = f"{zahl:.0%}"
    print(zahl, with_decimals, as_percentage)

"""

Nützliche String-Methoden:

    length = len(my_string)
        Gibt die Länge der Zeichenkette zurück.

    if "abc" in my_string:
        Prüft das Vorkommen des Substrings "abc" in my_string.

    new_string = my_string[2-8]
        Gibt einen neuen String startend mit Index 2 und endend
        mit Index 8 des alten Strings zurück.

    new_string = my_string.upper()
        Gibt den String in GROßSCHRIFT zurück.

    new_string = my_string.lower()
        Gibt den String in kleinschrift zurück.

    new_string = "ANANAS".replace("NA","P")
        ersetzt vorkommende "NA"-Substrings mit "P".
    
    book_info = "1984, George Orwell, Dystopie".split(",")
        Gibt eine am ","-Zeichen separierte Liste an Substrings zurück.
        (also: ["1984", " George Orwell", " Dystopie"])
    
    clear_string = " Hallo Welt ".strip()
        Entfernt Whitespaces vor und hinter einer Zeichenkette.
        (also: "Hallo Welt")

"""
def string_methods():
    target_string = ""
    target_list = []

    original_string = "He's not pining, he's passed on. This parrot is no more. He has ceased to be. He's expired and gone to meet his maker. He's a stiff, bereft of life, he rests in peace. If you hadn't have nailed him to the perch he'd be pushing up the daisies. He's rung down the curtain and joined the choir invisible. This is an ex-parrot."
    string_in_uppercase = original_string.upper()
    modified_string = string_in_uppercase.replace("HE", "ARTHAS")
    modified_string = modified_string.replace("PARROT", "ARTHAS")
    string_list = modified_string.split(".")
    for substring in string_list:
        substring = substring.strip()
        if "TARTHAS" not in substring and "" != substring: 
            target_list.append(substring)
    
    for i in range(len(target_list)-1,0,-1):
        target_string += target_list[i] + "\n"
    print(target_string.lower())

"""

Um entweder das Ausgabeformat des String grundlegend zu modifizieren oder um
spezielle Zeichen innerhalb eines Strings zu verwenden, gibt es die Möglichkeit das
Escape Zeichen Backslash zu verwenden. Mit Backslash sind also folgende
Escape-Sequenzen möglich:

    * \'    einfache Anführungszeichen      Ausgabe: '
    * \"    doppelte Anführungszeichen      Ausgabe: "
    * \\    Backslash                       Ausgabe: \
    * \n    Zeilenumbruch                   
    * \t    Tabulator
    * \b    Backspace                       Beispiel: "A\bBCD" -> "BCD"
    * \f    "Form Feed", nächste Seite      obsolet!
    * \000  Oktalwert                       0 steht hier für Ziffern von 0-7
    * \x00  Hexadezimalwert                 x gefolgt von zwei Hexadezimalziffer 0-F

"""
def escape_sequences():
    print("C:\\Users\\Admin\\FilmQuotes\\TheRoom_2003.mp4\b\b\b\b.avi")
    print("Tommy: \"Ha\tha\tha\tha. \n\tWhat \ta \tstory \tMark!\"")



## Logische Werte ## 
"""

    Die meisten Werte korrelieren mit dem Wahrheitswert "True".

    Ausnahmen: 
        False     ist Falsch  Boolscher Wert
        None      ist None    Boolscher Wert
        0         ist None    Ganzzahl
        ""        ist None    String
        ()        ist None    Tupel
        []        ist None    Liste
        {}        ist None    Set oder Wörterbuch

"""
def check_bool_value(parameter):
    argument = parameter
    if argument:
        return True
    elif argument is False:
        return False
    elif argument is None:
        return None
