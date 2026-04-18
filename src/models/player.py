class Player:
    def __init__(self, name: str, color: int):
        self._name = name
        self._color = color

    @property
    def name(self):
        return self._name
    @property
    def color(self):
        return self._color

    def askMove(self):
        return input(f"[{self._name}] A ton tour (ex: e2 e4) : ")
