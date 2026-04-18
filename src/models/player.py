import pygame

class Player:
    def __init__(self, name: str, color: int):
        self._name = name
        self._color = color

    @property
    def name(self): return self._name

    def askMove(self, screen) -> str:
        input_text = ""
        font = pygame.font.SysFont("Arial", 28)
        clock = pygame.time.Clock()
        box_width, box_height = 300, 50
        box_rect = pygame.Rect((screen.get_width() - box_width) // 2,
                               (screen.get_height() - box_height) // 2,
                               box_width, box_height)
        typing = True
        while typing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    import sys; sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        typing = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        if len(input_text) < 7:
                            input_text += event.unicode
            pygame.draw.rect(screen, (50, 50, 50), box_rect.move(4, 4))
            pygame.draw.rect(screen, (255, 255, 255), box_rect)
            pygame.draw.rect(screen, (0, 0, 0), box_rect, 2)
            prompt_surf = font.render(f"{self._name} : {input_text}", True, (0, 0, 0))
            screen.blit(prompt_surf, (box_rect.x + 10, box_rect.y + 10))
            pygame.display.flip()
            clock.tick(30)
        return input_text
