import abc
from abc import ABC, abstractclassmethod

class AbstractBaseClass(ABC):

    def printMethod(self):
        print("Abstract Base Class")            # Technically Abstract classes Cannot do this
                                                # Only baseclass with super() can invoke them

class ConcreteClass(AbstractBaseClass):

    def printMethod(self):
        super().printMethod()
        print("Concrete Class")


def main():
    shape = ConcreteClass()
    shape.printMethod()
    pass


if __name__ == '__main__':
    main()