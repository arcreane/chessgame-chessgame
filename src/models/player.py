import pygame


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def askMove(self, screen, timer=None, names=None):
        font = pygame.font.SysFont("Arial", 22)
        text = ""
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return None
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN and len(text) == 7:
                        return text
                    elif e.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) < 7:
                        text += e.unicode

            pygame.draw.rect(screen, (255, 255, 255), (80, 290, 480, 46))
            pygame.draw.rect(screen, (0, 0, 0), (80, 290, 480, 46), 2)
            screen.blit(font.render(f"{self.name}: {text}_", True, (0, 0, 0)), (90, 302))
            screen.blit(pygame.font.SysFont("Arial", 16).render(
                "ex: Pe2 Pe4  |  Nb1 Nc3", True, (80, 80, 80)), (90, 342))
            if timer and names:
                timer.draw(screen, names)
            pygame.display.flip()
