### Python Aufgaben zu Lektion 7 - Dateibearbeitung ###

"""

Aufgabe 1 (~5 Minuten):
Schreiben Sie in "y2_playground.txt" den in der Variable "encoded_text" geschriebenen Text.

"""
def aufgabe_7_1():
    encoded_text = "ohssvcvthuklyluluklklzbualyypjoazwyvglzzlz!pjozpagloplybukklurlüilyilzvuklyzkbttlalealuhjo!pjoohiltpynlmüosaqlklusvyltpwzbtnlulyhavyptulaghunlzjohbabukipugbtzjosbzznlrvttlu!khzzpjokvjosplilyzlsizalpulubuzpuuzaleazjoylpil!"



"""

Aufgabe 2 (~10 Minuten):
Ändern Sie den Text in "y2_playground.txt" dahingehend, dass nach jedem 5. Zeichen
ein Whitespace (Leerzeichen) steht.

"""
def aufgabe_7_2():
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



"""

Aufgabe 3 (~15 Minuten):
Schreiben Sie ein Programm zur Dekodierung des Textes in "y2_playground.txt".

Tipp: Cesar Shift +7.

"""
def aufgabe_7_3():
    pass