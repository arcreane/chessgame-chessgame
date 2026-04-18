import random, pygame
from src.models.player import Player

class AIPlayer(Player):
    def __init__(self, color):
        super().__init__("AI", color)

    def askMove(self, screen):
        from src.models.board import taille_case
        c = random.choice("abcdefgh")
        r1, r2 = (2, 4) if self.color == 0 else (7, 5)
        rect = pygame.Rect((ord(c)-ord('a'))*taille_case, (8-r1)*taille_case, taille_case, taille_case)
        pygame.draw.rect(screen, (0, 255, 0), rect, 5)
        pygame.display.flip()
        pygame.time.delay(1000)
        return f"{c}{r1} {c}{r2}"
