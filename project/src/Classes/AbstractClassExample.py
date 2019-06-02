from abc import ABC, abstractclassmethod

class Polygon(ABC):

    def numSides(self):
        pass

class Triangle(Polygon):

    def numSides(self):
        print("Triangle has 3 sides")

class Square(Polygon):
    def numSides(self):
        print("Square has 4 sides")

class Hexagon(Polygon):
    def numSides(self):
        print("Hexagon has 6 sides")


def main():
    shape = Triangle()
    shape.numSides()

    shape = Square()
    shape.numSides()

    shape = Hexagon()
    shape.numSides()

    pass


if __name__ == '__main__':
    main()

'''

Abstract Method
- Abstract method is provided by the Parent class but only implemented by the child(i.e Concrete) class

What ? 
- Blueprint for other sub classes
- Allows to create set of methods that must be created within any child classes

How ? 
- Python cannot provide Abstract classes 
- Instead, it uses a module called "ABC" (Abstract Base Class)
- Marks methods of the base class as abstract and then registering concrete classes as imlpementation


'''