from abc import ABC, abstractmethod

import pygame

from src.models import position

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


piece_position = {}


class Piece(ABC):
    pieces_colonne = {PieceTypes.KING: ["e"],
                      PieceTypes.QUEEN: ["d"],
                      PieceTypes.ROOK: ["a", "h"],
                      PieceTypes.KNIGHT: ["b", "g"],
                      PieceTypes.BISHOP: ["c", "f"],
                      }

    def __init__(self, drawing_surface, type, index, color):
        column = Piece.pieces_colonne[type][index]
        row = 1
        if color == Color_Piece.BLACK:
            row = 8

        self.position = Position(column, row)
        self.color = color
        self.drawing_surface = drawing_surface

    @abstractmethod
    def isValidMove(self, newPosition, board):
        pass

    def draw(self) :
        pygame.draw.circle(self.drawing_surface, (24, 21, 255),(self.position.get_col() *80 +40, self.position.row*80 -40), 5)

class King(Piece):
    def __init__(self, drawing_surface,index, color):
        super().__init__(drawing_surface, PieceTypes.KING, 0, color)

    def __str__(self):
        return "K"

    def isValidMove(self, newPosition, board):
        return True


class Queen(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.QUEEN, 0, color)

    def __str__(self):
        return "Q"

    def isValidMove(self, newPosition, board):
        return True


class Bishop(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.BISHOP, index, color)

    def __str__(self):
        return "B"

    def isValidMove(self, newPosition, board):
        return True


class Knight(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface, PieceTypes.KNIGHT, index, color)

    def __str__(self):
        return "N"

    def isValidMove(self, newPosition, board):
        return True


class Rook(Piece):
    def __init__(self, drawing_surface, index, color):
        super().__init__(drawing_surface,PieceTypes.ROOK, index, color)

    def __str__(self):
        return "R"

    def isValidMove(self, newPosition, board):
        return True


class Pawn(Piece):
    def __str__(self):
        return "P"

    def isValidMove(self, newPosition, board):
        return True
