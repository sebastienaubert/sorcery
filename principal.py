# Squelette de script pygame
import pygame
import random

WIDTH = 360 # taille écran largeur hauteur
HEIGHT = 480
FPS = 30 # images par seconde

# couleurs prédéfinies
BLACK = (0, 0, 0)
ROUGE = (255,0,0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init() # initialisation des sons
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorcery")
clock = pygame.time.Clock()

# boucle de jeu
running = True
while running:
    # assure que la boucle fonctionne au rythme donné par FPS
    clock.tick(FPS)
    # traitement des événements
    for event in pygame.event.get():
        # evenement fermeture de la fenetre pygame
        if event.type == pygame.QUIT:
            running = False

    # mise à jour des variables

    # dessin
    screen.fill(BLACK)
    # affichage
    pygame.display.flip()

pygame.quit()
