import pygame, sys
from src.models.board import BoardGame
from src.models.player import Player
from src.models.AIPlayer import AIPlayer
from src.models.timer import ChessTimer


def draw_board(screen, board):
    for r in range(8):
        for c in range(8):
            col = (240, 217, 181) if (r + c) % 2 == 0 else (139, 131, 134)
            pygame.draw.rect(screen, col, (c * 80, r * 80, 80, 80))
    board.draw_pieces()


def show_timeout_screen(screen, board, winner_name, timer, names):
    draw_board(screen, board)
    timer.draw(screen, names)

    overlay = pygame.Surface((640, 640), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    font_big = pygame.font.SysFont("Arial", 44, bold=True)
    font_small = pygame.font.SysFont("Arial", 26)

    msg = font_big.render(f"{winner_name} wins on time!", True, (255, 215, 0))
    sub = font_small.render("Window closes in 4 seconds…", True, (200, 200, 200))
    screen.blit(msg, (320 - msg.get_width() // 2, 280))
    screen.blit(sub, (320 - sub.get_width() // 2, 340))
    pygame.display.flip()
    pygame.time.delay(4000)


def main():
    pygame.init()
    # 640 board + 100 timer strip
    screen = pygame.display.set_mode((640, 740))
    pygame.display.set_caption("Chess Game")
    board = BoardGame(screen)

    players = []
    for c, l in [(0, "BLANC"), (1, "NOIR")]:
        n = input(f"Nom {l} (ou AI) : ")
        players.append(AIPlayer(c) if n.upper() == "AI" else Player(n, c))

    names = [p.name for p in players]
    timer = ChessTimer(minutes=10)
    curr = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(screen, board)
        timer.draw(screen, names)
        pygame.display.flip()

        p = players[curr]
        timer.start(curr)
        move = p.askMove(screen, timer, names)
        timer.stop()

        if move is None:
            winner = players[1 - curr].name
            show_timeout_screen(screen, board, winner, timer, names)
            pygame.quit()
            sys.exit()

        print(f"{p.name} joue {move}")
        curr = 1 - curr


if __name__ == "__main__":
    main()
