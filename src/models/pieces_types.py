import pygame
from abc import ABC, abstractmethod
from src.models.position import Position
from enum import Enum, auto


class Color_Piece(Enum):
    WHITE = auto()
    BLACK = auto()


class Piece(ABC):
    colonnes_lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    _images_cache = {}  # Cache pour ne charger chaque image qu'une fois

    def __init__(self, drawing_surface, index, color):
        column = Piece.colonnes_lettres[index]
        row = 1 if color == Color_Piece.WHITE else 8

        self.position = Position(column, row)
        self.color = color
        self.drawing_surface = drawing_surface

    @abstractmethod
    def __str__(self):
        pass

    def _get_image_key(self):
        """Retourne le nom du fichier image, ex: 'Kw' pour King blanc"""
        suffix = 'w' if self.color == Color_Piece.WHITE else 'b'
        return f"{str(self)}{suffix}"  # ex: "Kw", "Pb", "Rw"...

    def _load_image(self):
        from src.models.board import taille_case
        import os
        key = self._get_image_key()
        if key not in Piece._images_cache:
            # Remonte de src/models/ jusqu'à la racine du projet
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            path = os.path.join(base_dir, "assets", "pieces", f"{key}.png")
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (taille_case, taille_case))
            Piece._images_cache[key] = img
        return Piece._images_cache[key]

    def draw(self):
        from src.models.board import taille_case
        col_idx = ord(self.position.column) - ord('a')
        row_idx = 8 - self.position.row
        x = col_idx * taille_case
        y = row_idx * taille_case

        image = self._load_image()
        self.drawing_surface.blit(image, (x, y))


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
