### Python Aufzählungen ###
even_numbers = [x for x in range(1,101) if x % 2 == 0]



## Übersicht ##
"""

Aufzählungen ("Collections") können in Python grundsätzlich die Form der Liste, des Tupels und
des Sets annehmen. Auch Strings und Dictionaries sind eigentlich Collections.

Aufzählungen (bis auf Strings) können jeden Datentyp aufnehmen.

"""
def collections():
    tuple_example = ("Winston", "Smith", 52, True)
    list_example = ["Josef", "K.", 46, False]
    set_example = {"Heinrich", "Faust", 72, None}
    dict_example = {"Vorname": "Arthur", "Nachname": "Dent", "Alter": 42, "Lebt": True}
    string_example = "ABCDEFGHIJKLMNOPQURSTUVWXYZ0123456789"
    return [tuple_example, list_example, set_example, dict_example, string_example]



"""

In aller Kürze:

Collection      Liste[]     Tupel()     Set{}       Dict{}      String

geordnet?           Ja          Ja      Nein           *Ja          Ja
indiziert?          Ja          Ja      Nein     Schlüssel          Ja
veränderbar?        Ja        Nein      Nein            Ja        Nein
doppelte Werte?     Ja          Ja      Nein          Nein          Ja
    
"""
def character_sheet():
    all_names = {"Toaster","Fantastico","Mochok"}

    char_from_csv="Mochog,42.2846,Warrior,Human,Lagrand,420.247,1377.573,"\
            "Lame Copper Sword,Invisible Helm of Brilliance,Cool Shirt,-,10,128,12"
    char = char_from_csv.split(",")

    char_position = (char[4], int(float(char[5])), int(float(char[6])))
    
    char_dict = {
                "info":
                    {
                    "name":char[0],
                    "level":int(float(char[1])),
                    "class":char[2],
                    "race":char[3],
                    },
                "location":char_position,
                "stats":
                    {
                    "equipment":
                        {
                        "weapon":char[7],
                        "head":char[8],
                        "chest":char[9],
                        "pants":char[10]
                        },
                    "power":
                        {
                        "agility":int(char[11]),
                        "intelligence":int(char[12]),
                        "strength":int(char[13])
                        }
                    }
                }
    if char_dict["info"]["name"] not in all_names:
        for key in char_dict.keys():
            print("\n"+"* "*3+key.upper()+" *"*3)
            if type(char_dict[key])==dict:
                for subkey in char_dict[key].keys():
                    if type(char_dict[key][subkey])==dict:
                        print("\n"+subkey.upper()+"\n")
                        for item in char_dict[key][subkey].keys():
                            print(f"{item.capitalize()}:\t{char_dict[key][subkey][item]}")
                    else:
                        print(f"{subkey.capitalize()}:\t\t{char_dict[key][subkey]}")
            else:
                print(f"Zone:\t\t{char_dict[key][0]}\nX-Position:\t{char_dict[key][1]}\nY-Position:\t{char_dict[key][2]}")

    else:
        print("Your name is occupied. Please select another name.")



## Ordnung, Index, Veränderbarkeit und Redundanztoleranz ##
"""

Ordnung und Index:

Aufzählungen können geordnet sein, das heißt die Reihenfolge der Elemente bleibt erhalten.
Dies erlaubt den Zugriff auf einzelne Elemente durch ihren jeweiligen Index.
    (Eine Ausnahme stellt hier das Wörterbuch dar, bei dem statt dem Index der Schlüssel 
    gewählt werden muss)

"""
def access_collections():
    tuple_example = ("Winston", "Smith", 52, True)
    list_example = ["Josef", "K.", 46, False]
    set_example = {"Heinrich", "Faust", 72, None}
    dict_example = {"Vorname": "Arthur", "Nachname": "Dent", "Alter": 42, "Lebt": True}
    string_example = "ABCDEFGHIJKLMNOPQURSTUVWXYZ0123456789"

    # TUPLE
    print(tuple_example[0])

    # LIST
    print(list_example[0])

    # SET
    # print(set_example[0])           # nicht geordnet!
    for item in set_example:        # Workaround -> Loop und Konditional -> UNPRAKTIKABEL!
        if "Heinrich" == item:
            print(item)

    # DICT
    # print(dict_example[0])           # nicht indiziert!
    print(dict_example["Vorname"])   # Lösung -> Schlüssel statt Index angeben!

    # STRING
    print(string_example[0])

"""

Veränderbarkeit ("Mutability"):

Bis auf die Liste und das Dictionary, sind einzelne Elemente innerhalb der Aufzählung nach
Aufnahme nicht mehr veränderbar.

"""
def change_collections(data = collections()):
    tuple_example = ("Winston", "Smith", 52, True)
    list_example = ["Josef", "K.", 46, False]
    set_example = {"Heinrich", "Faust", 72, None}
    dict_example = {"Vorname": "Arthur", "Nachname": "Dent", "Alter": 42, "Lebt": True}
    string_example = "ABCDEFGHIJKLMNOPQURSTUVWXYZ0123456789"

    # TUPLE
    #tuple_example[1] = "Lauch"                 # Tupel unveränderbar!
    workaround_list = list(tuple_example)       # Workaround -> Tupel zu Liste casten
    workaround_list[1] = "Lauch"                # Element ändern
    tuple_example = tuple(workaround_list)      # Liste zu Tupel casten
    print(tuple_example[1])
    
    # LISTE
    list_example[1] = "Lauch"
    print(list_example[1])

    # SET
    #set_example[1] = "Lauch"                   # nicht geordnet!
    set_example.remove("Faust")                 # Workaround: 
    set_example.add("Lauch")                    # Entfernen des alten Werts und 
    print(set_example)                          # Hinzufügen des Neuen.

    # DICT
    dict_example["Nachname"] = "Lauch"
    print(dict_example["Nachname"])

    # STRING
    #string_example[1] = "L"                       # String unveränderbar!
    workaround_string = string_example[0]          # Workaround: Erstellung eines neuen Strings
    workaround_string += "L"
    for i in range(2,len(string_example)):
        workaround_string += string_example[i]
    string_example = workaround_string
    print(string_example[1])

"""

Redundanztoleranz:

Doppelte Werte werden in allen Aufzählungen erlaubt, 
jedoch ignorieren Sets doppelte Werte, Wörterbücher
ignorieren doppelte Schlüssel.

"""
def duplicates_in_collections():

    # TUPLE
    tuple_example = ("A","N","A","N","A","S")
    print(tuple_example)

    # LIST
    list_example = ["A","N","A","N","A","S"]
    print(list_example)
    
    # SET
    set_example = {"A","N","A","N","A","S"}
    print(set_example)

    # DICT
    dict_example = {"A": 0,
                    "N": 1,
                    "A": 2,
                    "N": 3,
                    "A": 4,
                    "S": 5}
    print(dict_example)
    
    # STRING
    string_example = "ananas"
    print(string_example)



## Listen ##
"""

Nützliche Funktionen für Listen:

list_a[i] = new_value          ändert den Wert der Liste an Index i zum Wert new_value.

list_a.insert(i, item)         fügt das genannte Item der Liste an Index i hinzu.
list_a.pop(i)                  entfernt das Item der Liste an Index i.

list_a.append(item)            fügt das genannte Item am Ende der Liste hinzu.
list_a.remove(item)            entfernt das genannte Item von der Liste.

list_a = list_one + list_two   kombiniert mehrere Listen zu einer neuen Liste.
list_a.extend(collection)      fügt Elemente einer weiteren Collection am Ende der Liste hinzu.

list_a.count("#")              gibt das Auftreten des angegebenen Werts in der Liste an.

"""
def list_functions(list_length: int):
    list_a = []

    for i in range(list_length):
        list_a.append(i)
        if i % 2 == 0:
            list_a.remove(i)
    for i in range(list_length):
        if i % 2 != 0:
            list_a.insert(i-1,i-1)

    # Reihenfolge - immer wichtig!
    list_a.pop(int(list_length/2))
    list_a.pop(0)
    list_a.pop()
        
    print(list_a)



## Tupel ##
"""

Nützliche Funktionen für Tupel:

tuple_a.append(item)    fügt das genannte item dem Tupel zu.
tuple_a.count(item)     gibt den Zählwert des vorgekommenen Wertes zurück.

a,b,c = tuple_a         entpackt die kommagetrennten Variablen in einen Tupel.

"""
def tuple_functions(*tuple_a):
    a,b,c,d = tuple_a
    [print(item) for item in tuple_a]
    print(tuple_a)
    print(f"42 kommt im angegebenen Tupel {tuple_a.count(42)} mal vor.")



## Sets ##
"""

Nützliche Funktionen für Sets:

set_a.add(item)                                 fügt das benannte Item dem Set hinzu.

set_a.update(set_b)                             erweitert das erste Set um ein zweites.
set_a = set_b.union(set_c)                      ^dasselbe, nur mit Deklaration eines dritten Sets.

set_a.symmetric_difference_update(set_b)        erweitert das erste Set um ein zweites, und entfernt redundante Elemente.
set_a = set_b.symmetric_difference(set_c)       ^dasselbe, nur mit Deklaration eines dritten Sets.

set_a.intersection_update(set_b)                erweitert das erste Set um ein zweites, und entfernt einzigartige Elemente.
set_a = set_b.intersection(set_c)               ^dasselbe, nur mit Deklaration eines dritten Sets.

set_a.discard(item)                             entfernt das benannte Item aus dem Set.
set_a.clear()                                   entfernt alle Elemente des Sets.

"""
def set_functions(set_a = {1,2,3,4,5}, set_b = {3,4,5,6,7}):
    all_elements = set_a.union(set_b)
    unique_elements = set_a.symmetric_difference(set_b)
    intersecting_elements = set_a.intersection(set_b)
    print(all_elements, "\n", unique_elements, "\n", intersecting_elements)



## Wörterbücher ##
"""

Nützliche Funktionen für Wörterbücher:

dict_a["key"] = new_value               weist dem Wörterbuchschlüssel einen (neuen) Wert zu.
dict_a.update({"key": new_value})       fügt dem Wörterbuch ein Schlüssel-Wert Paar hinzu oder ändert es.

dict_a = dict_b.copy()                  weist dem Wörterbuch eine Kopie eines anderen Wörterbuchs zu.                  
dict_a.pop("key")                       entfernt den Schlüssel (und zugehörige Werte) aus dem Wörterbuch.
dict_a.clear()                          entfernt alle Schlüssel (und zugehörige Werte) aus dem Wörterbuch.

"""
def dict_functions(dict_length=4,**dict_a):
    [dict_a.update({f"{i} hoch {i}": i**i}) for i in range(1,dict_length+1)]
    [print(f"{key} = {dict_a[key]}") for key in dict_a.keys()]
