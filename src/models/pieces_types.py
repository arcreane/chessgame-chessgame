import pygame
from abc import ABC, abstractmethod
from src.models.position import Position
from enum import Enum, auto


class Color_Piece(Enum):
    WHITE = auto()
    BLACK = auto()


class Piece(ABC):
    colonnes_lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, drawing_surface, index, color):
        column = Piece.colonnes_lettres[index]
        row = 1 if color == Color_Piece.WHITE else 8

        self.position = Position(column, row)
        self.color = color
        self.drawing_surface = drawing_surface

    @abstractmethod
    def __str__(self):
        pass

    def draw(self):
        from src.models.board import taille_case

        col_idx = ord(self.position.column) - ord('a')
        row_idx = 8 - self.position.row

        x = col_idx * taille_case + taille_case // 2
        y = row_idx * taille_case + taille_case // 2

        couleur_visuelle = (255, 255, 255) if self.color == Color_Piece.WHITE else (50, 50, 50)

        pygame.draw.circle(self.drawing_surface, couleur_visuelle, (x, y), taille_case // 3)

        font = pygame.font.SysFont("Arial", 24, bold=True)
        texte_couleur = (0, 0, 0) if self.color == Color_Piece.WHITE else (255, 255, 255)
        text_surf = font.render(self.__str__(), True, texte_couleur)
        text_rect = text_surf.get_rect(center=(x, y))
        self.drawing_surface.blit(text_surf, text_rect)


class King(Piece):
    def __str__(self): return "K"

class Queen(Piece):
    def __str__(self): return "Q"

class Rook(Piece):
    def __str__(self): return "R"

class Bishop(Piece):
    def __str__(self): return "B"

class Knight(Piece):
    def __str__(self): return "N"

class Pawn(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, index, color)
        self.position.row = 2 if color == Color_Piece.WHITE else 7

    def __str__(self): return "P"
