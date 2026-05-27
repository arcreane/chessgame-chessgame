import pygame


class ChessTimer:
    TIMER_Y = 640
    TIMER_H = 100

    def __init__(self, minutes=10, get_ticks=None):
        ms = minutes * 60 * 1000
        self.times = [ms, ms]  # index 0 = WHITE, 1 = BLACK
        self.active = None
        self._last_tick = None
        self._get_ticks = get_ticks if get_ticks is not None else pygame.time.get_ticks

    def start(self, player_index):
        self.active = player_index
        self._last_tick = self._get_ticks()

    def tick(self):
        if self.active is None:
            return
        now = self._get_ticks()
        elapsed = now - self._last_tick
        self._last_tick = now
        self.times[self.active] = max(0, self.times[self.active] - elapsed)

    def stop(self):
        self.tick()
        self.active = None



    def is_timeout(self, player_index):
        return self.times[player_index] == 0

    def format(self, player_index):
        ms = max(0, self.times[player_index])
        s = ms // 1000
        return f"{s // 60:02d}:{s % 60:02d}"

    def draw(self, screen, names):
        self.tick()
        font = pygame.font.SysFont("Arial", 32, bold=True)

        pygame.draw.rect(screen, (0, 0, 0), (0, self.TIMER_Y, 640, self.TIMER_H))

        for i, (name, cx) in enumerate(zip(names, [160, 480])):
            color = (255, 215, 0) if self.active == i else (255, 255, 255)
            txt = font.render(f"{name} {self.format(i)}", True, color)
            screen.blit(txt, (cx - txt.get_width() // 2, self.TIMER_Y + 30))
