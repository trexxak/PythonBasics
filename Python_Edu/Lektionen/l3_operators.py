### Python Operatoren ###
operator_chain = 1 < 2 < 3 < 4 < 5 > 4 > 3 > 2 > 1 >= 0 <= 1

## Arithmetische Operatoren ##
"""

    +   Addition
    -   Subtraktion
    *   Multiplikation
    /   Division (wie immer mit Vorsicht zu genießen!)
    %   Modulo
    **  Exponential (NICHT ^!) 
    //  "Floor Division" (NICHT Wurzel!) (Ganzzahlteilung)

"""


def calculus(zahl_1:int, operator:str, zahl_2:int): 
    match operator:
        case "*":
            return zahl_1 * zahl_2
        case "/":
            return zahl_1 / zahl_2
        case "+":
            return zahl_1 + zahl_2
        case "-":
            return zahl_1 - zahl_2
        case "**":
            return zahl_1 ** zahl_2
        case "//":
            return zahl_1 // zahl_2
        case "%":
            return zahl_1 % zahl_2
        case _:
            return f"{operator} ist kein arithmetischer Operator."


## Zuweisungsoperatoren ##
"""

    x = 0       weist der Variablen einen Wert zu.
    x += 1      weist der Variable ihren um den rechten Wert inkrementierten Wert zu.
    x -= 2      weist der Variable ihren um den rechten Wert dekrementierten Wert zu.
    x *= 3      weist der Variable ihren um den rechten Wert multiplizierten Wert zu.
    x /= 4      weist der Variable ihren um den rechten Wert dividierten Wert zu.
    x %= 5      weist der Variable ihren um den rechten Wert modulierten Wert zu.
    x **= 6     weist der Variable ihren um den rechten Wert potenzierten Wert zu.
    x //= 7     Zuweisung mit "Floor Division".

"""
def count_up_then_down():
    for i in range(0,10000,1):
        if i < 10000:
            i+=1
        print(i)
    for j in range(9999,0,-1):
        if j > 0:
            j-=1
        print(j)


## Vergleichsoperatoren ##
"""

    ==      gleicht
    !=      gleicht nicht
    >       größer als
    <       kleiner als
    >=      größer gleich
    <=      kleiner gleich

"""
def reality_check():
    if 2 + 2 == 5 \
    or 5 != 2 + 3 \
    or 5 < 5 \
    or 2 + 2 > 2 + 2 \
    or 5 >= 5 + 1 \
    or 2 + 3 <= 2 + 2:
        print("You've just entered Room 101.")



## Logische Operatoren ##
"""

    and     ist wahr, wenn beide Aussagen wahr sind.
    or      ist wahr, wenn eine der beiden Aussagen wahr ist.
    not     ist wahr, wenn die Aussage falsch ist.

"""
def collision_detection(entity_position = {"x": 16, "y": 0}, wall_position = {"x": 16, "y": 0}):
    if entity_position["x"] == wall_position["x"] and entity_position["y"] == wall_position["y"]:
        return True
    else: 
        return False



## Identitätsoperatoren ##
"""

    is      ist wahr, wenn sich beide Variablen auf dasselbe Objekt beziehen.
    is not  ist wahr, wenn sich beide Variablen nicht auf dasselbe Objekt beziehen.

    (Hinweis: Boolsche Werte werden mit Identitätsoperatoren überprüft.)

"""
def collision_handler(entity_is_ghost = True):
    if collision_detection() is True and entity_is_ghost is not False:
        print("collision method (nyi)")


## Zugehörigkeitsoperatoren ##
"""

    in      ist wahr, wenn das Element im Elternobjekt vorhanden ist.
    not in  ist wahr, wenn das Element nicht im Elternobjekt vorhanden ist.

"""
def numbered_list(itemlist = ["Collect underpants", "?", "Profit"]):
    counter = 0
    for item in itemlist:
        counter += 1
        print(f"Phase {counter}:\t{item}\n")



## Bitwise Operatoren ##
"""

    Bitwise-Operatoren werden verwendet, um auf den Bitmuster von Ganzzahlen zu arbeiten. 
    Es gibt sechs Bitwise-Operatoren in Python:

        &   AND         Setzt jeden Bit auf 1, wenn beide Bits 1 sind.

        |   OR          Setzt jeden Bit auf 1, wenn mindestens ein Bit 1 ist.

        ^   XOR         Setzt jeden Bit auf 1, wenn NUR ein Bit 1 ist.
        
        ~   NOT         Invertiert alle Bits

        <<  Left Shift  Verschiebt Bits nach links um eine bestimmte Anzahl von Stellen.
        
        >>  Right Shift Verschiebt Bits nach rechts um eine bestimmte Anzahl von Stellen.

    Bitwise-Operatoren werden häufig in eingebetteten Systemen und
    Treiberprogrammen verwendet, da sie schnell sind und auf der Hardwareebene arbeiten.
    
    Für die meisten Anwendungen sind Bitwise-Operatoren nicht erforderlich. Auch Python 
    verwendet nur selten Bitwise-Operatoren.

"""

def bitwise_operations():

    print("\n AND Setzt jeden Bit auf 1, wenn beide Bits 1 sind.")
    print(0 & 0)
    print(0 & 1)
    print(1 & 0)
    print(1 & 1)

    print("\n OR Setzt jeden Bit auf 1, wenn mindestens ein Bit 1 ist.")
    print(0 | 0)
    print(0 | 1)
    print(1 | 0)
    print(1 | 1)

    print("\n XOR Setzt jeden Bit auf 1, wenn NUR ein Bit 1 ist")
    print(0 ^ 0)
    print(0 ^ 1)
    print(1 ^ 0)
    print(1 ^ 1)

    print("\n NOT Invertiert alle Bits")
    print(~0)
    print(~1)

    print("\n Left Shift Verschiebt Bits nach links um eine bestimmte Anzahl von Stellen.")
    print(0 << 1)
    print(1 << 1)

    print("\n Right Shift Verschiebt Bits nach rechts um eine bestimmte Anzahl von Stellen.")
    print(0 >> 1)
    print(1 >> 1)
