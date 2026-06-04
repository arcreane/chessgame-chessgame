import pygame
from src.models.pieces_types import *
from src.models.position import Position

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

    def getPiece(self, position):
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def chemin_libre(self, depart, arrivee):
        dcol = ord(arrivee.column) - ord(depart.column)
        drow = arrivee.row - depart.row
        pas = max(abs(dcol), abs(drow))
        sc = (dcol > 0) - (dcol < 0)
        sr = (drow > 0) - (drow < 0)
        for i in range(1, pas):
            col = chr(ord(depart.column) + sc * i)
            case = Position(col, depart.row + sr * i)
            if self.getPiece(case) is not None:
                return False
        return True

    def move_piece(self, depart, arrivee):
        piece = self.getPiece(depart)
        if piece is None:
            return
        mange = self.getPiece(arrivee)
        if mange is not None:
            self.pieces.remove(mange)
        piece.position = arrivee

    def jouer_coup(self, move):
        # move ressemble a "e2 e4". On verifie la regle puis on applique.
        cases = move.split()
        if len(cases) != 2:
            return False
        depart = Position.from_string(cases[0])
        arrivee = Position.from_string(cases[1])
        if depart is None or arrivee is None:
            return False
        piece = self.getPiece(depart)
        if piece is None or not piece.isValidMove(arrivee, self):
            return False
        self.move_piece(depart, arrivee)
        # Promotion : un pion qui atteint la derniere rangee est remplace.
        if isinstance(piece, Pawn) and arrivee.row in (1, 8):
            self.pieces.remove(piece)
            self.pieces.append(self.demander_promotion(piece))
        return True

    def demander_promotion(self, piece):
        # Petite fenetre : on choisit la piece en tapant Q, R, B ou N.
        font = pygame.font.SysFont("Arial", 28, bold=True)
        choix = {"q": Queen, "r": Rook, "b": Bishop, "n": Knight}
        while True:
            pygame.draw.rect(self.drawing_surface, (255, 255, 255), (120, 280, 400, 80))
            pygame.draw.rect(self.drawing_surface, (0, 0, 0), (120, 280, 400, 80), 2)
            txt = font.render("Promotion : Q  R  B  N ?", True, (0, 0, 0))
            self.drawing_surface.blit(txt, (140, 305))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.unicode.lower() in choix:
                    classe = choix[event.unicode.lower()]
                    nouvelle = classe(self.drawing_surface, 0, piece.color)
                    nouvelle.position = piece.position
                    return nouvelle


"coded by clement"
