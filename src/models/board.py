from src.models.pieces_types import *

taille_case = 80

class BoardGame:
    pieces_constructor = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

    def __init__(self, drawing_surface):
        self.pieces = []
        self.drawing_surface = drawing_surface
        self._initialize_pieces()

    def _initialize_pieces(self):
        for index, constructor in enumerate(BoardGame.pieces_constructor):
            self.pieces.append(constructor(self.drawing_surface, index, Color_Piece.WHITE))
            self.pieces.append(constructor(self.drawing_surface, index, Color_Piece.BLACK))
            self.pieces.append(Pawn(self.drawing_surface, index, Color_Piece.WHITE))
            self.pieces.append(Pawn(self.drawing_surface, index, Color_Piece.BLACK))

    def draw_pieces(self):
        for piece in self.pieces:
            piece.draw()
