#?#?#    THEMA:   LILA      #?#?#

"""

Der Trexx-Jam ist ein Wettbewerbs unter angehenden Anwendungsentwicklern.
Ziel ist es am Ende des Wettbewerbs die höchste Anzahl funktionstüchtiger
Software-Prototypen vorführen zu können, und generell Spaß am Probieren zu haben.

Der Trexx-Jam besteht aus zwei Tagen des kreativen Chaos. Zum Anreiz
wird, wie in Game-Jams üblich, ein Thema bekannt gegeben. Dieses soll aber
lediglich als Denkanreiz, nicht als Qualitätskriterium dienen.

Zulässige Projekte beinhalten alle Challenges aus C0_challenges.py. 
(Spieleprojekte seh ich aber besonders gerne)

"""
def intro_questionmark(name: str):
    print(f"Gratulation {name}! Du bist eingeladen!")

"""

Regeln:
    * Ruhe bewahren
    * Fair bleiben

Ablauf:

    Ab 08:30 des ersten Tages hat jeder Teilnehmer Zeit bis um 16:00 ein MVP 
    (Minimal Viable Product) vorzustellen. Im Anschluss wird jedes Projekt geheim 
    in den Kategorien "Idee", "Code" und "Spaß/ Nützlichkeit" bewertet.

    Am zweiten Tag werden um 08:15 per Zufallsprinzip die MVPs einem jeweilig 
    anderen Teilnehmer übergeben. Die bis 16:00 vervollständigten Projekte 
    werden, wie schon am Vortag, in den Kategorien "Idee", "Code" 
    und "Spaß/ Nützlichkeit" bewertet.

"""
# Tag 0
"""

            08:15   Einladung

            08:30   Projekt
            10:30   Pause I

            11:00   Projekt
            12:00   Mittagspause

            13:00   Halbzeitbesprechung
            13:15   Projekt
            14:30   Pause II

            14:45   Projekt
            16:15   Präsentation und Bewertung
            16:30   Ende Tag 0

"""
# Tag 1
"""

            08:15   Auslosung der Projekte

            08:30   Projekt
            10:30   Pause I

            11:00   Projekt
            12:00   Mittagspause

            13:00   Halbzeitbesprechung
            13:15   Projekt
            14:30   Pause II

            14:45   Projekt
            16:00   Abgabe des vollständigen Projekts und Bewertung
            16:15   Demo und Kundgabe der Ergebnisse
            16:30   Ende Tag 1

"""

























# Bewertungsschema

teilnehmerzahl = 4

def best_daily(trexxaks_bewertung, rest, original_autor_bewertung=0,):

    fun_bewertung  = 0
    fun_bewertung += original_autor_bewertung * 1.5
    fun_bewertung += trexxaks_bewertung * 1.5

    for bewertung in rest:
        fun_bewertung += bewertung

    return fun_bewertung / teilnehmerzahl

def best_project():

    tag_0 = best_daily(3,[2,4])
    tag_1 = best_daily(4,[5,5],4)
    print(tag_0,tag_1)
    gesamt = (tag_0 + tag_1) / 2
    print(gesamt)

def best_winner():
    # dasselbe, aber es ist 10 nach 12 und ich will mich schlafen legen.
    pass

# QnA
"""

QnA

Q: Können wir auch im Team arbeiten?
A: Diesmal nicht, sorry.

Q: Das hört sich ganz schön extrem an?
A: Ist es auch. Ich werde jedoch durch die einzelnen Teilnehmer rotieren und 
gegebenenfalls mithelfen.

Q: Muss ich was aus dem Thema machen?
A: Nein, es ist rein als Denkanreiz gedacht ("Leeres Blatt"-Problem). Sollten Sie 
bereits gute Ideen haben, vergessen Sie das Thema am Besten.

Q: Gibt es einen Preis zum Ansporn?
A: Ihr fertiges Produkt und das gute Gewissen viel gelernt zu haben* :)

"""