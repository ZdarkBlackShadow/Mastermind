import concurrent.futures
import os
from fonction import*
import pygame
from pygame.locals import *

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


def creer_label(font, texte, couleur, **position):
    surface = font.render(texte, True, couleur)
    rect = surface.get_rect(**position)
    return surface, rect

"""
def get_temp_reading(future):
    i = future_to_temp.index(future)
    temperature = future.result()
    temperatures[i] = temperature
    future = executor.submit(afficheTemp, i)
    future.add_done_callback(get_temp_reading)
    future_to_temp[i] = future


init_temp_probes()
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
future_to_temp = [executor.submit(afficheTemp, i) for i in range(2)]
for future in future_to_temp:
    future.add_done_callback(get_temp_reading)
temperatures = [0, 0]

"""
#Taille de la fenetre
taille_fenetre = (800, 600)
continuer = 1

pygame.init()  # Initialisation de pygame
fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
# Definition de la taille de la fenetre
screen_surface = pygame.display.set_mode(taille_fenetre)

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

timer = pygame.time.Clock()

font = pygame.font.Font(None, 36)  # Police principale
horloge_label, horloge_rect = creer_label(font, str(afficheHeure()),
                                          BLANC, center=fenetre_rect.center)

temperature1_label, temperature1_rect = creer_label(font, "0",
                                                    BLANC, top=fenetre_rect.top)

temperature2_label, temperature2_rect = creer_label(font, "0",
                                                    BLANC, bottom=fenetre_rect.bottom)

pygame.time.set_timer(USEREVENT, 1000)

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            continuer = 0

        elif event.type == USEREVENT:
            horloge_label, horloge_rect = creer_label(font, str(afficheHeure()),
                                                      BLANC, center=fenetre_rect.center)

    dt = timer.tick(30) / 1000

    screen_surface.fill(BLANC)
    screen_surface.blit(horloge_label, horloge_rect)

pygame.quit()
