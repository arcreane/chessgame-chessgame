import pygame
import sys

from src.models.board import *

pygame.init()

nb_cases = 8
LARGEUR = taille_case * nb_cases
HAUTEUR = taille_case * nb_cases

# Couleurs
White = (240, 217, 181)
Lavender = (139,131,134,255) #139, 131, 134, 255

# Création de la fenêtre
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))


def dessiner_plateau(surface):
    for ligne in range(8):
        for colonne in range(8):
            if (ligne + colonne) % 2 == 0:
                couleur = White
            else:
                couleur = Lavender

            rect = pygame.Rect(colonne * taille_case, ligne * taille_case, taille_case, taille_case)
            pygame.draw.rect(surface, couleur, rect)

playing_board = BoardGame(screen)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dessiner_plateau(screen)
    playing_board.draw_pieces()
    pygame.display.flip()

pygame.quit()
sys.exit()