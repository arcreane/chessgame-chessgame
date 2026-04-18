import pygame
import sys
from src.models.board import BoardGame, taille_case
from src.models.player import Player
from src.models.AIPlayer import AIPlayer


def dessiner_plateau(surface):
    for l in range(8):
        for c in range(8):
            color = (240, 217, 181) if (l + c) % 2 == 0 else (139, 131, 134)
            pygame.draw.rect(surface, color, (c * taille_case, l * taille_case, taille_case, taille_case))


def rafraichir(screen, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()

    dessiner_plateau(screen)
    board.draw_pieces()
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((taille_case * 8, taille_case * 8))
    board = BoardGame(screen)

    players = []
    for color, label in [(0, "BLANC"), (1, "NOIR")]:
        rafraichir(screen, board)
        name = input(f"Pseudo {label} ('AI' pour robot) : ")
        players.append(AIPlayer(color) if name.upper() == "AI" else Player(name, color))

    current_idx = 0
    while True:
        rafraichir(screen, board)
        p = players[current_idx]

        if isinstance(p, AIPlayer):
            pygame.time.delay(1000)
            move = p.askMove(board)
            print(f"IA joue : {move}")
        else:
            move = p.askMove()

        current_idx = 1 - current_idx


if __name__ == "__main__":
    main()
