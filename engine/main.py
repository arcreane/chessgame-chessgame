import pygame, sys
from chess import Chess


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 740))
    pygame.display.set_caption("Chess Game")

    game = Chess(screen)
    game.play()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
