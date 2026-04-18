import pygame


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def askMove(self, screen):
        input_text = ""
        font = pygame.font.SysFont("Arial", 25)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(input_text) == 5:
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            rect = pygame.Rect(140, 300, 360, 50)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            txt = font.render(f"{self.name} (ex: e2 e4) : {input_text}", True, (0, 0, 0))
            screen.blit(txt, (rect.x + 10, rect.y + 10))
            pygame.display.flip()
