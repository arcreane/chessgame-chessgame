class Position:
    def __init__(self, column, row):
        self.column = column.lower()
        self.row = row

    def __str__(self):
        return f"{self.column}{self.row}"

    def get_col(self):
        return ord(self.column) - ord('a')


    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    @staticmethod
    def from_string(text):
        if len(text) != 2:
            return None
        col = text[0].lower()
        if col < 'a' or col > 'h' or not text[1].isdigit():
            return None
        row = int(text[1])
        if row < 1 or row > 8:
            return None
        return Position(col, row)
