#importation des librairies
import pygame
import random
import os
import time
from time import strftime
#from horloge import*


pygame.init()

#fonction
#verification de la reponse par rapport à la solution
def reponse(solution,choix):
    reponse = [0,0] #le premier represente le nombre de noir et le deuxieme le nombre de blanc
    print(solution,"\n")
    for k in range(4):
        if solution[k] == choix[k]:
            reponse[0]+=1
        elif choix[k] in solution:
            reponse[1]+=1
    return reponse

def heure():
    today = strftime("%H:%M:%S", time.localtime())
    return today[0] + today[1]

def minute():
    today = strftime("%H:%M:%S", time.localtime())
    return today[3] + today[4]

def seconde():
    today = strftime("%H:%M:%S", time.localtime())
    return today[6] + today [7]


def afficher():
    texte = font.render((heure() + ' H ' + minute() + 'min ' + seconde() + ' s'), True, (0, 0, 0), (18, 65, 120))
    texteRect = texte.get_rect()
    texteRect.center = (500,500)
    ecran.blit(texte, texteRect)


#initialistation de la fenetre
ecran = pygame.display.set_mode((1500,700))
ecran.fill((18, 65, 120))

#initialisation du texte
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)

#variables
continuer = True
aceuil = True
couleur_code = [(0, 0 ,0), (0, 255, 0), (255, 0, 0),(0, 0, 255), (255, 255, 255), (255, 255, 0)]
couleur = ['Noir','Vert','Rouge','Bleu','Blanc','Jaune']
noir_blanc = [(0, 0, 0), (255, 255, 255)]
coordonne_couleur = [(1340, 90), (1340, 160), (1400, 90), (1400, 160),(1460,90),(1460,160)]
coordonne_historique = [(100,100)]
coordonne_repere = (70,30)
solution_cache_nombre = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]
solution_cache = [couleur[solution_cache_nombre[0]],couleur[solution_cache_nombre[1]], couleur[solution_cache_nombre[2]], couleur[solution_cache_nombre[3]]]
repere = 0
liste_reponse = []
repere_valider = 30
valider_verification = False
retour_verification = False
ligne = 0
nombre_de_ligne = 1
infini = 0

#initialistation des images
dirMain = os.path.dirname(os.path.abspath(__file__)) + "\\"
valider = pygame.image.load(dirMain + "valider.jpg").convert_alpha()
#taille de valider : 253x128
retour = pygame.image.load(dirMain + "retour.jpg").convert_alpha()
#taille de retour : 162x48
felicitation = pygame.image.load(dirMain + "Felicitations.jpg").convert_alpha()
#taille de felicitation : 410x82
couleur_image = pygame.image.load(dirMain + "couleur.jpg").convert_alpha()
#taille de couleur_image : 240x77
quiter = pygame.image.load(dirMain + "quitter.jpg").convert_alpha()
#taille de quiter : 177x73
horloge = pygame.image.load(dirMain + "horloge.jpg").convert_alpha()
#taille de horloge : 280x86

#script principale
def game_mastermind():
    continuer = True
    aceuil = True
    couleur_code = [(0, 0, 0), (0, 255, 0), (255, 0, 0),(0, 0, 255), (255, 255, 255), (255, 255, 0)]
    couleur = ['Noir', 'Vert', 'Rouge', 'Bleu', 'Blanc', 'Jaune']
    noir_blanc = [(0, 0, 0), (255, 255, 255)]
    coordonne_couleur = [(1340, 90), (1340, 160), (1400, 90),(1400, 160), (1460, 90), (1460, 160)]
    coordonne_repere = (70, 30)
    solution_cache_nombre = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]
    solution_cache = [couleur[solution_cache_nombre[0]], couleur[solution_cache_nombre[1]],couleur[solution_cache_nombre[2]], couleur[solution_cache_nombre[3]]]
    repere = 0
    liste_reponse = []
    repere_valider = 30
    valider_verification = False
    retour_verification = False
    ligne = 0
    nombre_de_ligne = 1
    while continuer:
        afficher()
        for event in pygame.event.get():
            if aceuil == True:
                for k in range(6):
                    pygame.draw.circle(ecran,couleur_code[k],coordonne_couleur[k],25,0)
                ecran.blit(couleur_image,(1050,90))
                ecran.blit(quiter,(1323,627))
                ecran.blit(horloge, (1200,500))
            if event.type == pygame.QUIT:
                continuer = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                posSouris = pygame.mouse.get_pos() #donne un tuple contenat les coordonnée de la souris lorsque le clic droit a été effectué
                for k in range(6):
                    if posSouris[0] > coordonne_couleur[k][0]-25 and posSouris[0] < coordonne_couleur[k][0]+25 and posSouris[1] > coordonne_couleur[k][1]-25 and posSouris[1] < coordonne_couleur[k][1]+25:#couleur
                        if repere < 6:
                            pygame.draw.circle(ecran,couleur_code[k],coordonne_repere,25,0)
                            liste_reponse.append(couleur[k])
                            repere1 = coordonne_repere[0]
                            repere2 = coordonne_repere[1]
                            repere += 0.5
                            if repere >= 5:
                                repere1 = 0
                                coordonne_repere = (repere1 + 70, repere2 + 70)
                                ecran.blit(valider, (1235, 195))
                                valider_verification = True
                                ligne += 70
                                nombre_de_ligne += 1
                                pygame.draw.rect(ecran, (18, 65, 120), (1338, 0, 162, 48))
                            else:
                                coordonne_repere = (repere1 + 70, repere2)
                                ecran.blit(retour, (1338, 0))
                                retour_verification = True
                            repere += 1
                if posSouris[0] > 1338 and posSouris[0] < 1500 and posSouris[1] > 0 and posSouris[1] < 48:#retour
                    if retour_verification == True:
                        pygame.draw.rect(ecran, (18, 65, 120),(35,ligne,320,60))
                        retour_verification = False
                        liste_reponse = []
                        coordonne_repere = (70, 51 * nombre_de_ligne)
                        repere = 0
                if posSouris[0] > 1235 and posSouris[0] < 1488 and posSouris[1] > 195 and posSouris[1] < 313:#valider
                    if valider_verification == True:
                        pygame.draw.rect(ecran, (18, 65, 120), (1235, 195, 253, 128))
                        pygame.draw.rect(ecran, (18, 65, 120), (1338, 0, 162, 48))
                        liste_noir_blanc = reponse(solution_cache,liste_reponse)
                        repere_reponse=450
                        for k in range(liste_noir_blanc[0]):
                            pygame.draw.circle(ecran, noir_blanc[0],(repere_reponse,repere_valider), 25)
                            repere_reponse += 70
                        for k in range(liste_noir_blanc[1]):
                            pygame.draw.circle(ecran, noir_blanc[1],(repere_reponse,repere_valider),25)
                            repere_reponse += 70
                        liste_reponse = []
                        repere_valider += 70
                        repere = 0
                        valider_verification = False
                        if liste_noir_blanc[0] == 4:
                            ecran.blit(felicitation, (775,200))
                            repere = 10
                if posSouris[0] > 1323 and posSouris[0] < 1500 and posSouris[1] > 627 and posSouris[1] < 700: #quitter
                    continuer = False
            pygame.display.update()
    pygame.quit()

game_mastermind()