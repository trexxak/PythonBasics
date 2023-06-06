def aufgabe_0_1():

    stichwort_1 = "Anpassungsfähigkeit"

    stichwort_2 = "Unterschiedlicher Nutzen"

    stichwort_3 = "Abstraktes Denken trainieren"

    stichwort_4 = "Marktnachfrage"

    stichwort_5 = "Persönliche Präferenz entdecken"

    return f"Gründe mehr als nur eine Programmiersprache zu lernen:\n\t*{stichwort_1}\n\t*{stichwort_2}\n\t*{stichwort_3}\n\t*{stichwort_4}\n\t*{stichwort_5}\n\n"



def aufgabe_0_2():

    unterschied_1 = "Python lässt sich mit weniger Aufwand schreiben"
    gruende_unterschied_1 = ["Python ist eine Skriptsprache", "C# ist eine kompilierte Sprache", "Pythons Ursprung liegt in funktionaler Programmierung"]

    unterschied_2 = "Python ist einfacher zu lesen"
    gruende_unterschied_2 = ["Pythons Syntaxkonzeption beruht auf Englisch", "C# entstammt älteren Programmiersprachen", "Wegfall von '{}' und ';'"]

    antwort = "Der erste Unterschied zu C#: "+unterschied_1+"\n"
    for i in range(len(gruende_unterschied_1)):
        antwort += f"\tGrund {i+1}: "+gruende_unterschied_1[i]+"\n"

    antwort += "\n" + "Der zweite Unterschied zu C#: " + unterschied_2 + "\n"
    for i in range(len(gruende_unterschied_2)):
        antwort += f"\tGrund {i+1}: "+gruende_unterschied_2[i]+"\n"

    return antwort



def aufgabe_0_3():
    anwendungen = {

        "Automatisierung von Aufgaben": "Python ist ideal für die Automatisierung von Routineaufgaben, da es in der Lage ist, sich mit anderen Anwendungen zu verbinden.",

        "Webentwicklung": "Python ist in der Webentwicklung weit verbreitet und wird häufig verwendet, um Webanwendungen zu entwickeln.",

        "Datenanalyse und -visualisierung": "Python bietet eine Vielzahl von Bibliotheken, um Daten zu analysieren und zu visualisieren, wie zum Beispiel Pandas und Matplotlib.",

        "Künstliche Intelligenz und maschinelles Lernen": "Python ist die bevorzugte Sprache für KI- und ML-Entwickler aufgrund seiner einfachen Syntax und der Verfügbarkeit von Bibliotheken wie TensorFlow und Keras.",

        "Spielentwicklung": "Python bietet verschiedene Bibliotheken und Frameworks wie Pygame, um 2D- und 3D-Spiele zu entwickeln.",
    }

    for anwendung, begruendung in anwendungen.items():
        print(f"{anwendung}: {begruendung}")



def aufgabe_1_1():
    my_name = input("Geben Sie Ihren Namen ein:\t")
    print("Hello " + my_name)



def aufgabe_1_2(variable: int):
    MY_CONSTANT = 3.177
    my_variable = variable
    if (my_variable + MY_CONSTANT) > 0: 
        my_bool = True
    else:
        my_bool = False
    print(my_bool)



def aufgabe_1_3():

    list_of_numbers = []
    for i in range(1, 11):
        new_number = input(f"Geben Sie die {i}. Zahl ein:\t")
        list_of_numbers.append(new_number)

    for i in range(1, len(list_of_numbers)+1):
        number = float(list_of_numbers[i-1])
        if number < 0:
           print("B")
        elif number % 2 != 0:
           print("O")
        else:
           print("G")



def aufgabe_2_1(string):
    my_string = string
    for char in my_string:
        print(char)



def aufgabe_2_2(title, heading, paragraph, list, image_url, *style):
    
    style_string = ""
    for arg in style:
        style_string += arg
    
    style_content = f"<style>{style_string}</style>"    
    head_content = f"<title>{title}</title>\n"
    html_head = f"<head>\n{head_content}{style_content}\n</head>\n"
    body_content = f"<h1>{heading}</h1>\n"

    body_content += f'<img src="{image_url}">\n'

    body_content += f"<p>{paragraph}</p>\n"

    body_content += "<ul>\n"
    for item in list:
        body_content += f"<li>{item}</li>\n"
    body_content += "</ul>"
    
    html_body = f"<body>\n{body_content}\n</body>"
    full_html = "<!DOCTYPE html>\n<html>\n"+html_head+html_body+"\n</html>"
    return full_html

# print(aufgabe_2_2("Titel", "Heading", "Lorem Ipsum", ["eins","zwei","drei"],"image.png","abc"))

# import webbrowser

# html=aufgabe_2_2("Trexxak's lustige Seite",
#         "Was macht der so?",
#         "Meist nicht viel:",
#         ["Programmieren","Schlafen","Kaffee trinken"],
#         "https://static.jam.vg/raw/98b/d2/z/486c8.png",
#         "h1{color: #63897a; font-size: 64px}",
#         "p{color: #a0dec5; background-color: #82b3a0; font-size: 52px}",
#         "ul{color: #63897a; list-style-type: none; margin: 0; padding: 0;}",
#         "li{font-size: 32px;}"
#         "body{font-family: Papyrus; color: #63897a; text-align: center; background-color: #a0dec5}")

# f = open("y1_playground.html", "w")
# f.write(html)
# f.close()

# webbrowser.open("y1_playground.html")

def aufgabe_2_3(html_page: str):

    list_of_elements = html_page.split("<img")
    print(list_of_elements) 
    for item in list_of_elements:
        if "src" in item: 
            pic = item.split(">")
            print(pic[0])



def aufgabe_3_1(n: int):
    for i in range(0,n+1):
        result = 2**i
        print(f"Potenz{i}:\t2^{i}\t{result}")



def aufgabe_3_2(n: int):
    # print(n & (n - 1) == 0) # Profi-Antwort
    check = False
    for i in range(1,n+1):
        if 2**i == n:
            check = True
            break
    if check:
        print(f"Bei {n} handelt es sich um eine PoT-Zahl.")
    else:
        print(f"{n} ist keine PoT-Zahl.")



def aufgabe_3_3(string):
    w_string = ""
    for i in range(0, len(string)):
        if string[i] in ["a","e","i","o","u","ö","ü","ä","y"]:
            w_string += "o"
        else:
            w_string += string[i]

    n_string = []
    stop = False
    for i in range(len(string)-1,-1,-1):
        if w_string[i] not in ["a","e","i","o","u","ö","ü","ä","y"] and stop is False:
            n_string.append("g")
            stop = True
        else:
            n_string.append(w_string[i])
    
    n_string.reverse()
    return "".join(n_string)



def aufgabe_3_4():
    import random as r
    pw_length = r.randint(10,16)
    upper_char_count = r.randint(1,2)
    special_char_count = r.randint(1,2)
    number_char_count = r.randint(1,3)
    sum_char_counts = upper_char_count+special_char_count+number_char_count

    random_password = ""
    for i in range(upper_char_count): 
        random_password += r.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(special_char_count): 
        random_password += r.choice("!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~.")
    for i in range(number_char_count): 
        random_password += r.choice("0123456789")
    for i in range(pw_length - sum_char_counts):
        random_password += r.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())

    random_password = list(random_password)
    r.shuffle(random_password)
    return "".join(random_password)



def aufgabe_4_1(list_of_numbers):
    sum_of_evens = 0
    for num in list_of_numbers:
        if num % 2 == 0:
            sum_of_evens += num
    return sum_of_evens



def aufgabe_4_2(list_of_strings):
    input = ["Hallo", "Welt", "Python", "Programmieren", "ist", "toll"]
    for string in list_of_strings:
        if len(string) >= 5:
            print(string)



def aufgabe_5_1(**kwargs):
    [kwargs.update({f"{i} + {i} =": i+i}) if i % 2 == 0 else kwargs.update({f"{i} - {i} =": i*-i}) for i in range(10)]
    antwort = """ 
    Für Index i von 0 - 10, füge dem Wörterbuch den Schlüssel "i + i =" mit dem Wert "i+i" hinzu, wenn es sich bei
    i um eine runde Zahl handelt, sonst füge dem Wörterbuch den Schlüssel "i - i =" mit dem Wert "i*-i" hinzu.
    
    Prinzipiell also nichts Weiteres als:

    for i in range(10):
        if i % 2 == 0:
            kwargs.update({f"{i} + {i} =": i+i})
        else:
            kwargs.update({f"{i} - {i} =": i*-i})
    
    """
    print(antwort)
    return kwargs



def aufgabe_5_2():
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
    print(
        f'{o["A"]["A"]["B"]["s"]}'
        f'{o["A"]["A"]["A"]["s"]}'
        f'{o["B"]["A"]["A"]["s"]}'
        f'{o["B"]["B"]["B"]["s"]}'
        f'{o["B"]["A"]["B"]["s"]}'
        f'{o["A"]["B"]["B"]["s"]}'
        f'{o["A"]["A"]["A"]["s"]}'
        f'{o["B"]["B"]["A"]["s"]}'
        '\n'
        f'{o["B"]["B"]["B"]["t"]}'
        f'{o["B"]["B"]["A"]["t"]}'
        f'{o["A"]["B"]["B"]["t"]}'
        f'{o["B"]["A"]["A"]["t"]}'
        f'{o["B"]["A"]["B"]["t"]}'
        f'{o["A"]["A"]["B"]["t"]}'
        f'{o["A"]["B"]["A"]["t"]}'
        f'{o["A"]["A"]["A"]["t"]}'
        )



def aufgabe_5_3(own_position: tuple = (1,1), free_spaces: tuple = ((0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0))):
    map = {}
    for i in range(5):
        map.update({f"row {i+1}": []})
        for j in range(5):
            map[f"row {i+1}"].append({f"col {j+1}": {"pos": (i,j), "obs": None}, "player": None})
            if (i,j) in free_spaces:                
                map[f"row {i+1}"][j][f"col {j+1}"]["obs"] = False
            else:
                map[f"row {i+1}"][j][f"col {j+1}"]["obs"] = True
    
    display = ""
    for row in map.keys():
        display += "\n"
        for i in range(len(row)):
            if map[row][i][f"col {i+1}"]["obs"]:
                display += "x"
            elif map[row][i][f"col {i+1}"]["pos"] == own_position:
                display += "o"
            else:
                display += " "
    print(display)



def aufgabe_6_1():
    class Hund:
        pass
    class Dackel(Hund):
        pass
    wolfi = Dackel()



def aufgabe_6_2():

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



def aufgabe_7_1():
    import datetime
    greeting_with_datetime = datetime.datetime.now().strftime("Today is %A, %d. of %B, %Y.\nYour local time is %H:%M")
    return print(greeting_with_datetime)



def aufgabe_7_2():
    import y0_this_is_my_module
    y0_this_is_my_module.dummy_function()



def aufgabe_7_3():
    import numpy as np
    random_array = np.random.normal(10,5,(3,3)).astype(int)
    print(random_array)



def aufgabe_8_1():
    encoded_text = "ohssvcvthuklyluluklklzbualyypjoazwyvglzzlzpjozpagloplybukklurlblilyilzvuklyzkbttlalealuhjopjoohiltpynlmblosaqlklusvyltpwzbtnlulyhavyptulaghunlzjohbabukipugbtzjosbzznlrvttlukhzzpjokvjosplilyzlsizalpulubuzpuuzaleazjoylpil"
    with open("y2_playground.txt","w") as file:
        file.write(encoded_text)



def aufgabe_8_2():
    counter = 0
    changed_string = ""

    with open("y2_playground.txt","r") as file:
        string_to_change = file.read()
    
    for i in range(len(string_to_change)):
        changed_string += string_to_change[i]
        counter +=1
        if counter % 5 == 0:
            changed_string += " " 

    with open("y2_playground.txt","w") as file:
        file.write(changed_string)



def aufgabe_8_3():
    with open("y2_playground.txt","r") as file:
        string_to_change = file.read()
    temp_string = string_to_change.replace(" ","")
    final_string = ""
    for i in range(len(temp_string)):
        char = temp_string[i]
        final_string += chr((ord(char) -7 - 97) % 26 + 97)
    with open("y2_playground.txt","w") as file:
        file.write(final_string)
