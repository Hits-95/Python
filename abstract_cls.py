from abc import ABC, abstractclassmethod


class Shape(ABC):
    """
   shape abstract..
    """
    @abstractclassmethod
    def printArea(self):
        return 0


class Reactangle(Shape):
    """
    docstring
    """

    def printArea(self):
        print("Hitesh")


if __name__ == "__main__":
    Reactangle().printArea()
