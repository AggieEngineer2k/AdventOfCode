class Coordinate:
    x : float
    y : float
    def __init__(self, x : float = 0, y : float = 0):
        self.x = x
        self.y = y
    def get_tuple(self) -> "tuple[float, float]":
        return (self.x, self.y)