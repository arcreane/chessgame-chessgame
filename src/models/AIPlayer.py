import random, pygame
from src.models.player import Player


class AIPlayer(Player):
    def __init__(self, color):
        super().__init__("AI", color)

    def askMove(self, screen, timer=None, names=None):
        chess = getattr(self, '_chess_ref', None)
        cols = 'abcdefgh'
        move = None

        if chess:
            valid = []
            for p in [p for p in chess.board.pieces if p.color == self.color]:
                for tc in cols:
                    for tr in range(1, 9):
                        m = f"{p}{p.position.column}{p.position.row} {p}{tc}{tr}"
                        if chess.isValidMove(m):
                            valid.append(m)
            if valid:
                move = random.choice(valid)

        if not move:
            move = f"P{random.choice(cols)}{random.randint(1,8)} P{random.choice(cols)}{random.randint(1,8)}"

        # Affichage
        font = pygame.font.SysFont("Arial", 20)
        pygame.draw.rect(screen, (220, 255, 220), (80, 290, 480, 46))
        screen.blit(font.render(f"AI joue: {move}", True, (0, 0, 0)), (90, 302))
        if timer and names:
            timer.draw(screen, names)
        pygame.display.flip()
        pygame.time.delay(500)
        return move
