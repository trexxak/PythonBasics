### Python Aufgaben zu Lektion - Kontrollstrukturen ###

"""
Aufgabe 1 (~10 Minuten):
Schreiben Sie eine Python-Funktion, die eine Liste von Zahlen als Parameter entgegennimmt und
die Summe aller geraden Zahlen in der Liste zurückgibt.

Beispiel:
input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output: 30 (2+4+6+8+10)

"""
def aufgabe_z_1(list_of_numbers):
    sum_of_evens = 0
    for num in list_of_numbers:
        if num % 2 == 0:
            sum_of_evens += num
            return sum_of_evens

"""
Aufgabe 2 (~15 Minuten):
Schreiben Sie eine Python-Funktion, die eine Liste von Strings als Parameter entgegennimmt und
alle Strings ausgibt, die mindestens 5 Zeichen lang sind.

Beispiel:
input: ["Hallo", "Welt", "Python", "Programmieren", "ist", "toll"]
output: "Hallo" und "Programmieren"

"""
def aufgabe_1_2(list_of_strings):
    for string in list_of_strings:
        if len(string) >= 5:
            print(string)