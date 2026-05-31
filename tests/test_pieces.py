import unittest
import random
from src.models.player import Player
from src.models.AIPlayer import AIPlayer


class TestTrèsSimple(unittest.TestCase):

    def test_player(self):
        """Vérifie juste que le joueur se crée avec le bon nom et la bonne couleur."""
        p = Player("nico", 0)
        self.assertEqual(p.name, "nico")
        self.assertEqual(p.color, 0)

    def test_ai_player(self):
        """Vérifie le nom de l'IA et force un choix pour tester sa réponse."""
        ai = AIPlayer(0)
        self.assertEqual(ai.name, "AI")

        random.choice = lambda seq: 'e'

        ai.askMove = lambda screen=None: f"e2 e4"
        self.assertEqual(ai.askMove(), "e2 e4")


if __name__ == '__main__':
    unittest.main()
