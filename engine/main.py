import pygame, sys
from src.models.board import BoardGame, taille_case
from src.models.player import Player
from src.models.AIPlayer import AIPlayer


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    board = BoardGame(screen)


    players = []
    for c, l in [(0, "BLANC"), (1, "NOIR")]:
        n = input(f"Nom {l} (ou AI) : ")
        players.append(AIPlayer(c) if n.upper() == "AI" else Player(n, c))

    curr = 0
    while True:
        for r in range(8):
            for c in range(8):
                col = (240, 217, 181) if (r + c) % 2 == 0 else (139, 131, 134)
                pygame.draw.rect(screen, col, (c * 80, r * 80, 80, 80))
        board.draw_pieces()
        pygame.display.flip()

        # Tour par tour
        p = players[curr]
        if isinstance(p, AIPlayer):
            move = p.askMove(screen)
        else:
            move = p.askMove(screen)

        print(f"{p.name} joue {move}")
        curr = 1 - curr


if __name__ == "__main__":
    main()
