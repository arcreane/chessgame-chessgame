from src.models.pieces_types import *

CASE = 80


class BoardGame:
    BACK_ROW = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

    def __init__(self, surface):
        self.surface = surface
        self.pieces = [
            cls(surface, i, c)
            for i, cls in enumerate(self.BACK_ROW)
            for c in Color_Piece
        ] + [
            Pawn(surface, i, c)
            for i in range(8)
            for c in Color_Piece
        ]

    def draw_pieces(self):
        for p in self.pieces:
            p.draw()

    def getPosition(self, piece):
        return piece.position if piece in self.pieces else None

    def getPiece(self, position):
        return next((p for p in self.pieces
                     if p.position.column == position.column
                     and p.position.row == position.row), None)
