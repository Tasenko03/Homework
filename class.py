
"""Придумайте и напишсвой класс, у объектов которого будут атрибуты и методы.

a) Опишите текстом, какие характеристики будут у объекта этого класса и что этот объект сможет делать (4 балла).

Определите класс. Для этого:
б) напишите конструктор (метод __init__()) (2 балла);
в) определите другие методы объектов этого класса (1 балл).

Продемонстрируйте работу этого класса:
г) создайте объект класса (1 балл);
д) обратитесь к атрибутам данного объекта (1 балл);
e) вызовите методы данного объекта (1 балл)."""

import math
import random

class Cone:
    """This class describes cones. A radius, a height and a slant_height are attributes of the objects of this class.
We can find the volume and the full area of surface of the cone."""
    def __init__(self, radius, height, slant_height):
        self.radius, self.height, self.slant_height = radius, height, slant_height

    def calculate_volume(self):
        return 1/3 * math.pi * self.radius ** 2 * self.height

    def area_of_surface(self):
        return math.pi * self.radius * self.slant_height + math.pi * self.radius ** 2


cone = Cone(radius=5, height=10, slant_height=13)
print(f"\n{Cone.__doc__}\nCone\nRadius: {cone.radius}\nHeight: {cone.height}\nSlant_height: {cone.slant_height}\n"
      f"Volume: {round(cone.calculate_volume(), 1)}\nArea of surface: {round(cone.area_of_surface(), 1)}")
print(9888)
print(45)
