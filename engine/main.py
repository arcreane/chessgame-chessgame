import pygame
import sys
from src.models.board import BoardGame, taille_case
from src.models.player import Player
from src.models.AIPlayer import AIPlayer


WHITE_CELL = (240, 217, 181)
LAVENDER_CELL = (139, 131, 134)


def dessiner_plateau(surface):
    for ligne in range(8):
        for colonne in range(8):
            couleur = WHITE_CELL if (ligne + colonne) % 2 == 0 else LAVENDER_CELL
            pygame.draw.rect(surface, couleur,pygame.Rect(colonne * taille_case, ligne * taille_case,taille_case, taille_case))


def rafraichir_interface(screen, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dessiner_plateau(screen)
    board.draw_pieces()
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((taille_case * 8, taille_case * 8))
    pygame.display.set_caption("Échec")
    board = BoardGame(screen)

    print("Configuration de la partie")
    players = []
    for color, label in [(0, "BLANC"), (1, "NOIR")]:
        rafraichir_interface(screen, board)
        name = input(f"Nom du joueur {label} ('AI' pour l'ordinateur) : ").strip()
        if name.upper() == "AI":
            players.append(AIPlayer(color))
        else:
            players.append(Player(name, color))

    current_idx = 0
    clock = pygame.time.Clock()
    running = True

    print("\n Début de partie")
    while running:
        rafraichir_interface(screen, board)

        current_player = players[current_idx]

        if isinstance(current_player, AIPlayer):
            pygame.time.delay(1000)
            move = current_player.askMove(board)
            print(f"L'IA ({current_player.name}) a joué : {move}")
            current_idx = 1 - current_idx
        else:
            move = current_player.askMove()
            print(f"{current_player.name} a joué : {move}")
            current_idx = 1 - current_idx

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
