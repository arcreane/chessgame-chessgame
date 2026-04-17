import random
from src.models.player import Player

class AIPlayer(Player):
    def __init__(self, color: int):
        super().__init__("AI", color)

    def askMove(self, board=None) -> str:
        cols = "abcdefgh"
        move = f"P{random.choice(cols)}2 {random.choice(cols)}4"
        return move
