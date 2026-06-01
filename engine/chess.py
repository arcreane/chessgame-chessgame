import pygame, sys
from src.models.board import BoardGame, CASE
from src.models.player import Player
from src.models.AIPlayer import AIPlayer


def parse_move(move):
    """'Nb1 Nc3' → ('N','b',1,'c',3) ou None si format invalide."""
    try:
        src, dst = move.strip().split()
        if len(src) != 3 or len(dst) != 3: return None
        pl = src[0].upper()
        if pl not in 'KQRBNP': return None
        fc, fr, tc, tr = src[1].lower(), int(src[2]), dst[1].lower(), int(dst[2])
        if fc not in 'abcdefgh' or tc not in 'abcdefgh': return None
        if not (1 <= fr <= 8 and 1 <= tr <= 8): return None
        return pl, fc, fr, tc, tr
    except:
        return None


class Chess:
    def __init__(self, screen):
        self.screen = screen
        self.board = BoardGame(screen)
        self.players = []
        self.currentPlayer = None

    def initPlayers(self):
        from src.models.pieces_types import Color_Piece
        for color, label in zip([Color_Piece.WHITE, Color_Piece.BLACK], ["BLANC", "NOIR"]):
            name = input(f"Nom joueur {label} (ou AI) : ").strip()
            self.players.append(AIPlayer(color) if name.upper() == "AI" else Player(name, color))
        self.currentPlayer = self.players[0]

    def displayBoard(self):
        for r in range(8):
            for c in range(8):
                pygame.draw.rect(self.screen,
                    (240, 217, 181) if (r+c) % 2 == 0 else (139, 131, 134),
                    (c*CASE, r*CASE, CASE, CASE))
        self.board.draw_pieces()
        pygame.display.flip()

    def isValidMove(self, move):
        p = parse_move(move)
        if not p: return False
        pl, fc, fr, tc, tr = p
        piece = next((x for x in self.board.pieces
                      if x.position.column == fc and x.position.row == fr
                      and x.color == self.currentPlayer.color and str(x) == pl), None)
        return piece.isValidMove(fc, fr, tc, tr, self.board.pieces) if piece else False

    def isCheckMate(self):
        return False

    def updateBoard(self, move):
        _, fc, fr, tc, tr = parse_move(move)
        piece = next((x for x in self.board.pieces
                      if x.position.column == fc and x.position.row == fr
                      and x.color == self.currentPlayer.color), None)
        if not piece: return
        self.board.pieces = [x for x in self.board.pieces
                             if not (x.position.column == tc and x.position.row == tr and x != piece)]
        piece.position.column, piece.position.row = tc, tr
        from src.models.pieces_types import Pawn
        if isinstance(piece, Pawn):
            piece.has_moved = True

    def switchPlayer(self):
        self.currentPlayer = self.players[1] if self.currentPlayer == self.players[0] else self.players[0]

    def play(self):
        from src.models.timer import ChessTimer
        self.initPlayers()
        names = [p.name for p in self.players]
        timer = ChessTimer(minutes=10)
        font = pygame.font.SysFont("Arial", 20)

        while not self.isCheckMate():
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

            self.displayBoard()
            timer.draw(self.screen, names)
            pygame.display.flip()

            idx = self.players.index(self.currentPlayer)
            timer.start(idx)
            self.currentPlayer._chess_ref = self

            while True:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit(); sys.exit()

                move = self.currentPlayer.askMove(self.screen, timer, names)
                if move is None:
                    return

                if self.isValidMove(move):
                    break

                # Afficher erreur
                self.displayBoard()
                timer.draw(self.screen, names)
                pygame.draw.rect(self.screen, (30, 30, 30), (0, 648, 640, 28))
                self.screen.blit(font.render(f"Invalide: {move} — réessayez", True, (220, 60, 60)), (10, 651))
                pygame.display.flip()

            timer.stop()
            self.updateBoard(move)
            self.switchPlayer()
