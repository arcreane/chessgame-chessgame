import pygame, os
from abc import ABC, abstractmethod
from enum import Enum, auto
from src.models.position import Position


class Color_Piece(Enum):
    WHITE = auto()
    BLACK = auto()


COLS = 'abcdefgh'


def col_idx(c):
    return ord(c) - ord('a')


class Piece(ABC):
    _cache = {}

    def __init__(self, surface, index, color):
        self.position = Position(COLS[index], 1 if color == Color_Piece.WHITE else 8)
        self.color = color
        self.surface = surface

    @abstractmethod
    def __str__(self): pass

    def draw(self):
        from src.models.board import CASE
        key = f"{self}{('w' if self.color == Color_Piece.WHITE else 'b')}"
        if key not in Piece._cache:
            base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            img = pygame.image.load(os.path.join(base, "assets", "pieces", f"{key}.png")).convert_alpha()
            Piece._cache[key] = pygame.transform.scale(img, (CASE, CASE))
        x = col_idx(self.position.column) * CASE
        y = (8 - self.position.row) * CASE
        self.surface.blit(Piece._cache[key], (x, y))

    def _at(self, col, row, pieces):
        return next((p for p in pieces if p.position.column == col and p.position.row == row), None)

    def _friendly(self, col, row, pieces):
        p = self._at(col, row, pieces)
        return p is not None and p.color == self.color

    def _clear(self, fc, fr, tc, tr, pieces):
        dc = 0 if tc == fc else (1 if col_idx(tc) > col_idx(fc) else -1)
        dr = 0 if tr == fr else (1 if tr > fr else -1)
        c, r = col_idx(fc) + dc, fr + dr
        while (c, r) != (col_idx(tc), tr):
            if self._at(COLS[c], r, pieces):
                return False
            c += dc; r += dr
        return True

    def isValidMove(self, fc, fr, tc, tr, pieces):
        return False

 


class King(Piece):
    def __str__(self): return "K"
    def isValidMove(self, fc, fr, tc, tr, pieces):
        if self._friendly(tc, tr, pieces): return False
        return max(abs(col_idx(tc)-col_idx(fc)), abs(tr-fr)) == 1


class Queen(Piece):
    def __str__(self): return "Q"
    def isValidMove(self, fc, fr, tc, tr, pieces):
        if self._friendly(tc, tr, pieces): return False
        dc, dr = abs(col_idx(tc)-col_idx(fc)), abs(tr-fr)
        return (dc == 0 or dr == 0 or dc == dr) and self._clear(fc, fr, tc, tr, pieces)
 

class Rook(Piece):
    def __str__(self): return "R"

class Bishop(Piece):
    def __str__(self): return "B"
    def isValidMove(self, fc, fr, tc, tr, pieces):
        if self._friendly(tc, tr, pieces): return False
        dc, dr = abs(col_idx(tc)-col_idx(fc)), abs(tr-fr)
        return dc == dr and dc > 0 and self._clear(fc, fr, tc, tr, pieces)
 

class Knight(Piece):
    def __str__(self): return "N"


class Pawn(Piece):
    def __init__(self, surface, index, color):
        super().__init__(surface, index, color)
        self.position.row = 2 if color == Color_Piece.WHITE else 7
        self.has_moved = False

    def __str__(self): return "P"

    def isValidMove(self, fc, fr, tc, tr, pieces):
        d = 1 if self.color == Color_Piece.WHITE else -1
        dc, dr = col_idx(tc) - col_idx(fc), tr - fr
        if dc == 0:
            if dr == d:
                return self._at(tc, tr, pieces) is None
            if dr == 2*d and not self.has_moved:
                return self._at(tc, tr, pieces) is None and self._at(fc, fr+d, pieces) is None
        elif abs(dc) == 1 and dr == d:
            target = self._at(tc, tr, pieces)
            return target is not None and target.color != self.color
        return False
