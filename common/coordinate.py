class Coordinate:
    x : float
    y : float
    def __init__(self, x : float = 0, y : float = 0):
        self.x = float(x)
        self.y = float(y)
    def get_tuple(self) -> "tuple[float, float]":
        return (self.x, self.y)
    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)