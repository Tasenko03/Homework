def __init__(self, radius: float, height: float, d) -> None:
    """The function creates attributes of the objects of this class"""
    self.radius, self.height = radius, height
    self.slant_height = self.radius ** 2 + self.height ** 2
    self.d = d