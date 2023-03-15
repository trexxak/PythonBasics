"""

Aufgabe 3 (~15 Minuten):
Was würde Sie besonders interessieren mit Python zu schreiben? 
Finden Sie im Internet das dafür notwendige Modul, 
importieren Sie es und schreiben Sie ein Minimalprogramm.
(ein sogenanntes "Hello World").

"""
def aufgabe_0_3():
    import random # Ändern Sie "random" zu Ihrem gewünschten Modulnamen
    print(f"Du würfelst: {random.randint(1,6)}") # Ändern Sie den Code um das gewünsche Modul zu demonstrieren

def aufgabe_0_3():
    import pygame
    pygame.init()
    surface = pygame.display.set_mode((256, 256))
    surface.fill((255,0,255))
    pygame.display.flip()
