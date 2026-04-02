from src.models.position import Position
from src.models.pieces_types import Piece, King, Queen, Bishop, Knight, Rook, Pawn, Color_Piece

taille_case_droite = 8
taille_case_gauche = 10
taille_case = taille_case_droite * taille_case_gauche


class BoardGame:
    pieces_constructor = [Rook,  Knight, Bishop,  King, Queen, Bishop, Knight, Rook ]
    def __init__(self, drawing_surface):
        self.pieces = []
        self.grid = {}
        self._initialize_pieces(drawing_surface)

    def _add_piece(self, piece):
        self.pieces.append(piece)
        self.grid[str(piece.position)] = piece

    def _initialize_pieces(self, drawing_surface):
        for index, contructor in enumerate(BoardGame.pieces_constructor):
            self._add_piece(contructor(drawing_surface, 2*index// len(BoardGame.pieces_constructor), Color_Piece.WHITE))
            self._add_piece(contructor(drawing_surface, 2 * index // len(BoardGame.pieces_constructor), Color_Piece.BLACK))


    def getPosition(self, piece):
        if piece in self.pieces and piece.position is not None:
            return piece.position
        return None

    def getPiece(self, position):
        return self.grid.get(str(position), None)

    def draw_pieces(self):
        for piece in self.pieces:
            piece.draw()