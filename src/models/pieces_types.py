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

    def _ecart(self, newPosition):
        dcol = ord(newPosition.column) - ord(self.position.column)
        drow = newPosition.row - self.position.row
        return dcol, drow

    def _arrivee_libre(self, newPosition, board):
        piece = board.getPiece(newPosition)
        return piece is None or piece.color != self.color

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

    def isValidMove(self, newPosition, board):
        dcol, drow = self._ecart(newPosition)
        if abs(dcol) <= 1 and abs(drow) <= 1 and (dcol != 0 or drow != 0):
            return self._arrivee_libre(newPosition, board)
        return False

class Queen(Piece):
    def __str__(self): return "Q"

    def isValidMove(self, newPosition, board):
        dcol, drow = self._ecart(newPosition)
        droite = (dcol == 0 or drow == 0)
        diago = (abs(dcol) == abs(drow))
        if (dcol == 0 and drow == 0) or not (droite or diago):
            return False
        if not board.chemin_libre(self.position, newPosition):
            return False
        return self._arrivee_libre(newPosition, board)

class Rook(Piece):
    def __str__(self): return "R"

    def isValidMove(self, newPosition, board):
        dcol, drow = self._ecart(newPosition)
        if (dcol == 0) == (drow == 0):
            return False
        if not board.chemin_libre(self.position, newPosition):
            return False
        return self._arrivee_libre(newPosition, board)

class Bishop(Piece):
    def __str__(self): return "B"

    def isValidMove(self, newPosition, board):
        dcol, drow = self._ecart(newPosition)
        if dcol == 0 or abs(dcol) != abs(drow):
            return False
        if not board.chemin_libre(self.position, newPosition):
            return False
        return self._arrivee_libre(newPosition, board)

class Knight(Piece):
    def __str__(self): return "N"

    def isValidMove(self, newPosition, board):
        dcol, drow = self._ecart(newPosition)
        if (abs(dcol), abs(drow)) in [(1, 2), (2, 1)]:
            return self._arrivee_libre(newPosition, board)
        return False

class Pawn(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, index, color)
        self.position.row = 2 if color == Color_Piece.WHITE else 7

    def __str__(self): return "P"

    def isValidMove(self, newPosition, board):
        dcol, drow = self._ecart(newPosition)
        sens = 1 if self.color == Color_Piece.WHITE else -1
        depart = 2 if self.color == Color_Piece.WHITE else 7
        cible = board.getPiece(newPosition)
        if dcol == 0:
            if drow == sens and cible is None:
                return True
            if drow == 2 * sens and self.position.row == depart and cible is None:
                milieu = Position(self.position.column, self.position.row + sens)
                if board.getPiece(milieu) is None:
                    return True
            return False
        if abs(dcol) == 1 and drow == sens and cible is not None and cible.color != self.color:
            return True
        return False
