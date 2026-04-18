from abc import ABC, abstractmethod
import pygame
import os
from enum import Enum, auto
from src.models.position import Position


class PieceTypes(Enum):
    KING = auto()
    QUEEN = auto()
    BISHOP = auto()
    KNIGHT = auto()
    ROOK = auto()
    PAWN = auto()


class Color_Piece(Enum):
    WHITE = auto()
    BLACK = auto()


# Correspondance PieceTypes -> lettre fichier image
PIECE_LETTER = {
    PieceTypes.KING:   "K",
    PieceTypes.QUEEN:  "Q",
    PieceTypes.BISHOP: "B",
    PieceTypes.KNIGHT: "N",
    PieceTypes.ROOK:   "R",
    PieceTypes.PAWN:   "P",
}

# Correspondance Color_Piece -> lettre fichier image
COLOR_LETTER = {
    Color_Piece.WHITE: "w",
    Color_Piece.BLACK: "b",
}

# Chemin vers les images
IMAGES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets", "pieces")

# Cache global des images
_images_cache = {}


def get_piece_image(piece_type: PieceTypes, color: Color_Piece) -> pygame.Surface:
    """Charge et retourne l'image d'une pièce (avec mise en cache)."""
    from src.models.board import taille_case
    key = (piece_type, color)
    if key not in _images_cache:
        filename = f"{PIECE_LETTER[piece_type]}{COLOR_LETTER[color]}.png"
        filepath = os.path.join(IMAGES_PATH, filename)
        image = pygame.image.load(filepath).convert_alpha()
        _images_cache[key] = pygame.transform.scale(image, (taille_case, taille_case))
    return _images_cache[key]


class Piece(ABC):
    colonnes_lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    pieces_colonne = {
        PieceTypes.KING:   ["e"],
        PieceTypes.QUEEN:  ["d"],
        PieceTypes.ROOK:   ["a", "h"],
        PieceTypes.KNIGHT: ["b", "g"],
        PieceTypes.BISHOP: ["c", "f"],
        PieceTypes.PAWN:   ["a", "b", "c", "d", "e", "f", "g", "h"],
    }

    def __init__(self, drawing_surface, piece_type, index, color):
        column = Piece.pieces_colonne[piece_type][index]
        row = 1 if color == Color_Piece.WHITE else 8

        self.position = Position(column, row)
        self.color = color
        self.type = piece_type
        self.drawing_surface = drawing_surface

    @abstractmethod
    def __str__(self):
        pass

    def isValidMove(self, newPosition, board):
        return True

    def draw(self):
        from src.models.board import taille_case
        image = get_piece_image(self.type, self.color)
        col_idx = ord(self.position.column) - ord('a')
        row_idx = 8 - self.position.row
        x = col_idx * taille_case
        y = row_idx * taille_case
        self.drawing_surface.blit(image, (x, y))


class King(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.KING, 0, color)

    def __str__(self):
        return "K"


class Queen(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.QUEEN, 0, color)

    def __str__(self):
        return "Q"


class Bishop(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.BISHOP, index, color)

    def __str__(self):
        return "B"


class Knight(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.KNIGHT, index, color)

    def __str__(self):
        return "N"


class Rook(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.ROOK, index, color)

    def __str__(self):
        return "R"


class Pawn(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.PAWN, index, color)
        self.position.row = 2 if color == Color_Piece.WHITE else 7

    def __str__(self):
        return "P"